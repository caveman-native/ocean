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
          + '</td><td>' + item["pattern.type"] +  '</td><td>' + item["pattern.status "]
          + '</td><td> <a href="/editPattern#"> Edit </a> </td>'
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

<br/>
<br/>
<br/>
<br/>
    </div>


% include('footer.tpl')