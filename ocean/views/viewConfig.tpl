<h2>Current properties are : </h2>

<body>
%from readCfg import readProperties
% configMap = readProperties()
    %    for key, value in configMap.iteritems():
<p> {{key}} :  {{value}}</p>
    %end

<p> <a href="/editConfig">Edit</a>  </p>

</body>