% include('header.tpl')

<div id="profile-patterns-container">

    <h2 class="section-title">My Patterns</h2>


	<button id="ajax-button" type="button">Make a Pattern</button>
	<div id="create-pattern"></div>
 
<script>
(function() {

	var httpRequest;
	document.getElementById("ajax-button").addEventListener('click', makeRequest());
	
	function makeRequest() {
		httpRequest = new XMLHttpRequest();
		if (!httpRequest) {
			alert('Giving up :( Cannot create an XMLHTTP instance');
			return false;
		}
		httpRequest.onreadystatechange = alertContents;
		httpRequest.open('GET', '/createPattern');
		httpRequest.send();
	}

	function alertContents() {
		if (httpRequest.readyState === XMLHttpRequest.DONE) {
			if (httpRequest.status === 200) {
				//alert(httpRequest.responseText);
				document.getElementById("create-pattern").innerHTML = httpRequest.responseText;
			} else {
				alert('There was a problem with the request.');
			}
		}
	}

	function createPattern() {
		document.getElementById("pattern-submit").addEventListener("click", function(event) {				
			event.preventDefault();
			
			// form input values
			var metaValue = document.getElementById("meta").value;
			var startDateValue = document.getElementById("start-date").value;
			var endDateValue = document.getElementById("end-dt").value;
			var typeValue = document.getElementById("type").value;
			var statusValue = document.getElementById("status").value;

			var data = new FormData();
			data.append('meta', metaValue);
			data.append('start_dt', startDateValue);
			data.append('end-dt', endDateValue);
			data.append('type', typeValue);
			data.append('status', statusValue);

			var xhr = new XMLHttpRequest();
			xhr.open('POST', '/createPattern', true);
			xhr.onload = function () {
				if (xhr.status == 200) {
					document.getElementById("create-pattern").innerHTML = httpRequest.responseText;
				} else {
					xhr.innerHTML = "Error " + xhr.status + " occurred when trying to upload your file.<br \/>";
				}
			}; 
			xhr.send(data);

			//event.preventDefault();

		}, false);
	}

})();
</script>

<!--
<table border="0">
	%if (len(profile_rows)>0):
		<thead>
			<tr>
				<th>Description</th>
				<th>Direction</th>
				<th>Update</th>
			</tr>
		</thead>
	%else:
		Nothing Here!
	%end
	%count = 0
	%for row in profile_rows:
		<tr>
			<td>{{row['description']}}</td>
			<td>{{row['direction']}}</td>
			<td><center><a href="/update/{{count}}"> update</a></center></td>
		</tr>
		%count = count + 1
	%end
</table>
-->

</div>

% include('footer.tpl')
