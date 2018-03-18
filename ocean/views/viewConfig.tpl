% include('header.tpl')

<div id="profiler-viewconfig-container">

    <h2 class="section-title">Profiler Mission Configuration</h2>
    <h3 class="view-title">Current Properties</h3>

    <div class="current-property-list">

        <ul>
            % for key, value in reversed(sorted(supervisors.items())):
            <li><span class="left">{{key}}:</span><span class="right">{{value}}</span></li><br>
            %end
        </ul>

        <ul>
            % for key, value in reversed(sorted(hosts.items())):
            <li><span class="left">{{key}}:</span><span class="right">{{value}}</span></li><br>
            %end
        </ul>

        <ul>
            % for key, value in reversed(sorted(imm.items())):
            <li><span class="left">{{key}}:</span><span class="right">{{value}}</span></li><br>
            %end
        </ul>

    </div>

    <div class="edit-btn-bottom">
            <a href="/editConfig">Edit Current Configuration</a>
    </div>

</div>

% include('footer.tpl')