<!DOCTYPE html>
<html>
<header>
      <title>View configuration</title>
      <style>
        body {background-color: powderblue;}
        h1   {color: blue;}
        p    {color: red;}
        ul   { padding-left: 5px;}
        li {
        padding: 3 3 3 3;
}

</style>
</header>    
    
<body>

<body>

% include('mission.tpl')

<h2>Current supervisors properties are : </h2>    
    

    %    for key, value in reversed(sorted(supervisors.items())):
<p> {{key}} :  {{value}}</p>
    %end
	

<h2>Current host properties are : </h2>    
    
    %    for key, value in reversed(sorted(hosts.items())):
<p> {{key}} :  {{value}}</p>
    %end

<h2>Current imm properties are : </h2>    
    

    %    for key, value in reversed(sorted(imm.items())):
<p> {{key}} :  {{value}}</p>
    %end

<p> <a href="/editConfig">Edit</a>  </p>

</body>
% include('footer.tpl')

</head>