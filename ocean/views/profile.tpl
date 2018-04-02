% include('header.tpl')
<script>

(function() {


$.getJSON( "/viewProfiles", function( data ) {
  var items = [];
  $.each( data, function( key, val ) {
    items.push( val  );
  });
 $("tr:has(td)").remove();

   var trows = '';
    $.each(items, function(index, item) {
        trows += '<tr><td>' + item["profile.meta"] + '</td><td>' + item["profile.type"]
          + '</td><td>' + item["profile.direction"] + '</td> <td>' + item["profile.interval"]
          + '</td><td>' + item["profile.stopCheck"] +  '</td><td>' + item["profile.shallowWindow"]
          + '</td><td>' + item["profile.stallTimeout"] + '</td> '
          + '</td><td> <a href="/editProfile#"> Edit </a> </td>'
          + '</td><td> <a href="/deleteProfile#"> Delete </a> </td> </tr>';

    });

    $("#added-profiles").append(trows);

});



$('#createProfile').on('click', function(event) {
   alert('clicked');
  event.preventDefault();  // To prevent following the link (optional)

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

<br/>
<br/>
<br/>
<br/>
    </div>


% include('footer.tpl')