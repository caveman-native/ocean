% include('header.tpl')

<div class="row">

    <!--
    <div class="col-sm">
        #% include('nav.tpl')
    </div>
    -->

    <div class="col-10 ml-5">

    <h2>Exsiting Patterns</h2>

    <div class="table-responsive">
      <table class="table">
        <thead class="thead-dark">
          <tr>
            <th>Meta</th>
            <th>Start date</th>
            <th>Stop date</th>
            <th>Sequence</th>
            <th>Type</th>
            <th>Status</th>
            <th>Edit</th>
            <th>Delete</th>
          </tr>
        </thead>
        <tbody id="added-pattern"></tbody>
      </table>
    </div>

    <button type="button" class="btn btn-primary" id="createPattern">Create Pattern</button>

    <div id="message"></div>

    <div id="patternForm"></div>

    <div id="editForm" style="display: none;">

    <form id="patternUpdateForm" action="" method="post">

      <div class="form-group">
        <label for="inputMeta">Meta</label>
        <input type="text" name="meta" value={{meta}} class="form-control" id="meta" aria-describedby="metaHelp" placeholder="Enter meta">
        <small id="metaHelp" class="form-text text-muted">Please enter some description.</small>
      </div>

      <div class="form-group">
        <label for="inputStartDate">start_dt</label>
        <input type="date" value={{start_dt}} name="start_dt" class="form-control" id="inputStartDate" placeholder="start_dt">
      </div>

      <div class="form-group">
        <label for="inputstop_dt">stop_dt</label>
        <input type="datetime-local" name="stop_dt" value="{{stop_dt}}" class="form-control" id="inputstop_dt" placeholder="inputstop_dt">
      </div>

      <div class="form-group">
        <label for="inputsequence">sequence</label>
        <input type="number"  value={{sequence}} min="0" max="6000" name="sequence" class="form-control" id="inputsequence" placeholder="sequence">
      </div>

      <div class="form-group">
        <label for="inputType1">type</label>
        <input type="number" value={{type}} min="0" max="6000" name="type" class="form-control" id="inputType1" placeholder="type">
      </div>

      <div class="form-group">
        <label for="inputstatus">status</label>
        <input type="number" name="status" value={{status}} min="0" max="6000" class="form-control"  id="inputstatus" placeholder="status">
      </div>

      <div class="form-group">
        <label for="relatedprofiles">profiles in patterns</label>
        <textarea class="form-control" id="exampleFormControlTextarea1" rows="3">profile1, profile2, profile3</textarea>
      </div>

      <button type="submit" id="savePattern" class="btn btn-warning">Save To Pattern</button>
    </form>

  % include('footerNav.tpl')  
  </div>

</div>
<script>
$(function(){
    
  $.getJSON("/viewPatterns", function(data){
    var items = [];
    var keys = [];
    $.each(data, function(key, val){
      items.push(val);
      keys.push(key);
    });
    $("tr:has(td)").remove();
      var trows = '';
      $.each(items, function(index, item) {
        trows += '<tr><td>' + item["pattern.meta"]
        + '</td><td>' + item["pattern.start_dt"]
        + '</td><td>' + item["pattern.stop_dt"]
        + '</td> <td>' + item["pattern.sequence"]
        + '</td><td>' + item["pattern.type"]
        +  '</td><td>' + item["pattern.status"]
        + '</td><td><a id="editPattern" href="/pattern/edit/' + keys[index] + '">View/Edit</a></td>'
        + '</td><td><a id="deletePattern" href="#deletePattern" onClick="deletePattern(' + keys[index] + '); return false;">Delete</a></td></tr>';
      });
      $("#added-pattern").append(trows);
  });

});

var pathname = window.location.pathname;
  if(pathname.includes('/pattern/edit/')){
  if (document.getElementById('editForm'))
  document.getElementById("editForm").style.display = "block";
}

</script>    
% include('footer.tpl')