% include('header.tpl')

<div id="profiler-editconfig-container">

    <h2 class="section-title">Profiler Mission Configuration</h2>

    <form id="edit-config-form" method="post" action="/">

        <div class="option-container-super">
            <legend>Supervisor Options</legend>            
            <ul>                  
                % for key, value in reversed(sorted(supervisors.items())):
                <li>
                    % if key == "supervisor.wake_mode":
                        <label>Wake Mode:</label>
                        <select  name={{key}}>
                            <option value="1"></option> 
                            <option value="2" selected>{{value}}</option>
                        </select>
                    % else:
                        <label>{{key}}:</label><br> <input class="" name={{key}} value={{value}} />
                    % end
                % end  
                </li>                       
            </ul>
        </div> 
        
        <div class="option-container-imm">
            <legend>IMM Options</legend>
            <ul>                  
                % for key, value in reversed(sorted(imm.items())):
                <li>
                    <label>{{key}}:</label><br> <input class="" name={{key}} value={{value}} />                        
                % end  
                </li>                       
            </ul>
        </div>        
        
        <div class="option-container-hosts">
            <legend>Hosts Options</legend>
            <ul>                  
                % for key, value in reversed(sorted(hosts.items())):
                <li>
                    <label>{{key}}:</label><br> <input class="" name={{key}} value={{value}} />    
                % end  
                </li>                       
            </ul>
        </div>        
            
        <div class="submit-btn-container">
            <input class="submit-btn" type='submit' value='Edit Properties'>
        </div>

    </form>

</div>

% include('footer.tpl')
