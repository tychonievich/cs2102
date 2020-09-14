---
title: Video Player
...

<div id="playhere">Missing video name</div>

Playback speed: <input type="text" id="speed" value="1.0" oninput="respeed()"/>

<a href="" id="download"></a>

<script type="text/javascript">
function loadVid() {
    var vid = location.hash.replace('#','lectures/')
    if (vid) {
        document.getElementById('playhere').innerHTML = '<video src="'+vid+'" controls style="max-width:100%">'
        document.getElementById('download').innerHTML = 'download '+vid.replace(/.*\//g, '')
        document.getElementById('download').href = vid
    }
}
loadVid();

function respeed() {
    let vid = document.querySelector('video')
    if (vid) vid.playbackRate = document.querySelector('#speed').value
}
</script>
