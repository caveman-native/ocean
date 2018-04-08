% include('header.tpl')
<div class="row">

    <!--
    <div class="col-sm">
        #% include('nav.tpl')
    </div>
    -->

    <div class="col-10 ml-5">

    <h2>Exsiting Profiles</h2>

    <div class="table-responsive">
      <table class="table table-sm">
        <thead class="thead-dark">
          <tr>
            <th>Meta</th>
            <th>Type</th>
            <th>Direction</th>
            <th>Interval</th>
            <th>Stop Check</th>
            <th>Shallow Window</th>
            <th>Stall Timeout</th>
            <th>Edit</th>
            <th>Delete</th>
            <th>Add to Pattern</th>
            <th><button type="button" class="btn btn-primary" id="create-profile">Create Profile</button></th>
          </tr>
        </thead>
        <tbody id="added-profiles"></tbody>
      </table>
    </div>

    <div id="message"></div>

    <div id="profile-form"></div>

    <div id="edit-form" style="display: none;">

    <form id="profile-update-form" action="" method="post">

      <div class="row">

        <div class="col-sm">
            <div class="form-group">
              <label for="inputMeta">meta</label>
              <input type="text" name="meta" value="{{meta}}" class="form-control form-control-sm" id="inputMeta" aria-describedby="metaHelp" placeholder="Enter Meta">
              <small id="metaHelp" class="form-text text-muted">Please enter a profile name.</small>
            </div>
      
            <div class="form-group">
              <label for="inputType1">type</label>
              <input type="number" name="type" value="{{type}}" class="form-control form-control-sm" id="inputType1" placeholder="Type">
            </div>
            
            <div class="form-group">
              <label for="inputDirection">direction</label>
              <input type="number" min="0" value="{{direction}}" name="direction" max="1" class="form-control form-control-sm" id="inputDirection" placeholder="Direction">
            </div>
            
            <div class="form-group">
              <label for="inputinterval">interval</label>
              <input type="number" min="0" max="6000" value="{{interval}}" name="interval" class="form-control form-control-sm" id="inputinterval" placeholder="Interval">
            </div>
            
            <div class="form-group">
              <label for="inputmax_time">max_time</label>
              <input type="number" min="0" max="6000"  value="{{maxTime}}" name="max_time" class="form-control form-control-sm" id="inputmax_time" placeholder="max_time">
            </div>
        </div>

        <div class="col-sm">
          <div class="form-group">
              <label for="inputType1">deep_depth</label>
              <input type="number" min="0" max="6000" value="{{deepDepth}}" name="deep_depth" class="form-control form-control-sm" id="inputdeep_depth" placeholder="deep_depth">
            </div>
      
            <div class="form-group">
              <label for="inputdeep_window">deep_window</label>
              <input type="number" min="0" max="6000" value="{{deepWindow}}" class="form-control form-control-sm" name="deep_window" id="inputdeep_window" placeholder="deep_window">
            </div>
      
            <div class="form-group">
              <label for="inputshallow_depth">shallow_depth</label>
              <input type="number" min="0" max="6000" value="{{shallowDepth}}" class="form-control form-control-sm" id="inputshallow_depth" name="shallow_depth"  placeholder="shallow_depth">
            </div>
      
            <div class="form-group">
              <label for="inputshallow_window">shallow_window</label>
              <input type="number" min="0" max="6000" value="{{shallowWindow}}" class="form-control form-control-sm" id="inputshallow_window" name="shallow_window" placeholder="shallow_window">
            </div>
      
            <div class="form-group">
              <label for="inputstall_timeout">stall_timeout</label>
              <input type="number" min="0" value="{{stallTimeout}}" max="6000" class="form-control form-control-sm" id="inputstall_timeout"  name="stall_timeout" placeholder="stall_timeout">
            </div>
        </div>

        <div class="col-sm">
          <div class="form-group">
              <label for="inputramp_time">ramp_time</label>
              <input type="number" min="0" value="{{rampTime}}" max="6000" class="form-control form-control-sm" name="inputramp_time" id="inputramp_time" placeholder="ramp_time">
            </div>
      
            <div class="form-group">
              <label for="inputstop_check">stop_check</label>
              <input type="number" min="0" value="{{stopCheck}}" max="6000" class="form-control form-control-sm" name="stop_check" id="inputstop_check"  placeholder="stop_check">
            </div>
      
            <div class="form-group">
              <label for="inputType1">backtrack_time</label>
              <input type="number" value="{{backtrackTimes}}" min="0" max="6000" class="form-control form-control-sm" name="backtrack_time" id="inputbacktrack_time" placeholder="backtrack_time">
            </div>
      
            <div class="form-group">
              <label for="inputbacktrack_count">backtrack_count</label>
              <input type="number" min="0" value="{{backtrackCount}}" max="6000" class="form-control form-control-sm" name="backtrack_count" id="inputbacktrack_count" placeholder="backtrack_count">
            </div>
      
            <div class="form-group">
              <label for="inputctd_warmup_time">ctd_warmup_time</label>
              <input type="number" min="0" value="{{ctdWrapupTime}}" max="6000" name="ctd_warmup_time" class="form-control form-control-sm" id="inputctd_warmup_time" placeholder="ctd_warmup_time">
            </div>
      
            <div class="form-group">
              <label for="inputdpdt_threshold">dpdt_threshold</label>
              <input type="number" min="0" value="{{dpdt}}" max="6000" name="dpdt_threshold" class="form-control form-control-sm" id="inputdpdt_threshold" placeholder="dpdt_threshold">
            </div>
        </div>

      </div>

    <button type="submit" id="create-profile" class="btn btn-warning">Save Profile</button>
    </form>

  % include('footerNav.tpl')
  </div>

</div>
<script>
$(function(){ 
  
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
            trows += '<tr><td>' + item["profile.meta"]
            + '</td><td>' + item["profile.type"]
            + '</td><td>' + item["profile.direction"]
            + '</td> <td>' + item["profile.interval"]
            + '</td><td>' + item["profile.stopCheck"]
            +  '</td><td>' + item["profile.shallowWindow"]
            + '</td><td>' + item["profile.stallTimeout"]
            + '</td>'
            + '</td><td><a id="edit-profile" href="/profile/edit/' + keys[index] + '">View/Edit</a></td>'
              + '</td><td><a id="delete-profile" href="#delete-profile" onClick="deleteProfile(' + keys[index] + '); return false;">Delete</a></td>'
            + '</td><td><select class="custom-select custom-select-sm mr-sm-2" id="inlineFormCustomSelect" name="Add to Pattern" value="">'
            + '<option value="1">1</option>'
            + '</select>'
            + '</td><td><button type="submit" id="add-to-pattern" class="btn btn-warning">Add To Pattern</button>'
            +  '</tr>';
        });
        $("#added-profiles").append(trows);
    });
  
});

var pathname = window.location.pathname;
if(pathname.includes('/profile/edit/')){
    if (document.getElementById('edit-form'))
    document.getElementById("edit-form").style.display = "block";
}

</script>
% include('footer.tpl')