---
title: Fall 2020 Schedule
...

At the time this note was written, UVA had not stated the exact structure of the semester. They've stated we'll not return to grounds after Thanksgiving break, but not stated if that means we'll have finals before then, or after then, or have a post-Thanksgiving week of online courses before finals. As that information is released, the schedule is likely to be updated.

<hr/>

<style id="schedule-css">

#schedule.calendar {
    display: grid;
    width: 100%; 
    background: rgba(0,0,0,0.125); 
    border: 0.5ex solid rgba(0,0,0,0);
    border-radius: 1.5ex; 
}
.calendar .day.Sun { grid-column: 1}
.calendar .day.Mon { grid-column: 2}
.calendar .day.Tue { grid-column: 3}
.calendar .day.Wed { grid-column: 4}
.calendar .day.Thu { grid-column: 5}
.calendar .day.Fri { grid-column: 6}
.calendar .day.Sat { grid-column: 7}

.calendar .day { 
    background: white;
    border-radius: 1ex;
    padding: .25ex .5ex;
    margin: .25ex;
    box-sizing:border-box; 
    overflow: hidden;
}


#schedule td, #schedule th { padding: 0ex; }

.calendar span.date { 
    font-size: 70.7%;
    padding-left: 0.5ex;
    float:right;
    margin-top:-0.5ex;
}
.calendar div {
    padding: 0 0.5ex 0 0.5ex;
    margin: 0 -0.5ex 0 -0.5ex;
}
.calendar div.day div:first-child {
    padding-top: 0.5ex;
    margin-top: -0.5ex;
}
.calendar div.day div:last-child {
    padding-bottom: 0.5ex;
    margin-bottom: -0.5ex;
}


.agenda { display: block; }

.agenda .day.newweek {
    border-top: thick solid grey;
}
.agenda .day:not(.empty) {
    display: block; border-top: thin solid grey; width: 100%;
    padding: 0;
}
.agenda span.date.w0:before { content: "Sun "; }
.agenda span.date.w1:before { content: "Mon "; }
.agenda span.date.w2:before { content: "Tue "; }
.agenda span.date.w3:before { content: "Wed "; }
.agenda span.date.w4:before { content: "Thu "; }
.agenda span.date.w5:before { content: "Fri "; }
.agenda span.date.w6:before { content: "Sat "; }
.agenda span.date {
    font-size: 70.7%; width:7em;
    vertical-align: middle; 
    display: table-cell;
    padding: 0 0.5ex;
}
.agenda div.events { display: table-cell; vertical-align: middle; }

.assignment:before { content: "due: "; font-size: 70.7%; }
small { opacity: 0.5; }
.special, .exam { background: rgba(255,127,0,0.25); opacity: 0.75; }
span.date { font-family:monospace; }
details { padding-left: 1em; }
summary { margin-left: -1em; }

.day.past { opacity: 0.707; }
.day.today { box-shadow: 0 0 0.5ex 0.5ex grey; }
.agenda .day.today .wrapper { margin: 0.5ex 0;}

.calendar div.day.empty { background: rgba(0,0,0,0); padding: 0em; margin: 0em; border: none; border-radius: 0; min-height: 1.5em; }

</style>


<p>View 
<label><input type="checkbox" name="show" onchange="show(this)" checked value="CS2102-002"> CS2102-002</label>
<label><input type="checkbox" name="show" onchange="show(this)" checked value="CS2102-003"> CS2102-003</label>
<label><input type="checkbox" name="show" onchange="show(this)" checked value="CS2102-004"> CS2102-004</label>
</p>

<p>View as 
<label><input type="radio" name="viewmode" onchange="viewmode(this)" checked value="calendar" id="viewmode=calendar"> calendar</label>
or
<label><input type="radio" name="viewmode" onchange="viewmode(this)" value="agenda" id="viewmode=agenda"> agenda</label>;
<label><input type="checkbox" name="showpast" onclick="showPast(this)" checked id="showpast"> show past</label>;
readings can be <input type="button" value="shown" onclick="document.querySelectorAll('details').forEach(x => x.setAttribute('open','open'))"></input> or <input type="button" value="hidden" onclick="document.querySelectorAll('details').forEach(x => x.removeAttribute('open'))"></input> as a whole, or clicked on individually to toggle visibility.
</p>


{#include schedule.html}


<script src="schedule.js"></script>

To subscribe to the above calendar, add <http://www.cs.virginia.edu/luther/2102/F2020/cal.ics> to your calender application of choice.

<hr/>

At the time this note was written, the exact structure and timing of final exams had not been released. The official information about finals can be found at <https://www2.virginia.edu/registrar/exams.html#1208>
