% include('header.tpl')
<script>

(function() {


$.getJSON( "/viewProfiles", function( data ) {
  var items = [];
  var keys = [];
  $.each( data, function( key, val ) {
    items.push( val  );
    keys.push( key );
  });
 $("tr:has(td)").remove();

   var trows = '';
    $.each(items, function(index, item) {
        trows += '<tr><td>' + item["profile.meta"] + '</td><td>' + item["profile.type"]
          + '</td><td>' + item["profile.direction"] + '</td> <td>' + item["profile.interval"]
          + '</td><td>' + item["profile.stopCheck"] +  '</td><td>' + item["profile.shallowWindow"]
          + '</td><td>' + item["profile.stallTimeout"] + '</td> '
          + '</td><td> <a id="editProfile" href="/profile/edit/' + keys[index] + '"> Edit </a> </td>'
          + '</td><td> <a id="deleteProfile" href="#deleteProfile" onClick="deleteProfile(' + keys[index] + '); return false;"> Delete </a> </td> </tr>';

    });

    $("#added-profiles").append(trows);

});




})();
</script>

<div class="row">

    <div class="col-sm">
        % include('nav.tpl')
    </div>

    <div class="col-8">

  <h2>Exsiting Profiles</h2>

  <div class="table-responsive">
  <table class="table" >
    <thead>
      <tr>
        <th>Meta</th>
        <th>Type</th>
        <th>DIRECTION</th>
        <th>INTERVAL</th>
        <th>STOP CHECK </th>
        <th>Shallow Window</th>
        <th>Stall Timeout </th>
        <th> Edit </th>
        <th> Delete </th>

      </tr>
    </thead>
    <tbody id="added-profiles">
    </tbody>
  </table>
  </div>

 <br/> <br/>
 <button type="button" class="btn btn-primary" id="createProfile" > Create Profile </button>

<div id="message">

</div>



<div id="profileForm"></div>



<div id="editForm" style="display: none;">
  <form id="profileUpdateForm" action="" method="post">

    <div class="form-group">
    <label for="inputMeta">Meta</label>
    <input type="text" name="meta" value="{{meta}}" class="form-control" id="inputMeta" aria-describedby="metaHelp" placeholder="Enter meta">
    <small id="metaHelp" class="form-text text-muted">Please enter some description.</small>
   </div>
   <div class="form-group">
     <label for="inputType1">Type</label>
    <input type="number" name="type" value="{{type}}" class="form-control" id="inputType1" placeholder="Type">
   </div>
    <div class="form-group">
    <label for="inputDirection">Direction</label>
    <input type="number" min="0" value="{{direction}}" name="direction" max="1" class="form-control" id="inputDirection" placeholder="Direction">
   </div>
    <div class="form-group">
    <label for="inputinterval">interval</label>
    <input type="number" min="0" max="6000" value="{{interval}}" name="interval" class="form-control" id="inputinterval" placeholder="interval">
  </div>'
      <div class="form-group">
    <label for="inputmax_time">max_time</label>
    <input type="number" min="0" max="6000"  value="{{maxTime}}" name="max_time" class="form-control" id="inputmax_time" placeholder="max_time">
  </div>
    <div class="form-group">
    <label for="inputType1">deep_depth</label>
    <input type="number" min="0" max="6000" value="{{deepDepth}}" name="deep_depth" class="form-control" id="inputdeep_depth" placeholder="deep_depth">
  </div>

    <div class="form-group">
    <label for="inputdeep_window">deep_window</label>
    <input type="number" min="0" max="6000" value="{{deepWindow}}" class="form-control" name="deep_window" id="inputdeep_window" placeholder="deep_window">
  </div>

    <div class="form-group">
    <label for="inputshallow_depth">shallow_depth</label>
    <input type="number" min="0" max="6000" value="{{shallowDepth}}" class="form-control" id="inputshallow_depth" name="shallow_depth"  placeholder="shallow_depth">
  </div>

    <div class="form-group">
    <label for="inputshallow_window">shallow_window</label>
    <input type="number" min="0" max="6000" value="{{shallowWindow}}" class="form-control" id="inputshallow_window" name="shallow_window" placeholder="shallow_window">
  </div>

    <div class="form-group">
    <label for="inputstall_timeout">stall_timeout</label>
    <input type="number" min="0" value="{{stallTimeout}}" max="6000" class="form-control" id="inputstall_timeout"  name="stall_timeout" placeholder="stall_timeout">
  </div>

    <div class="form-group">
    <label for="inputramp_time">ramp_time</label>
    <input type="number" min="0" value="{{rampTime}}" max="6000" class="form-control" name="inputramp_time" id="inputramp_time" placeholder="ramp_time">
  </div>

    <div class="form-group">
    <label for="inputstop_check">stop_check</label>
    <input type="number" min="0" value="{{stopCheck}}" max="6000" class="form-control" name="stop_check" id="inputstop_check"  placeholder="stop_check">
  </div>

     <div class="form-group">
      <label for="inputType1">backtrack_time</label>
      <input type="number" value="{{backtrackTimes}}" min="0" max="6000" class="form-control" name="backtrack_time" id="inputbacktrack_time" placeholder="backtrack_time">
    </div>

    <div class="form-group">
        <label for="inputbacktrack_count">backtrack_count</label>
        <input type="number" min="0" value="{{backtrackCount}}" max="6000" class="form-control" name="backtrack_count" id="inputbacktrack_count" placeholder="backtrack_count">
   </div>

    <div class="form-group">
    <label for="inputctd_warmup_time">ctd_warmup_time</label>
    <input type="number" min="0" value="{{ctdWrapupTime}}" max="6000" name="ctd_warmup_time" class="form-control" id="inputctd_warmup_time" placeholder="ctd_warmup_time">
   </div>

   <div class="form-group">
    <label for="inputdpdt_threshold">dpdt_threshold</label>
    <input type="number" min="0" value="{{dpdt}}" max="6000" name="dpdt_threshold" class="form-control" id="inputdpdt_threshold" placeholder="dpdt_threshold">
  </div>

   <button type="submit" id="saveProfile" class="btn btn-warning"> Submit </button>
</form>
</div>


<br/>
<br/>
<br/>
<br/>
    </div>


<script>
   var pathname = window.location.pathname;
   if(pathname.includes('/profile/edit/')){
   if (document.getElementById('editForm'))
   document.getElementById("editForm").style.display = "block";
}


</script>

% include('footer.tpl')