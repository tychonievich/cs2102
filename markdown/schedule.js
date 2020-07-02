var today = new Date().toISOString().substr(0,10);

document.querySelectorAll('.day').forEach(function(x){
    if (!x.getAttribute('date')) return;
    if (x.getAttribute('date') < today) x.classList.add('past');
    else {
        /* if (x.getAttribute('date') == today) x.classList.add('today');
        else */ x.classList.add('future');
        x.parentElement.classList.remove('past');
    }
});
document.querySelectorAll('.week').forEach(function(x){
    if (x.querySelector('.future'))
        x.classList.add('future');
    else
        x.classList.add('past');
});
document.querySelector('.day:not(.past) div').parentElement.classList.add('today');




function viewmode(me) {
    if (me.value) me = me.value;
    if (!document.getElementById('viewmode='+me)) {
        console.log('ignoring', me, 'setting to calendar instead')
        me = 'calendar'
    }
    document.getElementById('schedule').classList.remove('calendar');
    document.getElementById('schedule').classList.remove('agenda');
    document.getElementById('schedule').classList.add(me);
    localStorage.setItem('viewmode', me);
    if (!document.getElementById('viewmode='+me).checked) {
        document.getElementById('viewmode='+me).checked = true;
    }
}
function show(me,val) {
    if (me.value) return show(me.value, me.checked);
    let css = document.getElementById('schedule-css');
    if (val) {
        for(let i=0; i<css.sheet.cssRules.length; i+=1) {
            if (css.sheet.cssRules[i].cssText == '.'+me+' { display: none; }') {
                css.sheet.deleteRule(i);
                break;
            }
        }
    } else {
        css.sheet.insertRule('.'+me+' { display: none; }');
    }
    localStorage.setItem('view_'+me, val);
}

function showPast(visible) {
    if (typeof(visible) != 'boolean') {
        visible = visible.checked;
        localStorage.setItem('showpast', visible);
        //console.log('showPast button',visible)
    } else {
        //console.log('showPast cookie',visible)
    }
    let css = document.getElementById('schedule-css');
    if (visible) {
        for(let i=0; i<css.sheet.cssRules.length; i+=1) {
            if (css.sheet.cssRules[i].cssText == '.calendar .week.past { display: none; }')
            { css.sheet.deleteRule(i); i-=1; }
            else if (css.sheet.cssRules[i].cssText == '.calendar > .day.past { display: none; }')
            { css.sheet.deleteRule(i); i-=1; }
            else if (css.sheet.cssRules[i].cssText == '.agenda .day.past { display: none; }')
            { css.sheet.deleteRule(i); i-=1; }
            else if (css.sheet.cssRules[i].cssText == '.agenda .week.past { display: none; }')
            { css.sheet.deleteRule(i); i-=1; }
        }
    } else {
        css.sheet.insertRule('.calendar .week.past { display: none; }');
        css.sheet.insertRule('.calendar > .day.past { display: none; }');
        css.sheet.insertRule('.agenda .day.past { display: none; }');
        css.sheet.insertRule('.agenda .week.past { display: none; }');
    }
    document.getElementById('showpast').checked = visible;
}

document.querySelectorAll('input[name="show"]').forEach(x => {
    if (localStorage.getItem('view_'+x.value) == 'true')
        x.checked = true
    else
        x.checked = false
    show(x)
})

viewmode(localStorage.getItem('viewmode'))
showPast(localStorage.getItem('showpast') == 'true')

