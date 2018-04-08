% include('header.tpl')
<div class="row">
    
    <!--
    <div class="col-sm">
        #% include('nav.tpl')
    </div>
    -->

    <div class="col-10 ml-5">

        <div class="row">
            <h5>Edit Configuration</h4>
        </div>

        <div class="row">

            <form id="edit-config-form" method="post" action="/">

                <div class="form-group">
                    <h5>Supervisors</h5><br>
                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(supervisors.items())):
                            % if key == "supervisor.gps_interval":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <input type="text" name={{key}} class="form-control form-control-sm" value="{{value}}">
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">minutes between gps fixes</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(supervisors.items())):
                            % if key == "supervisor.wake_mode":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <select class="custom-select custom-select-sm mr-sm-2" id="inlineFormCustomSelect" name={{key}} value="{{value}}">
                                <option value="1">1</option>
                                <option value="2">2</option>
                            </select>
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">1=bump from now 2=fixed interval, default=2</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(supervisors.items())):
                            % if key == "supervisor.alarm_interval":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            <input type="text" name={{key}} class="form-control form-control-sm" value="{{value}}">
                            </div>
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">wake alarm interval minutes</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(supervisors.items())):
                            % if key == "supervisor.watchdog_seconds":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            <input type="text" name={{key}} class="form-control form-control-sm" value="{{value}}">
                            </div>
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">max host on without wd kick</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(supervisors.items())):
                            % if key == "supervisor.starting_alarm_time":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <input type="text" name={{key}} class="form-control form-control-sm" value="{{value}}">
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">first alarm/base datetime</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(supervisors.items())):
                            % if key == "supervisor.emergency_isu_call_interval":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <input type="text" name={{key}} class="form-control form-control-sm" value="{{value}}">
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">emergency gps wake based count</small>
                </div>

                <div class="form-group">
                    <h5>Host</h5><br>
                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(hosts.items())):
                            % if key == "host.status_file_mode":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <select class="custom-select custom-select-sm mr-sm-2" id="inlineFormCustomSelect" name={{key}} value="{{value}}">
                                <option value="0">0</option>
                                <option value="1">1</option>
                                <option value="2">2</option>
                                <option value="3">3</option>
                            </select>
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">0-off 1-before 2-after 3-both [default: 1]</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(hosts.items())):
                            % if key == "host.max_session_time":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <input type="text" name={{key}} class="form-control form-control-sm" value="{{value}}">
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">max time host is allowed to be up for any session</small>
                </div>

                <div class="form-group">
                    <h5>IMM</h5><br>
                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(imm.items())):
                            % if key == "imm.from_remote_dir_name":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <input type="text" class="form-control form-control-sm" name={{key}} value="{{value}}">
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">directory under /data where files from surfcon go</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(imm.items())):
                            % if key == "imm.session_attempts":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <input type="text" name={{key}} class="form-control form-control-sm" value="{{value}}">
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">1-n [default: 10]</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(imm.items())):
                            % if key == "imm.listen_timeout":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <input type="text" name={{key}} class="form-control form-control-sm" value="{{value}}">
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">listening seconds</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(imm.items())):
                            % if key == "imm.max_imm_time":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <input type="text"  name={{key}} class="form-control form-control-sm" value="{{value}}">
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">max imm transfer time in seconds</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(hosts.items())):
                            % if key == "host.max_session_time":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <input type="text" name={{key}} class="form-control form-control-sm" value="{{value}}">
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">max time host is allowed to be up for any session</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(imm.items())):
                            % if key == "imm.verbose":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <select class="custom-select custom-select-sm mr-sm-2" id="inlineFormCustomSelect" name={{key}} value="{{value}}">
                                <option value="0">0</option>
                                <option value="1">1</option>
                            </select>
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">0-off 1-on [default: 0]</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(imm.items())):
                            % if key == "imm.send_syslog":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <input type="text" name={{key}} class="form-control form-control-sm" value="{{value}}">
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">Send yesterdays syslog [default: 0]</small>

                    <div class="input-group input-group-sm mb-1">
                        % for key, value in reversed(sorted(imm.items())):
                            % if key == "imm.max_fput_count":
                            <div class="input-group-prepend">
                                <span class="input-group-text">{{key}}</span>
                            </div>
                            <input type="text" name={{key}} class="form-control form-control-sm" value="{{value}}">
                            % end
                        % end
                    </div>
                    <small class="form-text text-muted">max fput list entries</small>
                </div>

            <button type="submit" class="btn btn-primary submit-btn">Save</button>
            </form>

        </div>

    % include('footerNav.tpl')    
    </div>

</div>
% include('footer.tpl')