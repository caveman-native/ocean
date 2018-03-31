% include('header.tpl')
<div class="row">

    <div class="col-sm">
        % include('nav.tpl')
    </div>

    <div class="col-8">

        <div class="row">
            <h5>Profiler Mission Configuration</h4>
        </div>
        
        <div class="row">
            <p>Current Properties</p>
        </div>

        <div class="row">

            <div class="col">
                <p class="text-capitalize font-weight-bold">supervisors</p>
                <ul class="list-group">
                    % for key, value in reversed(sorted(supervisors.items())):
                    <li class="list-group-item"><span class="left">{{key}}:</span><span class="right">{{value}}</span></li><br>
                    %end
                </ul>
            </div>

            <div class="col">
                <p class="text-capitalize font-weight-bold">hosts</p>
                <ul class="list-group">
                    % for key, value in reversed(sorted(hosts.items())):
                    <li class="list-group-item"><span class="left">{{key}}:</span><span class="right">{{value}}</span></li><br>
                    %end
                </ul>
            </div>

            <div class="col">
                <p class="text-capitalize font-weight-bold">imm</p>
                <ul class="list-group">
                    % for key, value in reversed(sorted(imm.items())):
                    <li class="list-group-item"><span class="left">{{key}}:</span><span class="right">{{value}}</span></li><br>
                    %end
                </ul>
            </div>

        </div>

        <div class="row">
            <a class="btn btn-primary" href="/editConfig" role="button">Edit Current Configuration</a>
        </div>

        % include('footerNav.tpl')
    
    </div>

</div>
% include('footer.tpl')
