webpackJsonp([19],{280:function(e,t,n){"use strict";var i=n(62);e.exports=i.extend({template:n(312),className:"toggle sc-toggle",tagName:"label",defaults:{label:"",name:"",size:"",iconActive:"",iconInactive:"",isActive:!1},element2selector:{input:".sc-toggle-input"},states:{active:"sc-toggle-active"},events:{"change .sc-toggle-input":"onInputChange"},setup:function(e){this.toggleState("active",e.isActive),e.size&&this.$el.addClass("sc-toggle-"+e.size)},getTemplateData:function(e){return e.showIcon=this.options.size&&this.options.iconActive&&this.options.iconInactive,e.isActive=this.getState("active"),e},getChecked:function(){return this.getElement("input").prop("checked")},setChecked:function(e){this.getElement("input").prop("checked",!!e),this.toggleState("active",e)},onInputChange:function(e){var t=e.target.checked;this.toggleState("active",t),this.bubble("toggle:change",{name:this.options.name,isActive:t})}})},290:function(e,t,n){"use strict";function i(){return"string"==typeof this.options.size?a[this.options.size]:this.options.size}var a,r=n(3),s=n(88),o=n(68),l=n(94),u=n(62);a={tiny:20,xsmall:30,small:40,medium:50,large:100,xlarge:200};e.exports=u.extend(o.withOptions("groupAvatarBadge"),{template:n(315),className:"g-avatar-badge groupAvatarBadge",ModelClass:s,requiredAttributes:["permalink","name"],defaults:{hover_actions:!1,is_link:!0,stretch:!1,size:"small"},states:{hoverActions:"hoverActions"},setup:function(e){e.hover_actions=e.hover_actions&&!l.touch,this.toggleState("hoverActions",e.hover_actions)},loadingTemplate:function(){var e=i.call(this);return'<img width="'+e+'" height="'+e+'">'},getTemplateData:function(e){var t=i.call(this);return r.assign(e,{imageSize:t,onlineBadgeSize:t<=a.medium?"small":"medium",show_join_button:!this.model.isMyGroup()})}})},312:function(e,t,n){var i=n(21);e.exports=(i["default"]||i).template({1:function(e,t,i,a,r){var s;return"    "+e.escapeExpression((n(83)||t&&t.$a11y||i.helperMissing).call(null!=t?t:{},{name:"$a11y",hash:{screenreader:null!=(s=null!=t?t._options:t)?s.label:s},data:r}))+"\n"},3:function(e,t,n,i,a){var r,s=e.lambda,o=e.escapeExpression;return'    <span class="sc-toggle-icon-inactive sc-icon sc-icon-'+o(s(null!=(r=null!=t?t._options:t)?r.size:r,t))+" "+o(s(null!=(r=null!=t?t._options:t)?r.iconInactive:r,t))+'"></span>\n    <span class="sc-toggle-icon-active sc-icon-'+o(s(null!=(r=null!=t?t._options:t)?r.size:r,t))+" "+o(s(null!=(r=null!=t?t._options:t)?r.iconActive:r,t))+'"></span>\n'},5:function(e,t,n,i,a){return"checked"},compiler:[7,">= 4.0.0"],main:function(e,t,n,i,a){var r,s=null!=t?t:{};return'<span class="sc-toggle-handle">\n'+(null!=(r=n["if"].call(s,null!=(r=null!=t?t._options:t)?r.label:r,{name:"if",hash:{},fn:e.program(1,a,0),inverse:e.noop,data:a}))?r:"")+"\n"+(null!=(r=n["if"].call(s,null!=t?t.showIcon:t,{name:"if",hash:{},fn:e.program(3,a,0),inverse:e.noop,data:a}))?r:"")+'</span>\n\n<input class="sc-toggle-input sc-visuallyhidden" type="checkbox" '+(null!=(r=n["if"].call(s,null!=t?t.isActive:t,{name:"if",hash:{},fn:e.program(5,a,0),inverse:e.noop,data:a}))?r:"")+">\n"},useData:!0})},314:function(e,t,n){var i=n(21);e.exports=(i["default"]||i).template({compiler:[7,">= 4.0.0"],main:function(e,t,i,a,r){var s;return e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(280),{name:"$view",hash:{key:"toggle",isActive:null!=t?t.isActive:t,iconInactive:null!=(s=null!=t?t._options:t)?s.iconInactive:s,iconActive:null!=(s=null!=t?t._options:t)?s.iconActive:s,size:null!=(s=null!=t?t._options:t)?s.size:s,label:null!=t?t.defaultLabel:t},data:r}))+"\n"},useData:!0})},315:function(e,t,n){var i=n(21);e.exports=(i["default"]||i).template({1:function(e,t,i,a,r){var s,o=null!=t?t:{},l=i.helperMissing,u=e.escapeExpression;return'        <a href="'+u((n(152)||t&&t.$relativeUrl||l).call(o,null!=t?t.permalink_url:t,{name:"$relativeUrl",hash:{},data:r}))+'" title="Go to '+u((s=null!=(s=i.name||(null!=t?t.name:t))?s:l,"function"==typeof s?s.call(o,{name:"name",hash:{},data:r}):s))+'">\n'},3:function(e,t,n,i,a){return"        </a>\n"},5:function(e,t,i,a,r){return"    <a href='"+e.escapeExpression((n(64)||t&&t.$route||i.helperMissing).call(null!=t?t:{},"group",t,{name:"$route",hash:{},data:r}))+'\' class="g-avatar-badge-avatar-link">\n'},7:function(e,t,n,i,a){return"    </a>\n"},9:function(e,t,i,a,r){return'    <div class="groupBadge__actions sc-button-toolbar">\n      '+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(211),{name:"$view",hash:{is_cta:!0,resource_id:null!=t?t.id:t,size:"small"},data:r}))+"\n    </div>\n"},compiler:[7,">= 4.0.0"],main:function(e,t,i,a,r){var s,o=null!=t?t:{},l=i.helperMissing,u=e.escapeExpression;return'<div class="g-avatar-badge-header">\n  <div class="sc-type-h2 sc-type-light">\n    <span class="g-type-shrinkwrap-inline">\n'+(null!=(s=i["if"].call(o,null!=(s=null!=t?t._options:t)?s.is_link:s,{name:"if",hash:{},fn:e.program(1,r,0),inverse:e.noop,data:r}))?s:"")+"        "+u((n(119)||t&&t.$usertextOneline||l).call(o,null!=t?t.name:t,{name:"$usertextOneline",hash:{maxLength:"90",links:!1},data:r}))+"\n"+(null!=(s=i["if"].call(o,null!=(s=null!=t?t._options:t)?s.is_link:s,{name:"if",hash:{},fn:e.program(3,r,0),inverse:e.noop,data:r}))?s:"")+"    </span>\n    &#8203; \n  </div>\n  <div>\n    "+u((n(61)||t&&t.$view||l).call(o,n(215),{name:"$view",hash:{resource_id:null!=t?t.id:t,inverted:!0,size:"small"},data:r}))+'\n  </div>\n</div>\n\n<div class="g-avatar-badge-body">\n'+(null!=(s=i["if"].call(o,null!=(s=null!=t?t._options:t)?s.is_link:s,{name:"if",hash:{},fn:e.program(5,r,0),inverse:e.noop,data:r}))?s:"")+'  <div class="g-avatar-badge-avatar">\n    '+u((n(61)||t&&t.$view||l).call(o,n(78),{name:"$view",hash:{stretch:null!=(s=null!=t?t._options:t)?s.stretch:s,size:null!=t?t.imageSize:t,resource_type:null!=t?t._resource_type:t,resource_id:null!=t?t._resource_id:t},data:r}))+"\n  </div>\n"+(null!=(s=i["if"].call(o,null!=(s=null!=t?t._options:t)?s.is_link:s,{name:"if",hash:{},fn:e.program(7,r,0),inverse:e.noop,data:r}))?s:"")+'</div>\n\n<div class="g-avatar-badge-footer g-opacity-transition">\n'+(null!=(s=i["if"].call(o,null!=t?t.show_join_button:t,{name:"if",hash:{},fn:e.program(9,r,0),inverse:e.noop,data:r}))?s:"")+"</div>\n"},useData:!0})},369:function(e,t,n){"use strict";var i=n(88),a=n(62);e.exports=a.extend({template:n(673),css:n(737),className:"groupBadge sc-media",ModelClass:i,requiredAttributes:["artwork_url","permalink_url","name"],getTemplateData:function(e){return e.show_join_button=!this.model.isMyGroup(),e}})},397:function(e,t,n){"use strict";var i=n(3),a=n(27),r=n(74),s=n(65),o=n(88);e.exports=r.extend({model:o,baseUrl:"groups",fetch:function(e){var t=this,n=e&&e.url||i.result(this,"url");return n?this._requests&&this._requests[n]||a.Collection.prototype.fetch.call(this,e).done(function(e){var n=!1;e.next_href&&(n=e.next_href.replace(/\/me\//,"/")),t.next_href=n}):s.resolve({})}},{hashFn:function(){return 1}})},400:function(e,t,n){"use strict";var i=n(105),a=n(138);e.exports=a.extend({model:i,defaults:{type:"comments"},baseUrl:function(){return this.getEndpointUrl("userComments",{id:this.options.userId})}})},473:function(e,t,n){"use strict";function i(e,t){var n=this.options,i=this.subviews.toggle;this.$el.attr("title",t?n.activeLabel:n.inactiveLabel),i.getChecked()!==t&&i.setChecked(t)}var a=n(3),r=n(23),s=n(63),o=n(62),l=100;e.exports=o.extend({className:"shuffleButton",template:n(314),defaults:{iconActive:"sc-icon-shuffle-orange",iconInactive:"sc-icon-shuffle",Collection:null,inactiveLabel:s.t("Turn on shuffle mode"),resource_id:null,activeLabel:s.t("Turn off shuffle mode"),size:"medium"},bubbleEvents:{"toggle:change":"onToggleChange"},attributes:{role:"button"},setup:function(e){var t=e.Collection,n=e.resource_id;this.source=new t(null,{resource_id:n}),this.listenTo(this.source,"shuffled",i),this.attributes=a.clone(this.attributes)},dispose:function(){this.source.release()},getTemplateData:function(e){return e.isActive=this.source.isShuffled(),e.defaultLabel=e.isActive?this.options.activeLabel:this.options.inactiveLabel,e},renderDecorate:function(){this.source.length<l&&!this.source.isFullyPopulated()&&this.source.bulkFetch(l)},onToggleChange:function(e){var t=e.data.isActive;this.source.toggleShuffle(t),r.trigger("tracking:shuffle",{isActive:t})}})},474:function(e,t,n){"use strict";var i=n(105),a=n(22),r=n(209),s=n(62);e.exports=s.extend({template:n(668),css:n(732),className:"commentBadge",ModelClass:i,requiredAttributes:["user"],defaults:{compact:!0},states:{canDelete:"canDelete",dialogOpen:"dialogOpen"},initialize:function(){this.bubbleEvents={},this.bubbleEvents[r.TOGGLE]="onDeleteDialogToggle",s.prototype.initialize.apply(this,arguments)},renderDecorate:function(){this.toggleState("canDelete",a.get("me").owns(this.model))},onDeleteDialogToggle:function(){this.toggleState("dialogOpen",this.subviews.deleteCommentButton.isOverlayOpened())},getTemplateData:function(e){e.canDelete=a.get("me").owns(this.model)}})},477:function(e,t,n){"use strict";var i=n(69),a=n(62);e.exports=a.extend({template:n(669),tagName:"div",ModelClass:i,requiredAttributes:["title","permalink"]})},480:function(e,t,n){"use strict";var i=n(22),a=n(63),r=86558888,s={stream:{heading:a.t("This is your stream"),text:a.t("Follow your favorite artists, labels and friends on SoundCloud<br/> and see every track they post right here."),shouldShowHeader:function(){return i.get("me").id>r}},likesPage:{heading:a.t("This is where all your Likes are saved."),text:a.t("Looking for more tracks to like? Use Search & Explore to find great music & audio. <br/>Make a great discovery? Create a Playlist or use Reposts to share your best finds with people that follow you."),shouldShowHeader:function(){return i.get("me").id>r}}};e.exports={get:function(e){return s[e]}}},481:function(e,t,n){"use strict";function i(e){var t=a.get(e);return!t.shouldShowHeader||t.shouldShowHeader()}var a=n(480),r=n(100),s=n(169),o=n(62),l=new r("already-seen");e.exports=o.extend(s.withOptions({automatic:!1}),{template:n(672),className:"featureHeader sc-border-light-bottom",css:n(736),states:{visible:"visible"},events:{"click .featureHeader__closeButton":"onDismissClick"},defaults:{featureKey:null,dismissAfter:3},alreadySeenKey:function(){return this.options.featureKey+"-header"},setup:function(e){var t=this.alreadySeenKey(),n=l.get(t)||0,a=i(e.featureKey)&&n<e.dismissAfter;this.toggleState("visible",a),a?l.set(t,n+1):l.set(t,99)},onDismissClick:function(e){e.preventDefault(),l.set(this.alreadySeenKey(),99),this.slideUp()},getTemplateData:function(){return a.get(this.options.featureKey)}})},482:function(e,t,n){"use strict";var i=n(3),a=n(22),r=n(84),s=n(397),o=n(369),l=n(290),u=n(63),c=n(70),d=n(401),p=n(67);e.exports=r.extend({css:[n(738),n(118)],className:"sc-border-box",Subview:null,defaults:{size:"small",subviewName:"user-badge",showEmptyNetworkPage:!1},setup:function(e){var t=e.resource_id,i=t?d:s;"user-avatar-badge"===e.subviewName?(this.Subview=l,this.$el.addClass("g-avatar-badge-list")):(this.Subview=o,this.$el.addClass("groupsList"),this.itemClassName="groupsList__item"),e.showEmptyNetworkPage&&(this.emptyTemplate=n(117)),this.collection=new i(null,{resource_id:t}),this.user=this.addDataSource(new p({id:t}),{requiredAttributes:["username"]})},getTemplateData:function(e){var t=this.options,n=this.user;return t.showEmptyNetworkPage&&(a.get("me").owns(n)?(e.message=u.t("You’re not a member of any groups."),e.linkUrl=c.getRoute("v1",["groups/new"]),e.linkText=u.t("Create a new group.")):e.message=u.t("[[username]] hasn’t joined any groups.",{username:n.get("username")}),e.emptyPageClass="emptyGroups"),e},getSubviewArgs:function(){var e=this.options,t=e.size,n=e.subviewName,a="user-avatar-badge"===n?{size:t,hover_actions:!0}:{};return i.assign(r.prototype.getSubviewArgs.apply(this,arguments),a)}})},521:function(e,t,n){"use strict";var i=n(458),a=n(62);e.exports=a.extend({ModelClass:i,template:n(706)})},539:function(e,t,n){"use strict";var i=n(148),a=n(22),r=n(89),s=n(84),o=n(70),l=n(67),u=n(231),c=n(338),d=n(63);e.exports=s.extend(r,i,{Subview:n(521),css:[n(129),n(118)],className:"soundList",itemClassName:"soundList__item",emptyTemplate:n(117),defaults:{type:"likes"},animations:{remove:{delay:0}},user:null,setup:function(e){var t=e.resource_id,n="likes"===e.type?u:c;this.collection=new n(null,{userId:t,resource_id:t}),this.collection.setLimit(24),this.user=this.addDataSource(new l({id:t}),{requiredAttributes:["username"]})},getTemplateData:function(e){return a.get("me")===this.user?(e.message=d.t("You have no likes yet."),e.linkUrl=o.getRoute("explore"),e.linkText=d.t("Explore Trending Music")):e.message=d.t("[[username]] hasn’t liked any tracks.",{username:this.user.get("username")}),e.emptyPageClass="emptyLikes",e}})},540:function(e,t,n){"use strict";var i=n(22),a=n(89),r=n(403),s=n(67),o=n(84),l=n(63);e.exports=o.extend(a,{Subview:n(79),css:[n(129),n(118)],className:"soundList",itemClassName:"soundList__item",emptyTemplate:n(117),defaults:{showEndView:!0},user:null,setup:function(e){var t=e.resource_id;this.collection=new r(null,{userId:t}),this.user=this.addDataSource(new s({id:t}),{requiredAttributes:["username"]})},getTemplateData:function(e){return i.get("me")===this.user?(e.message=l.t("You haven’t created any playlists."),e.linkUrl="http://uploadandmanage.help.soundcloud.com/customer/portal/articles/2166978",e.linkExternal=!0,e.linkText=l.t("Learn about playlists")):e.message=l.t("[[username]] hasn’t created any playlists yet.",{username:this.user.get("username")}),e.emptyPageClass="emptySets",e}})},541:function(e,t,n){"use strict";var i=n(22),a=n(89),r=n(84),s=n(79),o=n(67),l=n(232),u=n(63);e.exports=r.extend(a,{className:"soundList",itemClassName:"soundList__item",css:[n(129),n(118)],emptyTemplate:n(117),defaults:{showEndView:!0},Subview:s,setup:function(e){var t=e.resource_id;this.collection=new l(null,{userId:t,keepBlocked:!1}),this.user=this.addDataSource(new o({id:t}),{requiredAttributes:["username"]})},getTemplateData:function(e){return i.get("me")===this.user?(e.message=u.t("Seems a little quiet over here"),e.linkUrl="http://uploadandmanage.help.soundcloud.com/customer/portal/articles/2122042",e.linkExternal=!0,e.linkText=u.t("Upload a track to share it with your followers.")):(e.message=u.t("Nothing to hear here"),e.subheaderMessage=u.t("Follow [[username]] for updates on sounds they share in the future.",{username:this.user.get("username")})),e.emptyPageClass="emptyTracks",e}})},560:function(e,t,n){t=e.exports=n(6)(),t.push([e.id,".commentBadge{position:relative;overflow:hidden}.commentBadge__title{margin-right:70px}.commentBadge:hover .commentBadge__title a{color:#333}.commentBadge__time{color:#ccc;position:absolute;right:0;top:0}.commentBadge__deleteCommentButton{display:none;position:absolute;top:5px;right:7px}.commentBadge:hover .commentBadge__deleteCommentButton,.commentBadge.dialogOpen .commentBadge__deleteCommentButton{display:block}.commentBadge.dialogOpen .commentBadge__time,.commentBadge.canDelete:hover .commentBadge__time{display:none}.commentBadge__body:before{content:'“'}.commentBadge__body:after{content:'”'}",""])},562:function(e,t,n){t=e.exports=n(6)(),t.push([e.id,".featureHeader{margin-bottom:20px;padding:0 15px 10px 0;position:relative;line-height:1.3;display:none}.featureHeader.visible{display:block}.featureHeader__title{font-size:24px;margin:0 0 5px;line-height:1}.featureHeader__closeButton{background:url("+n(222)+") no-repeat 0 0;position:absolute;right:12px;top:15px;width:15px;height:15px}@media (min-width:1400px){.featureHeader__content br{display:none}}",""])},563:function(e,t,n){t=e.exports=n(6)(),t.push([e.id,".groupBadge{position:relative}.groupBadge__actions{position:absolute;right:0;bottom:2px}.groupBadge__title{margin-top:6px;padding-bottom:0}.groupBadge__titleLink{max-width:100%;display:block}",""])},564:function(e,t,n){t=e.exports=n(6)(),t.push([e.id,".groupsList .loading{padding:85px 0}.groupsList__item{padding:10px 0}.groupsList__empty{padding:20px 0}",""])},668:function(e,t,n){var i=n(21);e.exports=(i["default"]||i).template({1:function(e,t,n,i,a){return" sc-font-light"},3:function(e,t,i,a,r){return e.escapeExpression((n(119)||t&&t.$usertextOneline||i.helperMissing).call(null!=t?t:{},null!=t?t.body:t,{name:"$usertextOneline",hash:{maxLength:200,links:!1},data:r}))},5:function(e,t,i,a,r){return e.escapeExpression((n(164)||t&&t.$usertext||i.helperMissing).call(null!=t?t:{},null!=t?t.body:t,{name:"$usertext",hash:{paragraphs:!1},data:r}))},7:function(e,t,i,a,r){return'  <div class="commentBadge__deleteCommentButton">\n    '+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(286),{name:"$view",hash:{size:null!=t?t.button_size:t,key:"deleteCommentButton",resource_id:null!=t?t._resource_id:t},data:r}))+"\n  </div>\n"},compiler:[7,">= 4.0.0"],main:function(e,t,i,a,r){var s,o=null!=t?t:{},l=i.helperMissing,u=e.escapeExpression;return'<div class="commentBadge__title">\n  <!-- TODO When sound model will be included in comment we don\'t need this -->\n  '+u((n(61)||t&&t.$view||l).call(o,n(477),{name:"$view",hash:{resource_id:null!=t?t.track_id:t},data:r}))+'\n</div>\n<div class="commentBadge__body'+(null!=(s=i.unless.call(o,null!=(s=null!=t?t._options:t)?s.compact:s,{name:"unless",hash:{},fn:e.program(1,r,0),inverse:e.noop,data:r}))?s:"")+'">'+(null!=(s=i["if"].call(o,null!=(s=null!=t?t._options:t)?s.compact:s,{name:"if",hash:{},fn:e.program(3,r,0),inverse:e.program(5,r,0),data:r}))?s:"")+'</div>\n<span class="commentBadge__time sc-text-light">\n  '+u((n(61)||t&&t.$view||l).call(o,n(101),{name:"$view",hash:{timestamp:null!=t?t.created_at:t},data:r}))+"\n</span>\n"+(null!=(s=i["if"].call(o,null!=t?t.canDelete:t,{name:"if",hash:{},fn:e.program(7,r,0),inverse:e.noop,data:r}))?s:"")},useData:!0})},669:function(e,t,n){var i=n(21);e.exports=(i["default"]||i).template({1:function(e,t,n,i,a){return'  on <a class="sc-link-light" href="[[href]]">[[title]]</a>\n'},compiler:[7,">= 4.0.0"],main:function(e,t,i,a,r){var s,o=null!=t?t:{},l=i.helperMissing;return"<!-- TODO When sound model will be included in comment we don't need this -->\n"+(null!=(s=(n(60)||t&&t.$t||l).call(o,{name:"$t",hash:{_comment:"This is displayed on user/comments page, where each comment has this phrase, saying on which sound user left a comment",title:null!=t?t.title:t,href:(n(64)||t&&t.$route||l).call(o,"listen",t,{name:"$route",hash:{},data:r})},fn:e.program(1,r,0),inverse:e.noop,data:r}))?s:"")},useData:!0})},672:function(e,t,n){var i=n(21);e.exports=(i["default"]||i).template({compiler:[7,">= 4.0.0"],main:function(e,t,i,a,r){var s,o,l=null!=t?t:{},u=i.helperMissing,c=e.escapeExpression,d="function";return'<button class="featureHeader__closeButton sc-ir" title="'+c((n(60)||t&&t.$t||u).call(l,"Hide this message",{name:"$t",hash:{},data:r}))+'">'+c((n(60)||t&&t.$t||u).call(l,"Hide this message",{name:"$t",hash:{},data:r}))+'</button>\n\n<h2 class="featureHeader__title">'+c((o=null!=(o=i.heading||(null!=t?t.heading:t))?o:u,typeof o===d?o.call(l,{name:"heading",hash:{},data:r}):o))+'</h2>\n<div class="sc-font-light sc-type-large featureHeader__content">\n  <p>'+(null!=(o=null!=(o=i.text||(null!=t?t.text:t))?o:u,s=typeof o===d?o.call(l,{name:"text",hash:{},data:r}):o)?s:"")+"</p>\n</div>\n"},useData:!0})},673:function(e,t,n){var i=n(21);e.exports=(i["default"]||i).template({1:function(e,t,i,a,r){return'    <div class="groupBadge__actions">\n      '+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(211),{name:"$view",hash:{resource_id:null!=t?t.id:t,size:"small"},data:r}))+"\n    </div>\n"},compiler:[7,">= 4.0.0"],main:function(e,t,i,a,r){var s,o=null!=t?t:{},l=i.helperMissing,u=e.escapeExpression;return'<a href="'+u((n(152)||t&&t.$relativeUrl||l).call(o,null!=t?t.permalink_url:t,{name:"$relativeUrl",hash:{},data:r}))+'" class="groupBadge__coverArt sc-media-image">\n  '+u((n(61)||t&&t.$view||l).call(o,n(78),{name:"$view",hash:{size:50,resource_type:null!=t?t._resource_type:t,resource_id:null!=t?t._resource_id:t},data:r}))+'\n</a>\n<div class="sc-media-content">\n  <div class="groupBadge__title">\n    <h3>\n      <a href="'+u((n(152)||t&&t.$relativeUrl||l).call(o,null!=t?t.permalink_url:t,{name:"$relativeUrl",hash:{},data:r}))+'" class="groupBadge__titleLink sc-link-dark sc-truncate">\n        '+u((n(119)||t&&t.$usertextOneline||l).call(o,null!=t?t.name:t,{name:"$usertextOneline",hash:{maxLength:90,links:!1},data:r}))+'\n      </a>\n    </h3>\n  </div>\n\n  <div class="groupBadge__stats">\n    '+u((n(61)||t&&t.$view||l).call(o,n(215),{name:"$view",hash:{size:"small",resource_id:null!=t?t.id:t},data:r}))+"\n  </div>\n\n"+(null!=(s=i["if"].call(o,null!=t?t.show_join_button:t,{name:"if",hash:{},fn:e.program(1,r,0),inverse:e.noop,data:r}))?s:"")+"</div>\n"},useData:!0})},706:function(e,t,n){var i=n(21);e.exports=(i["default"]||i).template({1:function(e,t,i,a,r){var s;return"  "+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(79),{name:"$view",hash:{resource_type:"playlist",resource_id:null!=(s=null!=t?t.playlist:t)?s.id:s},data:r}))+"\n"},3:function(e,t,i,a,r){var s;return"  "+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(79),{name:"$view",hash:{resource_type:"sound",resource_id:null!=(s=null!=t?t.track:t)?s.id:s},data:r}))+"\n"},compiler:[7,">= 4.0.0"],main:function(e,t,n,i,a){var r;return(null!=(r=n["if"].call(null!=t?t:{},null!=t?t.playlist:t,{name:"if",hash:{},fn:e.program(1,a,0),inverse:e.program(3,a,0),data:a}))?r:"")+"\n"},useData:!0})},732:function(e,t,n){var i=n(560);"string"==typeof i&&(i=[[e.id,i,""]]);n(7)(i,{})},736:function(e,t,n){var i=n(562);"string"==typeof i&&(i=[[e.id,i,""]]);n(7)(i,{})},737:function(e,t,n){var i=n(563);"string"==typeof i&&(i=[[e.id,i,""]]);n(7)(i,{})},738:function(e,t,n){var i=n(564);"string"==typeof i&&(i=[[e.id,i,""]]);n(7)(i,{})},1141:function(e,t,n){"use strict";var i=n(22),a=n(131),r=n(23),s=n(111),o=n(350),l=n(65),u=n(63),c=n(67);e.exports=o.extend({topHeight:174,tracking:{pageName:function(){var e=this.args,t=e.subpage,n=i.get("me").hasPermalink(e.userPermalink);return(n?"you":"users")+":"+("sets"===t?"playlists":t)},pageUrn:function(){return this.user.getUrn()}},setup:function(e){var t=this,i=e.userPermalink,o=e.subpage,d=l.defer();return c.resolve(i).done(function(e){var i={resource_id:e.id,subpage:o},a={resource_id:e.id,subpage:o},s=e.get("username"),l={likes:u.t("[[[username]]]’s likes",{username:s}),followers:u.t("[[[username]]]’s followers",{username:s}),following:u.t("[[[username]]]’s following",{username:s}),comments:u.t("[[[username]]]’s comments",{username:s}),sets:u.t("[[[username]]]’s playlists",{username:s}),groups:u.t("[[[username]]]’s groups",{username:s}),tracks:u.t("[[[username]]]’s tracks",{username:s})};t.user=e,t.setTitle(l[o]),t.setViews({"l-top":[n(1566),i],"l-main":[n(1568),a]}).done(d.resolve).done(function(){r.trigger("tracking:userLayout",{user:e,subpage:o})})}).fail(d.reject).fail(s.ajaxFatal(a.USER_NOT_FOUND)),d}})},1565:function(e,t,n){"use strict";var i=n(400),a=n(84);e.exports=a.extend({Subview:n(474),css:n(2771),className:"userNetworkCommentsList",itemClassName:"userNetworkComments__item sc-border-light-top",defaults:{compact:!0},setup:function(){this.collection=new i(null,{limit:50,userId:this.options.resource_id})},getSubviewArgs:function(e){var t=a.prototype.getSubviewArgs.call(this,e);return t.compact=this.options.compact,t},LoadingView:null})},1566:function(e,t,n){"use strict";var i=n(67),a=n(62);e.exports=a.extend({className:"userNetworkInfo sc-browsers-enable-gpu",template:n(2421),css:n(2772),ModelClass:i,defaults:{subpage:null},requiredAttributes:["username","permalink"]})},1567:function(e,t,n){"use strict";var i=n(63),a=n(364),r=n(67);e.exports=a.extend({className:"userNetworkTabs g-tabs g-tabs-medium",ModelClass:r,requiredAttributes:["permalink","comments_count","followers_count"],routeName:"userNetwork",getTabs:function(e){var t=[{subpage:"likes",text:i.t("Likes")},{subpage:"following",text:i.t("Following")},{subpage:"followers",countable_attribute:"followers_count",text:i.t("Followers"),always_visible:!1,hide_count:!0},{subpage:"comments",countable_attribute:"comments_count",text:i.t("Comments"),always_visible:!1,hide_count:!0},{subpage:"groups",text:i.t("Groups")}];return t}})},1568:function(e,t,n){"use strict";function i(e,t){var n="followers"===t,i=e.is_current_user,a={emptyPageClass:"emptyUsers"};return n?a.message=i?r.t("No one is following you yet."):r.t("No one is following [[username]] yet",{username:this.model.get("username")}):i?(a.message=r.t("You aren’t following anyone yet."),a.linkUrl=o.getRoute("people"),a.linkText=r.t("Find people to follow")):a.message=r.t("[[username]] isn’t following anyone.",{username:this.model.get("username")}),d.bind(null,a)}var a=n(22),r=n(63),s=n(68),o=n(70),l=n(231),u=n(67),c=n(62),d=n(117);e.exports=c.extend(s.withOptions("userNetwork"),{className:"userNetwork",template:n(2422),css:[n(2773),n(118)],ModelClass:u,requiredAttributes:["username"],element2selector:{title:".userNetworkTop__title"},states:{hasButtons:"hasButtons"},defaults:{subpage:null},getTemplateData:function(e){var t=e._options.subpage;switch(e["is_"+t]=!0,e.is_current_user=this.model===a.get("me"),t){case"likes":e.UserLikes=l,this.toggleState("hasButtons",!0);break;case"followers":e.emptyTemplate=i.call(this,e,"followers");break;case"following":e.emptyTemplate=i.call(this,e,"followings")}return e}})},1929:function(e,t,n){t=e.exports=n(6)(),t.push([e.id,".userNetworkCommentsList{margin-top:-6px}.userNetworkComments__item{min-height:40px;padding:10px 0}.userNetworkComments__item:first-child{border-top:0}.userNetworkComments__item .commentBadge__body{font-size:14px;margin-top:1px}.userNetworkComments__item .commentBadge__title{min-height:18px}",""])},1930:function(e,t,n){t=e.exports=n(6)(),t.push([e.id,".userNetworkTop__title{margin-top:0}.userNetworkInfo .userAvatarBadge{float:left;margin:0 20px 10px 0}.userNetworkInfo .userNetworkTabs{clear:both}",""])},1931:function(e,t,n){t=e.exports=n(6)(),t.push([e.id,".userNetwork{margin-top:20px}.userNetwork__subheadlineWrapper{margin-top:-6px}.userNetwork__subheadline{float:left;margin-bottom:25px}.userNetwork__likeActions{float:right;margin-top:1px}.userNetwork__shuffle{display:inline-block;vertical-align:top;margin-top:-3px}.userNetwork__share{display:inline-block}.userNetwork__featureHeader{margin-top:10px}@media (max-width:1239px){.userNetworkTop__inner{width:920px}.userNetwork.hasButtons .g-tabs-link>.g-tabs-icon,.userNetwork.hasButtons .g-tabs-link>b{display:none}}@media (max-width:1079px){.userNetworkTop__inner{width:830px}}@media (max-width:900px){.userNetworkTabs__link{padding-left:10px;padding-right:10px}}",""])},2421:function(e,t,n){var i=n(21);e.exports=(i["default"]||i).template({compiler:[7,">= 4.0.0"],main:function(e,t,i,a,r){var s,o,l=null!=t?t:{},u=i.helperMissing,c=e.escapeExpression;return c((n(61)||t&&t.$view||u).call(l,n(126),{name:"$view",hash:{size:"large",resource_id:null!=t?t.id:t},data:r}))+'\n\n<h1 class="userNetworkTop__title sc-truncate">\n  <a href="'+c((n(64)||t&&t.$route||u).call(l,"user",t,{name:"$route",hash:{},data:r}))+'" class="sc-link-dark">\n    '+c((o=null!=(o=i.username||(null!=t?t.username:t))?o:u,"function"==typeof o?o.call(l,{name:"username",hash:{},data:r}):o))+"\n  </a>\n</h1>\n\n"+c((n(61)||t&&t.$view||u).call(l,n(1567),{name:"$view",hash:{subpage:null!=(s=null!=t?t._options:t)?s.subpage:s,resource_id:null!=t?t.id:t},data:r}))+"\n"},useData:!0})},2422:function(e,t,n){var i=n(21);e.exports=(i["default"]||i).template({1:function(e,t,i,a,r){return"  "+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(172),{name:"$view",hash:{pageSize:12,limit:12,emptyTemplate:null!=t?t.emptyTemplate:t,type:"followings",resource_type:null!=t?t._resource_type:t,resource_id:null!=t?t._resource_id:t},data:r}))+"\n"},3:function(e,t,i,a,r){return"  "+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(172),{name:"$view",hash:{pageSize:12,limit:12,emptyTemplate:null!=t?t.emptyTemplate:t,type:"followers",resource_type:null!=t?t._resource_type:t,resource_id:null!=t?t._resource_id:t},data:r}))+"\n"},5:function(e,t,i,a,r){var s,o=null!=t?t:{},l=i.helperMissing,u=e.escapeExpression;return'  <div class="userNetwork__subheadlineWrapper sc-clearfix">\n    <h2 class="userNetwork__subheadline sc-type-light sc-type-medium">\n'+(null!=(s=i["if"].call(o,null!=t?t.is_current_user:t,{name:"if",hash:{},fn:e.program(6,r,0),inverse:e.program(8,r,0),data:r}))?s:"")+'    </h2>\n    <div class="userNetwork__likeActions">\n      <span class="userNetwork__shuffle">\n        '+u((n(61)||t&&t.$view||l).call(o,n(473),{name:"$view",hash:{resource_id:null!=t?t.id:t,Collection:null!=t?t.UserLikes:t},data:r}))+'\n      </span>\n      <span class="userNetwork__share">\n        '+u((n(61)||t&&t.$view||l).call(o,n(248),{name:"$view",hash:{share_type:"likes",resource_type:null!=t?t._resource_type:t,resource_id:null!=t?t._resource_id:t},data:r}))+"\n      </span>\n    </div>\n  </div>\n"+(null!=(s=i["if"].call(o,null!=t?t.is_current_user:t,{name:"if",hash:{},fn:e.program(10,r,0),inverse:e.noop,data:r}))?s:"")+"  "+u((n(61)||t&&t.$view||l).call(o,n(539),{name:"$view",hash:{resource_id:null!=t?t.id:t},data:r}))+"\n"},6:function(e,t,i,a,r){return"        "+e.escapeExpression((n(60)||t&&t.$t||i.helperMissing).call(null!=t?t:{},"Hear the tracks you’ve liked",{name:"$t",hash:{},data:r}))+"\n"},8:function(e,t,i,a,r){return"        "+e.escapeExpression((n(60)||t&&t.$t||i.helperMissing).call(null!=t?t:{},"Hear the tracks [[username]] has liked",{name:"$t",hash:{username:null!=t?t.username:t},data:r}))+"\n"},10:function(e,t,i,a,r){return'    <div class="userNetwork__featureHeader">\n      '+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(481),{name:"$view",hash:{featureKey:"likesPage"},data:r}))+"\n    </div>\n"},12:function(e,t,i,a,r){return"  "+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(1565),{name:"$view",hash:{compact:!1,resource_id:null!=t?t.id:t},data:r}))+"\n"},14:function(e,t,i,a,r){var s,o=null!=t?t:{};return'  <div class="userNetwork__subheadlineWrapper '+(null!=(s=i["if"].call(o,null!=t?t.is_sets:t,{name:"if",hash:{},fn:e.program(15,r,0),inverse:e.noop,data:r}))?s:"")+' sc-clearfix">\n    <h2 class="userNetwork__subheadline sc-type-light sc-type-medium">\n'+(null!=(s=i["if"].call(o,null!=t?t.is_current_user:t,{name:"if",hash:{},fn:e.program(17,r,0),inverse:e.program(19,r,0),data:r}))?s:"")+"    </h2>\n  </div>\n  "+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(o,n(540),{name:"$view",hash:{resource_id:null!=t?t.id:t},data:r}))+"\n"},15:function(e,t,n,i,a){return"is_sets"},17:function(e,t,i,a,r){return"        "+e.escapeExpression((n(60)||t&&t.$t||i.helperMissing).call(null!=t?t:{},"Hear your playlists",{name:"$t",hash:{},data:r}))+"\n"},19:function(e,t,i,a,r){return"        "+e.escapeExpression((n(60)||t&&t.$t||i.helperMissing).call(null!=t?t:{},"Hear [[username]]’s playlists",{name:"$t",hash:{username:null!=t?t.username:t},data:r}))+"\n"},21:function(e,t,i,a,r){return"  "+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(482),{name:"$view",hash:{showEmptyNetworkPage:!0,subviewName:"user-avatar-badge",size:"xlarge",resource_id:null!=t?t.id:t},data:r}))+"\n"},23:function(e,t,i,a,r){return"  "+e.escapeExpression((n(61)||t&&t.$view||i.helperMissing).call(null!=t?t:{},n(541),{name:"$view",hash:{resource_id:null!=t?t.id:t},data:r}))+"\n"},compiler:[7,">= 4.0.0"],main:function(e,t,n,i,a){var r,s=null!=t?t:{};return(null!=(r=n["if"].call(s,null!=t?t.is_following:t,{name:"if",hash:{},fn:e.program(1,a,0),inverse:e.noop,data:a}))?r:"")+(null!=(r=n["if"].call(s,null!=t?t.is_followers:t,{name:"if",hash:{},fn:e.program(3,a,0),inverse:e.noop,data:a}))?r:"")+(null!=(r=n["if"].call(s,null!=t?t.is_likes:t,{
name:"if",hash:{},fn:e.program(5,a,0),inverse:e.noop,data:a}))?r:"")+(null!=(r=n["if"].call(s,null!=t?t.is_comments:t,{name:"if",hash:{},fn:e.program(12,a,0),inverse:e.noop,data:a}))?r:"")+(null!=(r=n["if"].call(s,null!=t?t.is_sets:t,{name:"if",hash:{},fn:e.program(14,a,0),inverse:e.noop,data:a}))?r:"")+(null!=(r=n["if"].call(s,null!=t?t.is_groups:t,{name:"if",hash:{},fn:e.program(21,a,0),inverse:e.noop,data:a}))?r:"")+(null!=(r=n["if"].call(s,null!=t?t.is_tracks:t,{name:"if",hash:{},fn:e.program(23,a,0),inverse:e.noop,data:a}))?r:"")},useData:!0})},2771:function(e,t,n){var i=n(1929);"string"==typeof i&&(i=[[e.id,i,""]]);n(7)(i,{})},2772:function(e,t,n){var i=n(1930);"string"==typeof i&&(i=[[e.id,i,""]]);n(7)(i,{})},2773:function(e,t,n){var i=n(1931);"string"==typeof i&&(i=[[e.id,i,""]]);n(7)(i,{})}});