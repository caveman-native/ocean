<html>
<body>
<!-- TEMPLATE BELOW
–––––––––––––––––––––––––––––––––––––––––––––––––– -->

<hr/>
<h5><font color=#33C3F0>Profile list</font></h5>
<hr/>
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
	<td>{{row['description']}}</td><td>{{row['direction']}}</td><td><center><a href="/update/{{count}}"> update</a></center></td>
	</tr>
	%count = count + 1
%end
</table>
<hr/>


</body>

</html>