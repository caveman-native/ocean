% include('header.tpl')
<script>

(function() {


$.getJSON( "/viewPatterns", function( data ) {
  var items = [];
  var keys = [];
  $.each( data, function( key, val ) {
    items.push( val  );
    keys.push( key );
  });
 $("tr:has(td)").remove();

   var trows = '';
    $.each(items, function(index, item) {
        trows += '<tr><td>' + item["pattern.meta"] + '</td><td>' + item["pattern.start_dt"]
          + '</td><td>' + item["pattern.stop_dt"] + '</td> <td>' + item["pattern.sequence"]
          + '</td><td>' + item["pattern.type"] +  '</td><td>' + item["pattern.status"]
          + '</td><td> <a id="editPattern" href="/pattern/edit/' + keys[index] + '"> Edit </a> </td>'
          + '</td><td> <a id="deletePattern" href="#deletePattern" onClick="deletePattern(' + keys[index] + '); return false;"> Delete </a> </td> </tr>';

    });

    $("#added-pattern").append(trows);

});




})();
</script>

<div class="row">

    <div class="col-sm">
        % include('nav.tpl')
    </div>

    <div class="col-8">

  <h2>Exsiting Patterns</h2>

  <div class="table-responsive">
  <table class="table" >
    <thead>
      <tr>
        <th>Meta</th>
        <th> Start date</th>
        <th> Stop date </th>
        <th> Sequence </th>
        <th> Type</th>
        <th> Status </th>
        <th> Edit </th>
        <th> Delete </th>

      </tr>
    </thead>
    <tbody id="added-pattern">
    </tbody>
  </table>
  </div>

 <br/> <br/>
 <button type="button" class="btn btn-primary" id="createPattern" > Create Pattern </button>

<div id="message">

</div>



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
    <input type="date" value={{stop_dt}} name="stop_dt" class="form-control" id="inputstop_dt" placeholder="inputstop_dt">
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
   <button type="submit" id="savePattern" class="btn btn-warning"> Submit </button>
 </form>
 </div>



<br/>
<br/>
<br/>
<br/>
    </div>

<script>
   var pathname = window.location.pathname;
   if(pathname.includes('/pattern/edit/')){
   if (document.getElementById('editForm'))
   document.getElementById("editForm").style.display = "block";
}
</script>
% include('footer.tpl')