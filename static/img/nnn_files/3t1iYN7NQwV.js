if (self.CavalryLogger) { CavalryLogger.start_js(["6qJoc"]); }

__d("ChatSidebarSections",[],(function a(b,c,d,e,f,g){f.exports={ADMINED_PAGES:"admined_pages",MORE_ONLINE_FRIENDS:"more_online_friends",MORE_ONLINE_COWORKERS:"more_online_coworkers",OFFLINE_USERS:"offline_users",ORDERED_LIST:"ordered_list",ORDERED_COWORKERS:"ordered_coworkers",TYPEAHEAD:"typeahead",NOW_PINNED_LIST:"now_pinned_list",NEARBY:"nearby",WORKPLACE_OTHERS:"workplace_others"};}),null);
__d("MercuryTypeaheadConstants",[],(function a(b,c,d,e,f,g){f.exports={COMPOSER_FRIENDS_MAX:4,COMPOSER_FB4C_MAX:4,COMPOSER_NON_FRIENDS_MAX:2,COMPOSER_MESSENGER_ONLY_CONTACT_MAX:4,COMPOSER_SHOW_MORE_LIMIT:2,COMPOSER_THREADS_INITIAL_LIMIT:2,COMPOSER_CHATTAB_MAX:5,COMPOSER_PAGES_MAX:5,COMPOSER_WM_MAX:19,USER_TYPE:"user",PAGE_TYPE:"page",THREAD_TYPE:"thread",HEADER_TYPE:"header",SEARCH_TYPE:"search",FRIEND_TYPE:"friend",NON_FRIEND_TYPE:"non_friend",FB4C_TYPE:"fb4c",MEETING_ROOM_PAGE_TYPE:"meeting_room_page",COMMERCE_PAGE_TYPE:"commerce_page",INTERNAL_BOT_PAGE_TYPE:"internal_bot_page",GAME_TYPE:"game",WORKPLACE_BOT_CATEGORY_TYPE:"WORKPLACE_BOT",VALID_EMAIL:"^([A-Z0-9._\u0025+-]+\u0040((?!facebook\\.com))[A-Z0-9.-]+\\.[A-Z]{2,4}|(([A-Z._\u0025+-]+[A-Z0-9._\u0025+-]*)|([A-Z0-9._\u0025+-]+[A-Z._\u0025+-]+[A-Z0-9._\u0025+-]*))\u0040(?:facebook\\.com))$"};}),null);
__d("PagesLikeFollowNotifActions",[],(function a(b,c,d,e,f,g){f.exports={INIT_DATA:"init_data",LIKE:"like",UNLIKE:"unlike",FOLLOW_CHANGED:"follow_changed",NOTIF_CHANGE:"notif_change",NOTIF_ALL_ON:"notif_all_on",NOTIF_ALL_OFF:"notif_all_off",NEWS_FEED_CHANGE:"news_feed_change"};}),null);
__d("PagesLoggerEventEnum",[],(function a(b,c,d,e,f,g){f.exports={CLICK:"click",CREATE:"create",DELETE:"delete",DRAG:"drag",HOVER:"hover",IMPRESSION:"impression",RECEIVE_REQUEST:"receive_request",RECEIVE_RESPONSE:"receive_response",SCROLL:"scroll",SEND_REQUEST:"send_request",SEND_RESPONSE:"send_response",UPDATE:"update"};}),null);
__d("PagesLoggerEventTargetEnum",[],(function a(b,c,d,e,f,g){f.exports={ABOUT_TAB:"about_tab",ADMIN_TAB:"admin_tab",ADS_CTA:"ads_cta",CONFIRM_APPLY_PAGE_TEMPLATE_BUTTON:"confirm_apply_page_template_button",EDIT_PAGE_TEMPLATE_ROW:"edit_page_template_row",FAN_INVITE_EMAIL:"fan_invite_email",FEED_CTA:"feed_cta",FEED_PAGE_ATTACHMENT:"feed_page_attachment",FEED_PAGE_COMMENT_ATTACHMENT:"feed_page_comment_attachment",FOLLOW_UP_MESSAGE:"follow_up_message",MESSAGE_FANTA_TAB_CLOSE:"message_fanta_tab_close",MESSENGER_ABOUT_BUTTON:"messenger_about_button",MESSENGER_ATTACHMENT:"messenger_attachment",MESSENGER_URL_BUTTON:"messenger_url_button",MSITE_MESSAGE_BUBBLE:"msite_message_bubble",NEW_ACTION_PROMOTION:"new_action_promotion",PAGE_COVER_CTA_BUTTON:"page_cover_cta_button",PAGE_COVER_DESCRIPTION:"page_cover_description",PAGE_GET_DIRECTIONS:"page_get_directions",PAGE_HOME_CARD:"page_home_card",PAGE_MAP:"page_map",PAGE_MENU:"page_menu",PAGE_MESSAGE:"page_message",PAGE_NOTES_CARD:"page_notes_card",PAGE_NOTES_TAB:"page_notes_tab",PAGE_PHONE:"page_phone",PAGE_PROFILE:"page_profile",PAGE_REQUEST_TIME_BOOST:"page_request_time_boost",PAGE_SAVE:"page_save",PAGE_SETTINGS:"page_settings",PAGE_TAB_BAR:"page_tab_bar",PAGE_TEMPLATE:"page_template",PAGE_TEMPLATE_ALARM_CLOCK:"page_template_alarm_clock",PAGE_TEMPLATE_NUX_TOUR:"page_template_nux_tour",PAGE_VENUE_EVENT_ABOUT:"page_venue_event_about",PAGE_WEBSITE:"page_website",PAGES_COVER_VIDEO:"pages_cover_video",PAGES_PRIMARY_CTA_BUTTON:"pages_primary_cta_button",PMA_TAB:"pma_tab"};}),null);
__d('ChatTypeaheadConstants',[],(function a(b,c,d,e,f,g){var h={USER_TYPE:'user',THREAD_TYPE:'thread',FRIEND_TYPE:'friend',NON_FRIEND_TYPE:'non_friend',FB4C_TYPE:'fb4c',PAGE_TYPE:'page',MEETING_ROOM_PAGE_TYPE:'meeting_room_page',COMMERCE_PAGE_TYPE:'commerce_page',HEADER_TYPE:'header',INTERNAL_BOT_PAGE_TYPE:'internal_bot_page',GAME_TYPE:'game'};f.exports=h;}),null);
__d('PagesTypedLogger',['Banzai','GeneratedLoggerUtils','nullthrows'],(function a(b,c,d,e,f,g){'use strict';function h(){this.clear();}h.prototype.log=function(){c('GeneratedLoggerUtils').log('logger:PagesLoggerConfig',this.$PagesTypedLogger1,c('Banzai').BASIC);};h.prototype.logVital=function(){c('GeneratedLoggerUtils').log('logger:PagesLoggerConfig',this.$PagesTypedLogger1,c('Banzai').VITAL);};h.prototype.clear=function(){this.$PagesTypedLogger1={};return this;};h.prototype.updateData=function(j){this.$PagesTypedLogger1=babelHelpers['extends']({},this.$PagesTypedLogger1,j);return this;};h.prototype.setConnectionClass=function(j){this.$PagesTypedLogger1.connection_class=j;return this;};h.prototype.setEvent=function(j){this.$PagesTypedLogger1.event=j;return this;};h.prototype.setEventLocation=function(j){this.$PagesTypedLogger1.event_location=j;return this;};h.prototype.setEventTarget=function(j){this.$PagesTypedLogger1.event_target=j;return this;};h.prototype.setLogSource=function(j){this.$PagesTypedLogger1.log_source=j;return this;};h.prototype.setPageID=function(j){this.$PagesTypedLogger1.page_id=j;return this;};h.prototype.setSessionid=function(j){this.$PagesTypedLogger1.sessionid=j;return this;};h.prototype.setTags=function(j){this.$PagesTypedLogger1.tags=c('GeneratedLoggerUtils').serializeVector(j);return this;};h.prototype.updateExtraData=function(j){j=c('nullthrows')(c('GeneratedLoggerUtils').serializeMap(j));c('GeneratedLoggerUtils').checkExtraDataFieldNames(j,i);this.$PagesTypedLogger1=babelHelpers['extends']({},this.$PagesTypedLogger1,j);return this;};h.prototype.addToExtraData=function(j,k){var l={};l[j]=k;return this.updateExtraData(l);};var i={connection_class:true,event:true,event_location:true,event_target:true,log_source:true,page_id:true,sessionid:true,tags:true};f.exports=h;}),null);
__d('PagesLogger',['PagesLoggerEventEnum','PagesTypedLogger'],(function a(b,c,d,e,f,g){var h='extra_data_',i={log:function j(k,event,l){var m=arguments.length<=3||arguments[3]===undefined?null:arguments[3],n=arguments.length<=4||arguments[4]===undefined?[]:arguments[4],o=arguments.length<=5||arguments[5]===undefined?{}:arguments[5];Object.keys(o).forEach(function(p){var q=o[p];if(q instanceof Array||q instanceof Object)q=JSON.stringify(q);o[h+p]=q;delete o[p];});new (c('PagesTypedLogger'))().setPageID(k).setEvent(event).setEventTarget(l).setEventLocation(m).setLogSource('pages_logger').setTags(n).updateExtraData(o).log();},registerLogOnClick:function j(k,l,m){var n=arguments.length<=3||arguments[3]===undefined?null:arguments[3],o=arguments.length<=4||arguments[4]===undefined?[]:arguments[4],p=arguments.length<=5||arguments[5]===undefined?{}:arguments[5];k.addEventListener('click',function(){this.log(l,c('PagesLoggerEventEnum').CLICK,m,n,o,p);}.bind(this));}};f.exports=i;}),null);
__d('ChatOpenTabEventLogger',['Banzai','ChatImpressionLogger','ChatTypeaheadConstants','MercuryIDs','MercuryParticipantTypes','PagesLogger','PagesLoggerEventEnum','PagesLoggerEventTargetEnum'],(function a(b,c,d,e,f,g){'use strict';var h='messaging_tracking',i={log:function j(k,l,m,n){var o={referrer:k||'',message_thread_id:l,message_view:'chat',timestamp_send:Date.now(),message_target_ids:[]};if(m!==undefined)o.message_target_ids=[m];c('ChatImpressionLogger').logImpression(k,m,n);c('Banzai').post(h,o,{delay:0,retry:true});if(k==='pages_manager_user_message_prompt')return;var p=c('MercuryIDs').getUserIDFromThreadID(String(l));c('Banzai').post('page_message_button_click',{page_id:p,ref:k});},logUser:function j(k,l,m){var n=c('MercuryIDs').getThreadIDFromUserID(l);this.log(k,n,l,m);},logPage:function j(k,l){this.logUser(k,l);this._pagesLogger(k,l);},logByType:function j(k,l,m){if(k===c('ChatTypeaheadConstants').THREAD_TYPE){this.log(l,m);}else if(k===c('ChatTypeaheadConstants').MEETING_ROOM_PAGE_TYPE){var n=c('MercuryIDs').getUserIDFromThreadID(m);this.log(l,m,n);}else if(!k||k===c('MercuryParticipantTypes').FRIEND||k===c('ChatTypeaheadConstants').FRIEND_TYPE||k===c('ChatTypeaheadConstants').PAGE_TYPE||k===c('ChatTypeaheadConstants').USER_TYPE){var o=void 0;if(c('MercuryIDs').isValidThreadID(m))o=c('MercuryIDs').getUserIDFromThreadID(m);this.log(l,m,o);if(k===c('ChatTypeaheadConstants').PAGE_TYPE)this._pagesLogger(l,m);}else this.log(l,m);},_pagesLogger:function j(k,l){if(k==='pages_manager_user_message_prompt')return;c('PagesLogger').log(l,c('PagesLoggerEventEnum').CLICK,c('PagesLoggerEventTargetEnum').PAGE_MESSAGE,k);}};f.exports=i;}),null);
__d('FBRTCStore',['FBRTCDispatcher','FluxStore'],(function a(b,c,d,e,f,g){'use strict';var h,i;h=babelHelpers.inherits(j,c('FluxStore'));i=h&&h.prototype;function j(){i.constructor.call(this,c('FBRTCDispatcher'));}j.prototype.__emitChange=function(){this.__emitter.emit(this.__changeEvent);};f.exports=j;}),null);
__d('VideoCallTypedLogger',['Banzai','GeneratedLoggerUtils','nullthrows'],(function a(b,c,d,e,f,g){'use strict';function h(){this.clear();}h.prototype.log=function(){c('GeneratedLoggerUtils').log('logger:VideoCallLoggerConfig',this.$VideoCallTypedLogger1,c('Banzai').BASIC);};h.prototype.logVital=function(){c('GeneratedLoggerUtils').log('logger:VideoCallLoggerConfig',this.$VideoCallTypedLogger1,c('Banzai').VITAL);};h.prototype.clear=function(){this.$VideoCallTypedLogger1={};return this;};h.prototype.updateData=function(j){this.$VideoCallTypedLogger1=babelHelpers['extends']({},this.$VideoCallTypedLogger1,j);return this;};h.prototype.setEvent=function(j){this.$VideoCallTypedLogger1.event=j;return this;};h.prototype.setMessage=function(j){this.$VideoCallTypedLogger1.message=j;return this;};var i={event:true,message:true};f.exports=h;}),null);
__d('FBRTCCallBlockingStore',['Arbiter','AsyncRequest','ChannelConstants','FBRTCDispatcher','FBRTCStore','VideoCallTypedLogger','setTimeoutAcrossTransitions'],(function a(b,c,d,e,f,g){'use strict';var h,i,j=false,k=0,l=null,m='call_block_setting_changed';h=babelHelpers.inherits(n,c('FBRTCStore'));i=h&&h.prototype;n.prototype.init=function(o){this.$FBRTCCallBlockingStore1(o);c('Arbiter').subscribe(c('ChannelConstants').getArbiterType('videocall_block_setting'),this.$FBRTCCallBlockingStore2.bind(this));};n.prototype.__onDispatch=function(o){if(o.type!==m)return;this.$FBRTCCallBlockingStore1(o.data);};n.prototype.$FBRTCCallBlockingStore1=function(o){switch(o){case 0:j=false;this.$FBRTCCallBlockingStore3();break;case -1:j=true;this.$FBRTCCallBlockingStore3();break;default:j=true;this.$FBRTCCallBlockingStore4(o);}this.__emitChange();};n.prototype.$FBRTCCallBlockingStore4=function(o){if(l===null)l=c('setTimeoutAcrossTransitions')(this.turnOnVideoCalling.bind(this),o*1000);};n.prototype.getBlockingStatus=function(){return j;};n.prototype.turnOnVideoCalling=function(){new (c('AsyncRequest'))('/ajax/chat/settings.php').setHandler(this.$FBRTCCallBlockingStore5.bind(this)).setData({call_blocked_until:0}).send();};n.prototype.turnOffVideoCalling=function(o){k=o;new (c('AsyncRequest'))('/ajax/chat/settings.php').setHandler(this.$FBRTCCallBlockingStore6.bind(this)).setData({call_blocked_until:o}).send();};n.prototype.$FBRTCCallBlockingStore3=function(){if(l){clearTimeout(l);l=null;}};n.prototype.$FBRTCCallBlockingStore5=function(){c('FBRTCDispatcher').dispatch({type:m,data:0});new (c('VideoCallTypedLogger'))().setEvent(m).setMessage('enable').log();};n.prototype.$FBRTCCallBlockingStore6=function(){c('FBRTCDispatcher').dispatch({type:m,data:k});new (c('VideoCallTypedLogger'))().setEvent(m).setMessage('disable_'+k).log();};n.prototype.$FBRTCCallBlockingStore2=function(o,p){c('FBRTCDispatcher').dispatch({type:m,data:p.obj.value});};function n(){h.apply(this,arguments);}f.exports=new n();}),null);
__d('ChatOptions',['Arbiter','ChannelConstants','ChatSidebarActions','ChatSidebarVisibility','FBRTCCallBlockingStore','JSLogger','PresenceUtil','SidebarType','ChatOptionsInitialData'],(function a(b,c,d,e,f,g){var h=c('JSLogger').create('chat_options'),i={};(function(){var k=c('ChatOptionsInitialData');for(var l in k){var m=k[l];if(l==='call_blocked_until'){c('FBRTCCallBlockingStore').init(m);}else i[l]=!!m;}})();var j=Object.assign(new (c('Arbiter'))(),{getSetting:function k(l){return i[l];},setSetting:function k(l,m,n){if(l==='sidebar_mode'){c('ChatSidebarVisibility').shouldShowSidebarIgnoreEnabled(null,function(o,p){if(m){c('ChatSidebarActions').enable(o?c('SidebarType').SIDEBAR:c('SidebarType').BUDDYLIST);}else c('ChatSidebarActions').disable();});return;}if(this.getSetting(l)==m)return;if(n){n='from_'+n;h.log(n,{name:l,new_value:m,old_value:this.getSetting(l)});}i[l]=!!m;c('Arbiter').inform('chat/option-changed',{name:l,value:m});}});c('Arbiter').subscribe(c('ChannelConstants').getArbiterType('setting'),function(k,l){var m=l.obj;if(m.window_id===c('PresenceUtil').getSessionID())return;j.setSetting(m.setting,!!m.value,'channel');});c('Arbiter').subscribe(c('JSLogger').DUMP_EVENT,function(k,l){l.chat_options=i;});f.exports=j;}),null);
__d('ChatQuietLinks',['DataStore','DOM','Event','Parent','UserAgent_DEPRECATED','getOrCreateDOMID'],(function a(b,c,d,e,f,g){var h={},i={silenceLinks:function m(n){j(n,this.removeEmptyHrefs.bind(this));},nukeLinks:function m(n){j(n,this.removeAllHrefs.bind(this));},removeEmptyHrefs:function m(n){k(n,function(o){return !o||o==='#';});},removeAllHrefs:function m(n){k(n);}};function j(m,n){var o=!!c('UserAgent_DEPRECATED').chrome(),p=!!c('UserAgent_DEPRECATED').chrome()||c('UserAgent_DEPRECATED').ie()>=9||c('UserAgent_DEPRECATED').firefox()>=4;if(h[c('getOrCreateDOMID')(m)])return;h[c('getOrCreateDOMID')(m)]=true;if(!p)return;if(!o){n&&n(m);return;}c('Event').listen(m,'mouseover',function q(r){var s=c('Parent').byTag(r.getTarget(),'a');if(s){var t=s.getAttribute('href');if(l(t)){c('DataStore').set(s,'stashedHref',s.getAttribute('href'));s.removeAttribute('href');}}});c('Event').listen(m,'mouseout',function q(r){var s=c('Parent').byTag(r.getTarget(),'a'),t=s&&c('DataStore').remove(s,'stashedHref');if(l(t))s.setAttribute('href',t);});c('Event').listen(m,'mousedown',function(q){if(!q.isDefaultRequested())return true;var r=c('Parent').byTag(q.getTarget(),'a'),s=r&&c('DataStore').get(r,'stashedHref');if(l(s))r.setAttribute('href',s);});}function k(m,n){var o=c('DOM').scry(m,'a');if(n)o=o.filter(function(p){return n(p.getAttribute('href'));});o.forEach(function(p){p.removeAttribute('href');if(!p.tabIndex)p.setAttribute('tabindex',0);});}function l(m){return m&&m!=='#';}f.exports=i;}),null);
__d('ChatUnreadCountActionTypes',['keyMirror'],(function a(b,c,d,e,f,g){'use strict';f.exports=c('keyMirror')({COUNT_UPDATED:null});}),null);
__d('FantaDispatcher',['ExplicitRegistrationDispatcher'],(function a(b,c,d,e,f,g){'use strict';var h,i;h=babelHelpers.inherits(j,c('ExplicitRegistrationDispatcher'));i=h&&h.prototype;function j(){h.apply(this,arguments);}f.exports=new j({strict:false});}),null);
__d('WebMessengerThreadPermalinks',['MercuryIDs','MessagingTag','MessengerURIConstants','URI','WWWBase','requireWeak'],(function a(b,c,d,e,f,g){'use strict';var h={getThreadURI:function j(k,l,m){var n='';if(c('MercuryIDs').isCanonical(k)){n=c('MercuryIDs').tokenize(k).value;}else c('requireWeak')('MercuryThreadIDMap',function(p){n=p.get().getServerIDFromClientIDNow(k);});var o=h.getThreadURIFromServerID(n,m);l&&l(o);},getThreadURIFromServerID:function j(k,l){var m=new (c('URI'))(c('WWWBase').uri),n=c('MessengerURIConstants').FACEBOOK_PREFIX;if(l)switch(l){case c('MessagingTag').OTHER:n+='/filtered';break;case c('MessagingTag').PENDING:n+='/requests';break;case c('MessagingTag').INBOX:break;default:n+='/'+l;break;}m.setPath(n+c('MessengerURIConstants').THREAD_PREFIX+k);return m.toString();},getThreadURIFromUserID:function j(k,l){var m=new (c('URI'))(c('WWWBase').uri),n=c('MessengerURIConstants').FACEBOOK_PREFIX;m.setPath(i(n,l)+'/t/'+k);return m.toString();}};function i(j,k){if(k&&k!=c('MessagingTag').INBOX)j+='/'+k;return j;}f.exports=h;}),null);
__d('FantaTabActions',['Bootloader','FantaDispatcher','MercuryConfig','MessengerURIConstants','URI','WebMessengerThreadPermalinks','goURI','ifRequired','keyMirror'],(function a(b,c,d,e,f,g){'use strict';var h=c('keyMirror')({BLUR_TAB:null,CLOSE_ALL_TABS:null,CLOSE_AND_TAB_NEXT:null,CLOSE_TAB:null,DELETE_TAB:null,FOCUS_NEXT_TAB:null,FOCUS_PREVIOUS_TAB:null,FOCUS_TAB:null,LOAD_FROM_DATA:null,MINIMIZE_ALL_TABS:null,MINIMIZE_TAB:null,OPEN_TAB_WITH_INTERSTITIAL_DATA:null,OPEN_TAB:null,REPLACE_TAB:null,SCROLL_BOTTOM_CHANGED:null,SET_ALLOWED_RAISED_TABS:null,SET_MESSAGE_COUNT:null,SHOW_UNSEEN_MESSAGES:null,UNMINIMIZE_TAB:null});function i(l){var m=l?new (c('URI'))(c('WebMessengerThreadPermalinks').getThreadURIFromServerID(l)):new (c('URI'))(c('MessengerURIConstants').COMPOSE_SUBPATH);c('ifRequired')('BusinessURI.brands',function(n){return c('goURI')(n(m));},function(){return c('goURI')(m);});}function j(l){if(c('MercuryConfig').ChatOpenEventually){setTimeout(function(){k.openTabEventually(l);},100);}else i(l);}var k={Types:h,openTab:function l(m,n){this.dispatchOrBootloadGetMessages(function(){c('FantaDispatcher').dispatch({type:h.OPEN_TAB,tabID:m});c('ifRequired')('FantaTabsReactApp',function(o){this._tryLoadSlimApp(m);}.bind(this),function(){this._tryLoadSlimApp(m,function(){return i(m);});}.bind(this));}.bind(this));},openTabEventually:function l(m){this.dispatchOrBootloadGetMessages(function(){c('FantaDispatcher').dispatch({type:h.OPEN_TAB,tabID:m});c('ifRequired')('FantaTabsReactApp',function(n){this._tryLoadSlimApp(m);}.bind(this),function(){this._tryLoadSlimApp(m,function(){return j(m);});}.bind(this));}.bind(this));},openInterstitialTab:function l(m,n){this.dispatchOrBootloadGetMessages(function(){c('FantaDispatcher').dispatch({type:h.OPEN_TAB_WITH_INTERSTITIAL_DATA,tabID:m,interstitialData:n});c('ifRequired')('FantaTabsReactApp',function(o){this._tryLoadSlimAppWithInterstitialData(m,n);}.bind(this),function(){this._tryLoadSlimAppWithInterstitialData(m,n);}.bind(this));}.bind(this));},_tryLoadSlimApp:function l(m,n){c('ifRequired')('FantaTabsSlimApp',function(o){c('ifRequired')('FantaAppStore',function(){},function(){o.getPumpedUp(function(){c('FantaDispatcher').dispatch({type:h.OPEN_TAB,tabID:m});});});},function(){return n&&n(m);});},_tryLoadSlimAppWithInterstitialData:function l(m,n,o){c('ifRequired')('FantaTabsSlimApp',function(p){c('ifRequired')('FantaAppStore',function(){},function(){p.getPumpedUp(function(){c('FantaDispatcher').dispatch({type:h.OPEN_TAB_WITH_INTERSTITIAL_DATA,tabID:m,interstitialData:n});});});});},replaceTab:function l(m,n){c('FantaDispatcher').dispatch({type:h.REPLACE_TAB,tabID:m,newTabID:n});},minimizeTab:function l(m){c('FantaDispatcher').dispatch({type:h.MINIMIZE_TAB,tabID:m});},minimizeAllTabs:function l(){c('FantaDispatcher').dispatch({type:h.MINIMIZE_ALL_TABS});},unminimizeTab:function l(m){c('FantaDispatcher').dispatch({type:h.UNMINIMIZE_TAB,tabID:m});},closeTab:function l(m){c('FantaDispatcher').dispatch({type:h.CLOSE_TAB,tabID:m});},closeAllTabs:function l(){c('FantaDispatcher').dispatch({type:h.CLOSE_ALL_TABS});},closeAndTabNext:function l(m){c('FantaDispatcher').dispatch({type:h.CLOSE_AND_TAB_NEXT,tabID:m});},deleteTab:function l(m){c('FantaDispatcher').dispatch({type:h.DELETE_TAB,tabID:m});},focusTab:function l(m){c('FantaDispatcher').dispatch({type:h.FOCUS_TAB,tabID:m});},blurTab:function l(m){c('FantaDispatcher').dispatch({type:h.BLUR_TAB,tabID:m});},setAllowedRaisedTabs:function l(m){c('FantaDispatcher').dispatch({type:h.SET_ALLOWED_RAISED_TABS,allowedRaisedTabs:m});},loadFromData:function l(m){this.dispatchOrBootloadGetMessages(function(){c('FantaDispatcher').dispatch({type:h.LOAD_FROM_DATA,tabData:m});});},focusNextTab:function l(event){c('FantaDispatcher').dispatch({type:h.FOCUS_NEXT_TAB,event:event});},focusPreviousTab:function l(event){c('FantaDispatcher').dispatch({type:h.FOCUS_PREVIOUS_TAB,event:event});},scrollBottomChanged:function l(m,n,o){c('FantaDispatcher').dispatch({type:h.SCROLL_BOTTOM_CHANGED,isScrolledToBottom:n,tabID:m,showUnseenMessages:o});},showUnseenMessages:function l(m){c('FantaDispatcher').dispatch({type:h.SHOW_UNSEEN_MESSAGES,tabID:m});},dispatchOrBootloadGetMessages:function l(m){c('ifRequired')('FantaReducersGetMessages',function(){m();},function(){c('ifRequired')('FantaAppStore',function(n){c('Bootloader').loadModules(["FantaReducersGetMessages"],function(o){n.addReducers(o);m();},'FantaTabActions');},function(){m();});});}};f.exports=k;}),null);
__d('MessengerDispatcher',['Dispatcher_DEPRECATED'],(function a(b,c,d,e,f,g){'use strict';f.exports=new (c('Dispatcher_DEPRECATED'))();}),null);
__d('PagesLikeFollowNotifDispatcher',['Arbiter','ExplicitRegistrationReactDispatcher','PageLikeConstants','PagesLikeFollowNotifActions','SubscriptionsHandler'],(function a(b,c,d,e,f,g){'use strict';var h,i;h=babelHelpers.inherits(j,c('ExplicitRegistrationReactDispatcher'));i=h&&h.prototype;function j(k){i.constructor.call(this,k);var l=new (c('SubscriptionsHandler'))();l.addSubscriptions(c('Arbiter').subscribe(c('PageLikeConstants').LIKED,function(m,n){return this.dispatchLike(n.profile_id);}.bind(this)),c('Arbiter').subscribe(c('PageLikeConstants').UNLIKED,function(m,n){return this.dispatchUnlike(n.profile_id);}.bind(this)));}j.prototype.dispatchLike=function(k){this.dispatch({type:c('PagesLikeFollowNotifActions').LIKE,data:{pageID:k,likeStatus:true}});};j.prototype.dispatchUnlike=function(k){this.dispatch({type:c('PagesLikeFollowNotifActions').UNLIKE,data:{pageID:k,likeStatus:false}});};f.exports=new j({strict:true});}),null);
__d('PagesFollowStore',['FluxReduceStore','PagesLikeFollowNotifActions','PagesLikeFollowNotifDispatcher'],(function a(b,c,d,e,f,g){'use strict';var h,i;h=babelHelpers.inherits(j,c('FluxReduceStore'));i=h&&h.prototype;j.prototype.getInitialState=function(){return {};};j.prototype.reduce=function(k,l){var m=babelHelpers['extends']({},k);switch(l.type){case c('PagesLikeFollowNotifActions').INIT_DATA:if(l.data.pageID in k)return k;m[l.data.pageID]=l.data.followStatus;return m;case c('PagesLikeFollowNotifActions').FOLLOW_CHANGED:m[l.data.pageID]=l.data.followStatus;return m;}return k;};function j(){h.apply(this,arguments);}f.exports=new j(c('PagesLikeFollowNotifDispatcher'));}),null);
__d("Utf16",[],(function a(b,c,d,e,f,g){var h={decode:function i(j){switch(j.length){case 1:return j.charCodeAt(0);case 2:return 65536|(j.charCodeAt(0)-55296)*1024|j.charCodeAt(1)-56320;default:return null;}},encode:function i(j){if(j<65536){return String.fromCharCode(j);}else return String.fromCharCode(55296+(j-65536>>10))+String.fromCharCode(56320+j%1024);}};f.exports=h;}),null);
__d('createEmojiElement',['cx','JSXDOM'],(function a(b,c,d,e,f,g,h){function i(j,k,l){l=l||16;return c('JSXDOM').span({className:"_5mfr _47e3"},[c('JSXDOM').img({'aria-hidden':true,className:'img',height:l,src:k,width:l}),c('JSXDOM').span({className:"_7oe"},j)]);}f.exports=i;}),null);
__d('DOMEmoji',['cx','EmojiImageURL','EmojiRenderer','FBEmojiUtils','JSXDOM','SupportedFBEmoji','Utf16','createEmojiElement','flattenArray','isElementNode'],(function a(b,c,d,e,f,g,h){'use strict';var i={MAX_ITEMS:40,transform:function j(k,l){l=l||{};var m=l.size||16;return c('flattenArray')(k.map(function(n){if(!c('isElementNode')(n)){return c('EmojiRenderer').render(n,function(o){if(l.isSupportedEmoji){var p=c('FBEmojiUtils').getKeyFromCodepoints(o);if(l.isSupportedEmoji(p))return c('createEmojiElement')(o.join(''),c('EmojiImageURL').getMessengerURL(p,m),m);}else{var q=c('FBEmojiUtils').getSupportedKey(o);if(q)return c('createEmojiElement')(o.join(''),c('EmojiImageURL').getFBEmojiURL(q,m),m);}return c('JSXDOM').span({className:"_4ay8"+(m===16?' '+"_3kkw":'')},o.join(''));},this.MAX_ITEMS);}else return n;}.bind(this)));},params:function j(k){if(!k)return this;var l=this;return {__params:true,obj:l,params:k};}};f.exports=i;}),null);
__d('EmoticonEmojiList',[],(function a(b,c,d,e,f,g){f.exports={names:{':)':'slightsmile',':-)':'slightsmile',':]':'slightsmile','=)':'smile','(:':'slightsmile','(=':'smile',':(':'frown',':-(':'frown',':[':'frown','=(':'frown',')=':'frown',';-P':'winktongue',';P':'winktongue',';-p':'winktongue',';p':'winktongue',':poop:':'poop',':P':'tongue',':-P':'tongue',':-p':'tongue',':p':'tongue','=P':'tongue','=p':'tongue','=D':'grin',':-D':'slightgrin',':D':'slightgrin',':o':'gasp',':-O':'gasp',':O':'gasp',':-o':'gasp',';)':'wink',';-)':'wink','8-)':'glasses','8)':'glasses','B-)':'glasses','B)':'glasses','>:(':'grumpy','>:-(':'grumpy',':/':'unsure',':-/':'unsure',':\\':'unsure',':-\\':'unsure','=/':'unsure','=\\':'unsure',':\'(':'cry',':\'-(':'cry','3:)':'devil','3:-)':'devil','O:)':'angel','O:-)':'angel','0:)':'angel','0:-)':'angel',':*':'kiss',':-*':'kiss',';-*':'winkkiss',';*':'winkkiss','<3':'heart','&lt;3':'heart','\u2665':'heart','^_^':'kiki','^~^':'kiki','-_-':'expressionless',':-|':'squint',':|':'squint','>:o':'upset','>:O':'upset','>:-O':'upset','>:-o':'upset','>_<':'persevere','>.<':'persevere','<(")':'penguin',O_O:'flushface',o_o:'flushface','0_0':'flushface',T_T:'crying','T-T':'crying',ToT:'crying','-3-':'flushkiss','\'-_-':'sweating','(y)':'like',':like:':'like','(Y)':'like','(n)':'dislike','(N)':'dislike'},emote2emojis:{slightsmile:'1f642',smile:'1f60a',frown:'1f61e',winktongue:'1f61c',poop:'1f4a9',tongue:'1f61b',slightgrin:'1f600',grin:'1f603',gasp:'1f62e',wink:'1f609',glasses:'1f60e',grumpy:'1f620',unsure:'1f615',cry:'1f622',devil:'1f608',angel:'1f607',kiss:'1f617',winkkiss:'1f618',heart:'2764',kiki:'1f60a',expressionless:'1f611',squint:'1f610',upset:'1f620',persevere:'1f623',penguin:'1f427',flushface:'1f633',crying:'1f62d',flushkiss:'1f61a',sweating:'1f613',like:'f0000',dislike:'1f44e'},symbols:{slightsmile:':)',smile:'=)',frown:':(',winktongue:';-P',poop:':poop:',tongue:':P',slightgrin:':D',grin:'=D',gasp:':o',wink:';)',glasses:'8-)',grumpy:'>:(',unsure:':/',cry:':\'(',devil:'3:)',angel:'O:)',kiss:':*',winkkiss:';*',heart:'<3',kiki:'^_^',expressionless:'-_-',squint:':-|',upset:'>:o',persevere:'>_<',penguin:'<(")',flushface:'O_O',crying:'T_T',flushkiss:'-3-',sweating:'\'-_-',like:'(y)',dislike:'(n)'},regexp:/(^|[\s\'\".])(:\)(?!\))|:\-\)(?!\))|:\]|=\)(?!\))|\(:|\(=|:\(|:\-\(|:\[|=\(|\)=|;P|;\-P|;\-p|;p|:poop:|:P|:\-P|:\-p|:p|=P|=p|=D|:\-D|:D|:o|:\-O|:O|:\-o|;\)(?!\))|;\-\)(?!\))|8\-\)(?!\))|B\-\)(?!\))|B\)(?!\))|8\)(?!\))|>:\(|>:\-\(|:\/|:\-\/|:\\|:\-\\|=\/|=\\|:\'\(|:\'\-\(|3:\)(?!\))|3:\-\)(?!\))|O:\)(?!\))|O:\-\)(?!\))|0:\)(?!\))|0:\-\)(?!\))|:\*|:\-\*|;\*|;\-\*|<3|&lt;3|\u2665|\^_\^|\^~\^|\-_\-|:\-\||:\||>:o|>:O|>:\-O|>:\-o|>_<|>\.<|<\(\"\)(?!\))|O_O|o_o|0_0|T_T|T\-T|ToT|\-3\-|\'\-_\-|\(y\)(?!\))|:like:|\(Y\)(?!\))|\(n\)(?!\))|\(N\)(?!\)))([\s\'\".,!?]|<br>|$)/,noncapturingRegexp:/(?:^|[\s\'\".])(:\)(?!\))|:\-\)(?!\))|:\]|=\)(?!\))|\(:|\(=|:\(|:\-\(|:\[|=\(|\)=|;P|;\-P|;\-p|;p|:poop:|:P|:\-P|:\-p|:p|=P|=p|=D|:\-D|:D|:o|:\-O|:O|:\-o|;\)(?!\))|;\-\)(?!\))|8\-\)(?!\))|B\-\)(?!\))|B\)(?!\))|8\)(?!\))|>:\(|>:\-\(|:\/|:\-\/|:\\|:\-\\|=\/|=\\|:\'\(|:\'\-\(|3:\)(?!\))|3:\-\)(?!\))|O:\)(?!\))|O:\-\)(?!\))|0:\)(?!\))|0:\-\)(?!\))|:\*|:\-\*|;\*|;\-\*|<3|&lt;3|\u2665|\^_\^|\^~\^|\-_\-|:\-\||:\||>:o|>:O|>:\-O|>:\-o|>_<|>\.<|<\(\"\)(?!\))|O_O|o_o|0_0|T_T|T\-T|ToT|\-3\-|\'\-_\-|\(y\)(?!\))|:like:|\(Y\)(?!\))|\(n\)(?!\))|\(N\)(?!\)))(?:[\s\'\".,!?]|<br>|$)/};}),null);
__d('TransformTextToDOMMixin',['flattenArray','isElementNode'],(function a(b,c,d,e,f,g){var h=3,i={transform:function j(k,l){return c('flattenArray')(k.map(function(m){if(!c('isElementNode')(m)){var n=m,o=[],p=this.MAX_ITEMS||h;while(p--){var q=l?[n].concat(l):[n],r=this.match.apply(this,q);if(!r)break;o.push(n.substring(0,r.startIndex));o.push(r.element);n=n.substring(r.endIndex);}n&&o.push(n);return o;}return m;}.bind(this)));},params:function j(){for(var k=arguments.length,l=Array(k),m=0;m<k;m++)l[m]=arguments[m];var n=this;return {__params:true,obj:n,params:l};}};f.exports=i;}),null);
__d('DOMEmote',['cx','fbt','EmojiImageURL','EmoticonEmojiList','EmoticonsList','JSXDOM','SupportedFBEmoji','TransformTextToDOMMixin'],(function a(b,c,d,e,f,g,h,i){'use strict';var j={MAX_ITEMS:40,match:function k(l,m){var n=m&&m.getMessengerEmote,o=n?c('EmoticonEmojiList').regexp.exec(l):c('EmoticonsList').regexp.exec(l);if(!o||!o.length)return false;var p=o[2],q=o.index+o[1].length,r=n?c('EmoticonEmojiList').names[p]:c('EmoticonsList').emotes[p];return {startIndex:q,endIndex:q+p.length,element:this._element(p,r,m)};},_element:function k(l,m,n){var o=n&&n.getMessengerEmote,p=o?o(m):c('EmoticonsList').emoji[m],q=null;if(o&&p){q=c('JSXDOM').img({'aria-hidden':true,className:'img',height:16,src:c('EmojiImageURL').getMessengerURL(p,16),width:16});}else if(p){q=c('JSXDOM').img({'aria-hidden':true,className:'img',height:16,src:c('SupportedFBEmoji')[p]?c('EmojiImageURL').getFBEmojiURL(p):c('EmojiImageURL').getFBEmojiExtendedURL(p),width:16});}else q=c('JSXDOM').span({'aria-hidden':true,className:'emoticon emoticon_'+m});var r=i._("{emoticonName} emoticon",[i.param('emoticonName',m)]);return c('JSXDOM').span({className:"_47e3 _5mfr",title:r},[q,c('JSXDOM').span({'aria-hidden':true,className:"_7oe"},l)]);}};f.exports=Object.assign(j,c('TransformTextToDOMMixin'));}),null);
__d('transformTextToDOM',['createArrayFromMixed'],(function a(b,c,d,e,f,g){function h(i,j){var k=[i];j=c('createArrayFromMixed')(j);j.forEach(function(l){var m,n=l;if(l.__params){m=l.params;n=l.obj;}k=n.transform(k,m);});return k;}f.exports=h;}),null);
__d('emojiAndEmote',['DOMEmoji','DOMEmote','FbtResultBase','transformTextToDOM'],(function a(b,c,d,e,f,g){'use strict';var h=function i(j,k){if(j instanceof c('FbtResultBase'))return [j];var l=k?{isSupportedEmoji:k.isSupportedEmoji}:null,m=k?{getMessengerEmote:k.getMessengerEmote}:null,n=[c('DOMEmoji').params(l),c('DOMEmote').params(m)];return c('transformTextToDOM')(j,n);};f.exports=h;}),null);
__d('CompactTypeaheadRenderer',['BadgeHelper','DOM','emojiAndEmote','TypeaheadFacepile','isSocialPlugin'],(function a(b,c,d,e,f,g){function h(i,j){var k=[];if(i.xhp)return c('DOM').create('li',{className:'raw'},i.xhp);var l=i.photos||i.photo;if(l){if(l instanceof Array){l=c('TypeaheadFacepile').render(l);}else l=c('DOM').create('img',{alt:'',src:l});k.push(l);}var m=i.iconClass;if(m){var n=c('DOM').create('span',{className:m});k.push(n);}var o=i.debug_info;if(o)k.push(c('DOM').create('span',{className:'debugInfo'},o));if(i.text){var p=[i.text];if(!c('isSocialPlugin')())p=c('emojiAndEmote')(i.text);if(i.is_verified){p.push(c('BadgeHelper').renderBadge('xsmall','verified'));}else if(i.is_work_user){p.push(c('BadgeHelper').renderBadge('xsmall','work'));}else if(i.is_trending_hashtag)p.push(c('BadgeHelper').renderBadge('xsmall','trending'));k.push(c('DOM').create('span',{className:'text'},p));}var q=i.subtext,r=i.category;if(q||r){var s=[];q&&s.push(q);q&&r&&s.push(" \u00b7 ");r&&s.push(r);k.push(c('DOM').create('span',{className:'subtext'},s));}var t=c('DOM').create('li',{className:i.type||''},k);if(i.text){t.setAttribute('title',i.text);t.setAttribute('aria-label',i.text);}return t;}h.className='compact';f.exports=h;}),null);
__d('legacy:CompactTypeaheadRenderer',['CompactTypeaheadRenderer'],(function a(b,c,d,e,f,g){if(!b.TypeaheadRenderers)b.TypeaheadRenderers={};b.TypeaheadRenderers.compact=c('CompactTypeaheadRenderer');}),3);