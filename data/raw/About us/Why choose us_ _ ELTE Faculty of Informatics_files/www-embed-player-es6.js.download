(function(){'use strict';var r,ba=typeof Object.create=="function"?Object.create:function(a){function b(){}
b.prototype=a;return new b},ca=typeof Object.defineProperties=="function"?Object.defineProperty:function(a,b,c){if(a==Array.prototype||a==Object.prototype)return a;
a[b]=c.value;return a},da=globalThis;
function ea(a,b){if(b)a:{var c=da;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&ca(c,a,{configurable:!0,writable:!0,value:b})}}
var fa=Object.setPrototypeOf;function ha(a,b){a.prototype=ba(b.prototype);a.prototype.constructor=a;fa(a,b);a.Ea=b.prototype}
ea("Symbol.dispose",function(a){return a?a:Symbol("Symbol.dispose")});
ea("SuppressedError",function(a){function b(c,d,e){if(!(this instanceof b))return new b(c,d,e);e=Error(e);"stack"in e&&(this.stack=e.stack);this.message=e.message;this.error=c;this.suppressed=d}
if(a)return a;ha(b,Error);b.prototype.name="SuppressedError";return b});/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ia=ia||{},t=this||self;function v(a,b,c){a=a.split(".");c=c||t;for(var d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b}
function ja(a,b){var c=w("CLOSURE_FLAGS");a=c&&c[a];return a!=null?a:b}
function w(a,b){a=a.split(".");b=b||t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b}
function ka(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"}
function la(a){var b=ka(a);return b=="array"||b=="object"&&typeof a.length=="number"}
function ma(a){var b=typeof a;return b=="object"&&a!=null||b=="function"}
function na(a){return Object.prototype.hasOwnProperty.call(a,oa)&&a[oa]||(a[oa]=++pa)}
var oa="closure_uid_"+(Math.random()*1E9>>>0),pa=0;function qa(a,b,c){return a.call.apply(a.bind,arguments)}
function ra(a,b,c){ra=qa;return ra.apply(null,arguments)}
function sa(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}}
function ta(){return Date.now()}
function ua(a){return a}
function va(a,b){function c(){}
c.prototype=b.prototype;a.Ea=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.base=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}}
;function wa(a,...b){b=b.filter(Boolean).join("&");if(!b)return a;const c=a.match(/[?&]adurl=/);return c?a.slice(0,c.index+1)+b+"&"+a.slice(c.index+1):a+(a.indexOf("?")<0?"?":"&")+b}
function xa(a,b){return b?"&"+a+"="+encodeURIComponent(b):""}
function ya(a){a=a.o;if(!a)return"";let b=xa("uap",a.platform)+xa("uapv",a.platformVersion)+xa("uafv",a.uaFullVersion)+xa("uaa",a.architecture)+xa("uam",a.model)+xa("uab",a.bitness);a.fullVersionList&&(b+="&uafvl="+encodeURIComponent(a.fullVersionList.map(c=>encodeURIComponent(c.brand)+";"+encodeURIComponent(c.version)).join("|")));
a.wow64!=null&&(b+="&uaw="+Number(a.wow64));return b.slice(1)}
var za=class{constructor({url:a,Li:b}){this.i=a;this.o=b;this.j=(new Date).getTime()-17040672E5;this.h={};const c=/[?&]([^&=]+)=([^&]*)/g;for(;b=c.exec(a);)this.h[b[1]]=b[2]}};function Aa(a,b){if(b!==null&&b!==void 0){if(typeof b!=="object"&&typeof b!=="function")throw new TypeError("Object expected.");if(c===void 0){if(!Symbol.dispose)throw new TypeError("Symbol.dispose is not defined.");var c=b[Symbol.dispose]}if(typeof c!=="function")throw new TypeError("Object not disposable.");a.stack.push({value:b,dispose:c,async:!1})}return b}
function Ba(a){function b(f){a.error=a.jb?new SuppressedError(f,a.error,"An error was suppressed during disposal."):f;a.jb=!0}
function c(){for(;d=a.stack.pop();)try{if(!d.async&&e===1)return e=0,a.stack.push(d),Promise.resolve().then(c);if(d.dispose){var f=d.dispose.call(d.value);if(d.async)return e|=2,Promise.resolve(f).then(c,function(g){b(g);return c()})}else e|=1}catch(g){b(g)}if(e===1)return a.jb?Promise.reject(a.error):Promise.resolve();
if(a.jb)throw a.error;}
var d,e=0;c()}
;function Ca(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,Ca);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)}
va(Ca,Error);Ca.prototype.name="CustomError";/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
let Da=globalThis.trustedTypes,Ea;function Fa(){let a=null;if(!Da)return a;try{const b=c=>c;
a=Da.createPolicy("goog#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a}
function Ga(){Ea===void 0&&(Ea=Fa());return Ea}
;var Ha=class{constructor(a){this.h=a}toString(){return this.h+""}};function Ia(a){const b=Ga();a=b?b.createScriptURL(a):a;return new Ha(a)}
function Ja(a){if(a instanceof Ha)return a.h;throw Error("");}
;function Ka(a){return a.toString().indexOf("`")===-1}
Ka(a=>a``)||Ka(a=>a`\0`)||Ka(a=>a`\n`)||Ka(a=>a`\u0000`);var La=class{constructor(a){this.h=a}toString(){return this.h}},Ma=new La("about:invalid#zClosurez");class Na{constructor(a){this.Ze=a}}function Oa(a){return new Na(b=>b.substr(0,a.length+1).toLowerCase()===a+":")}
const Pa=[Oa("data"),Oa("http"),Oa("https"),Oa("mailto"),Oa("ftp"),new Na(a=>/^[^:]*([/?#]|$)/.test(a))];
function Qa(a,b=Pa){if(a instanceof La)return a;for(let c=0;c<b.length;++c){const d=b[c];if(d instanceof Na&&d.Ze(a))return new La(a)}}
var Ra=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;function Sa(a){if(a instanceof La)if(a instanceof La)a=a.h;else throw Error("");else a=Ra.test(a)?a:void 0;return a}
;function Ta(a,b){b=Sa(b);b!==void 0&&(a.href=b)}
;function Ua(a,b=`unexpected value ${a}!`){throw Error(b);}
;var Va=class{constructor(a){this.h=a}toString(){return this.h+""}};function Wa(a=document){a=a.querySelector?.("script[nonce]");return a==null?"":a.nonce||a.getAttribute("nonce")||""}
;var Xa=class{constructor(a){this.h=a}toString(){return this.h+""}};function Ya(a){const b=Ga();a=b?b.createScript(a):a;return new Xa(a)}
function Za(a){if(a instanceof Xa)return a.h;throw Error("");}
;function $a(a){const b=Wa(a.ownerDocument);b&&a.setAttribute("nonce",b)}
function ab(a,b){a.src=Ja(b);$a(a)}
;var bb=class{constructor(a){this.h=a}toString(){return this.h}};function cb(a){var b="true".toString(),c=[db`data-`];if(c.length===0)throw Error("");if(c.map(d=>{if(d instanceof bb)d=d.h;else throw Error("");return d}).every(d=>"data-loaded".indexOf(d)!==0))throw Error('Attribute "data-loaded" does not match any of the allowed prefixes.');
a.setAttribute("data-loaded",b)}
;const eb="alternate author bookmark canonical cite help icon license modulepreload next prefetch dns-prefetch prerender preconnect preload prev search subresource".split(" ");function fb(a,b){if(b instanceof Ha)a.href=Ja(b).toString(),a.rel="stylesheet";else{if(eb.indexOf("stylesheet")===-1)throw Error('TrustedResourceUrl href attribute required with rel="stylesheet"');b=Sa(b);b!==void 0&&(a.href=b,a.rel="stylesheet")}}
;function gb(a,b){return Array.prototype.indexOf.call(a,b,void 0)}
function hb(a,b){Array.prototype.forEach.call(a,b,void 0)}
function ib(a,b){return Array.prototype.filter.call(a,b,void 0)}
function jb(a,b){return Array.prototype.map.call(a,b,void 0)}
function kb(a,b){return Array.prototype.reduce.call(a,b,{duration:0})}
function lb(a,b){a:{const c=a.length,d=typeof a==="string"?a.split(""):a;for(let e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){b=e;break a}b=-1}return b<0?null:typeof a==="string"?a.charAt(b):a[b]}
function mb(a,b){b=gb(a,b);let c;(c=b>=0)&&Array.prototype.splice.call(a,b,1);return c}
function nb(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]}
function ob(a,b){for(let c=1;c<arguments.length;c++){const d=arguments[c];if(la(d)){const e=a.length||0,f=d.length||0;a.length=e+f;for(let g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
function pb(a,b){return a>b?1:a<b?-1:0}
;function qb(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b}
;function rb(a){var b=w("window.location.href");a==null&&(a='Unknown Error of type "null/undefined"');if(typeof a==="string")return{message:a,name:"Unknown error",lineNumber:"Not available",fileName:b,stack:"Not available"};let c,d;var e=!1;try{c=a.lineNumber||a.line||"Not available"}catch(f){c="Not available",e=!0}try{d=a.fileName||a.filename||a.sourceURL||t.$googDebugFname||b}catch(f){d="Not available",e=!0}b=sb(a);if(!(!e&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name)){e=a.message;if(e==
null){if(a.constructor&&a.constructor instanceof Function){if(a.constructor.name)e=a.constructor.name;else if(e=a.constructor,tb[e])e=tb[e];else{e=String(e);if(!tb[e]){const f=/function\s+([^\(]+)/m.exec(e);tb[e]=f?f[1]:"[Anonymous]"}e=tb[e]}e='Unknown Error of type "'+e+'"'}else e="Unknown Error of unknown type";typeof a.toString==="function"&&Object.prototype.toString!==a.toString&&(e+=": "+a.toString())}return{message:e,name:a.name||"UnknownError",lineNumber:c,fileName:d,stack:b||"Not available"}}return{message:a.message,
name:a.name,lineNumber:a.lineNumber,fileName:a.fileName,stack:b}}
function sb(a,b){b||(b={});b[ub(a)]=!0;let c=a.stack||"";var d=a.cause;d&&!b[ub(d)]&&(c+="\nCaused by: ",d.stack&&d.stack.indexOf(d.toString())==0||(c+=typeof d==="string"?d:d.message+"\n"),c+=sb(d,b));a=a.errors;if(Array.isArray(a)){d=1;let e;for(e=0;e<a.length&&!(d>4);e++)b[ub(a[e])]||(c+="\nInner error "+d++ +": ",a[e].stack&&a[e].stack.indexOf(a[e].toString())==0||(c+=typeof a[e]==="string"?a[e]:a[e].message+"\n"),c+=sb(a[e],b));e<a.length&&(c+="\n... "+(a.length-e)+" more inner errors")}return c}
function ub(a){let b="";typeof a.toString==="function"&&(b=""+a);return b+a.stack}
var tb={};function vb(a){return decodeURIComponent(a.replace(/\+/g," "))}
function wb(a){let b=0;for(let c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;const xb=RegExp("^(?:([^:/?#.]+):)?(?://(?:([^\\\\/?#]*)@)?([^\\\\/?#]*?)(?::([0-9]+))?(?=[\\\\/?#]|$))?([^?#]+)?(?:\\?([^#]*))?(?:#([\\s\\S]*))?$");function yb(a){return a?decodeURI(a):a}
function zb(a){return yb(a.match(xb)[3]||null)}
function Ab(a){return yb(a.match(xb)[5]||null)}
function Bb(a){var b=a.match(xb);a=b[5];var c=b[6];b=b[7];let d="";a&&(d+=a);c&&(d+="?"+c);b&&(d+="#"+b);return d}
function Cb(a){const b=a.indexOf("#");return b<0?a:a.slice(0,b)}
function Db(a,b){if(a){a=a.split("&");for(let c=0;c<a.length;c++){const d=a[c].indexOf("=");let e,f=null;d>=0?(e=a[c].substring(0,d),f=a[c].substring(d+1)):e=a[c];b(e,f?vb(f):"")}}}
function Eb(a,b,c){if(Array.isArray(b))for(let d=0;d<b.length;d++)Eb(a,String(b[d]),c);else b!=null&&c.push(a+(b===""?"":"="+encodeURIComponent(String(b))))}
function Fb(a){const b=[];for(const c in a)Eb(c,a[c],b);return b.join("&")}
function Gb(a,b){b=Fb(b);if(b){var c=a.indexOf("#");c<0&&(c=a.length);let d=a.indexOf("?"),e;d<0||d>c?(d=c,e=""):e=a.substring(d+1,c);a=[a.slice(0,d),e,a.slice(c)];c=a[1];a[1]=b?c?c+"&"+b:b:c;b=a[0]+(a[1]?"?"+a[1]:"")+a[2]}else b=a;return b}
function Hb(a,b,c,d){const e=c.length;for(;(b=a.indexOf(c,b))>=0&&b<d;){var f=a.charCodeAt(b-1);if(f==38||f==63)if(f=a.charCodeAt(b+e),!f||f==61||f==38||f==35)return b;b+=e+1}return-1}
const Ib=/#|$/,Jb=/[?&]($|#)/;function Kb(a,b){const c=a.search(Ib);let d=0,e;const f=[];for(;(e=Hb(a,d,b,c))>=0;)f.push(a.substring(d,e)),d=Math.min(a.indexOf("&",e)+1||c,c);f.push(a.slice(d));return f.join("").replace(Jb,"$1")}
;function Lb(){try{return!!window?.top?.location.href&&!1}catch(a){return!0}}
;var x=class extends Error{constructor(a,b,c=Error()){super();this.code=a;b+=":";c instanceof Error?(this.message=b+c.message,this.stack=c.stack||""):(this.message=b+String(c),this.stack="");Object.setPrototypeOf(this,new.target.prototype)}};function Mb(a){a&&typeof a.dispose=="function"&&a.dispose()}
;function Nb(a){for(let b=0,c=arguments.length;b<c;++b){const d=arguments[b];la(d)?Nb.apply(null,d):Mb(d)}}
;function y(){this.I=this.I;this.H=this.H}
y.prototype.I=!1;y.prototype.dispose=function(){this.I||(this.I=!0,this.ba())};
y.prototype[Symbol.dispose]=function(){this.dispose()};
function Ob(a,b){a.addOnDisposeCallback(sa(Mb,b))}
y.prototype.addOnDisposeCallback=function(a,b){this.I?b!==void 0?a.call(b):a():(this.H||(this.H=[]),b&&(a=a.bind(b)),this.H.push(a))};
y.prototype.ba=function(){if(this.H)for(;this.H.length;)this.H.shift()()};function Pb(a="bevasrsg"){return new Promise(b=>{const c=window===window.top?window:Lb()?window:window.top;let d=c[a];d?.bevasrs?b(new Qb(d.bevasrs)):(d||(d={nqfbel:[]},c[a]=d),d.nqfbel.push(e=>{b(new Qb(e))}))})}
function Rb(a){a.h!==void 0&&(a.i.forEach(b=>{a.h?.removeEventListener(b,a.j)}),a.h=void 0)}
class Qb extends y{constructor(a){super();this.vm=a;this.i="keydown keypress keyup input focusin focusout select copy cut paste change click dblclick auxclick pointerover pointerdown pointerup pointermove pointerout dragenter dragleave drag dragend mouseover mousedown mouseup mousemove mouseout touchstart touchend touchmove wheel".split(" ");this.h=void 0;this.Kb=this.vm.p;this.j=this.Xb.bind(this);this.addOnDisposeCallback(()=>void Rb(this))}snapshot(a){return this.vm.s({...(a.Ka&&{c:a.Ka}),
...(a.Ic&&{s:a.Ic}),...(a.gd!==void 0&&{p:a.gd})})}Xb(a){this.vm.e(a)}kc(a,b){return this.vm.c(a,b,!1)}cc(){return this.vm.l()}};function Sb(a){const b={Ka:a.c,Pc:a.e,jf:a.mc??!1,kf:a.me??!1};a.co&&(b.hc={od:a.co.c,je:a.co.a,Df:a.co.s});return b}
function Tb(a){return async()=>{const b=await a();return{f:()=>b.Jb.promise,
c:c=>{if(c>150)var d=!1;else try{b.cache=new Ub(c,b.logger),d=!0}catch(e){Vb(b,new x(22,"GBJ:init",e)),d=!1}return d},
m:c=>b.eb(Sb(c)),
mws:c=>b.yc(Sb(c))}}}
function Wb(a,b,c="bevasrsg"){b={s:f=>a.snapshot({...(f.c&&{Ka:f.c}),...(f.s&&{Ic:f.s}),Ji:f.p??!0}),
e:f=>void a.Xb?.(f),
c:(f,g)=>a.kc(f,g),
p:a.Kb,l:()=>a.cc(),
wpc:b?Tb(b):void 0};const d=window===window.top?window:Lb()?window:window.top;let e=d[c];if(e){e.bevasrs=b;if(e.nqfbel!==void 0)for(const f of e.nqfbel)f(b);e.nqfbel=void 0}else e={bevasrs:b,nqfbel:void 0},d[c]=e}
;function Xb(a){const b=[];Yb(a,Zb,6).forEach(c=>{$b(c,2)<=53&&b.push($b(c,1))});
return b}
function ac(a){const b=[];Yb(a,Zb,6).forEach(c=>{$b(c,2)>53&&b.push($b(c,1))});
return b}
;function bc(a){a.then(()=>{},()=>{})}
var cc=class extends y{constructor(){super(...arguments);this.Z=1}share(){if(this.I)throw Error("E:AD");this.Z++;return this}dispose(){--this.Z||super.dispose()}};function dc(a){return{fieldType:2,fieldName:a}}
function A(a){return{fieldType:3,fieldName:a}}
;var fc=class{constructor(a){this.h=a;ec(a,"/client_streamz/bg/frs",A("mk"))}record(a,b){this.h.record("/client_streamz/bg/frs",a,b)}},hc=class{constructor(a){this.h=a;ec(a,"/client_streamz/bg/wrl",A("mn"),dc("ac"),dc("sc"),A("rk"),A("mk"))}record(a,b,c,d,e,f){this.h.record("/client_streamz/bg/wrl",a,b,c,d,e,f)}},kc=class{constructor(a){this.i=a;ic(a,"/client_streamz/bg/ec",A("en"),A("mk"))}h(a,b){jc(this.i,"/client_streamz/bg/ec",[a,b])}},lc=class{constructor(a){this.h=a;ec(a,"/client_streamz/bg/el",
A("en"),A("mk"))}record(a,b,c){this.h.record("/client_streamz/bg/el",a,b,c)}},mc=class{constructor(a){this.i=a;ic(a,"/client_streamz/bg/cec",dc("ec"),A("mk"))}h(a,b){jc(this.i,"/client_streamz/bg/cec",[a,b])}},nc=class{constructor(a){this.i=a;ic(a,"/client_streamz/bg/po/csc",dc("cs"),A("mk"))}h(a,b){jc(this.i,"/client_streamz/bg/po/csc",[a,b])}},oc=class{constructor(a){this.i=a;ic(a,"/client_streamz/bg/po/ctav",A("av"),A("mk"))}h(a,b){jc(this.i,"/client_streamz/bg/po/ctav",[a,b])}},pc=class{constructor(a){this.i=
a;ic(a,"/client_streamz/bg/po/cwsc",A("su"),A("mk"))}h(a,b){jc(this.i,"/client_streamz/bg/po/cwsc",[a,b])}},qc=class{constructor(a){this.h=a;ec(a,"/client_streamz/bg/od/p",A("mk"))}record(a,b){this.h.record("/client_streamz/bg/od/p",a,b)}},rc=class{constructor(a){this.h=a;ec(a,"/client_streamz/bg/od/n",A("et"),A("mk"))}record(a,b,c){this.h.record("/client_streamz/bg/od/n",a,b,c)}};let sc;function tc(a){return(sc||(sc=new TextEncoder)).encode(a)}
;function uc(a){t.setTimeout(()=>{throw a;},0)}
;function vc(a){const b=[];let c=0;for(let d=0;d<a.length;d++){let e=a.charCodeAt(d);e<128?b[c++]=e:(e<2048?b[c++]=e>>6|192:((e&64512)==55296&&d+1<a.length&&(a.charCodeAt(d+1)&64512)==56320?(e=65536+((e&1023)<<10)+(a.charCodeAt(++d)&1023),b[c++]=e>>18|240,b[c++]=e>>12&63|128):b[c++]=e>>12|224,b[c++]=e>>6&63|128),b[c++]=e&63|128)}return b}
;var wc=ja(610401301,!1),xc=ja(748402147,!0),yc=ja(824656860,!0);function zc(){var a=t.navigator;return a&&(a=a.userAgent)?a:""}
var Ac;const Bc=t.navigator;Ac=Bc?Bc.userAgentData||null:null;function Cc(a){if(!wc||!Ac)return!1;for(let b=0;b<Ac.brands.length;b++){const {brand:c}=Ac.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1}
function C(a){return zc().indexOf(a)!=-1}
;function Dc(){return wc?!!Ac&&Ac.brands.length>0:!1}
function Ec(){return Dc()?!1:C("Opera")}
function Fc(){return C("Firefox")||C("FxiOS")}
function Gc(){return Dc()?Cc("Chromium"):(C("Chrome")||C("CriOS"))&&!(Dc()?0:C("Edge"))||C("Silk")}
;function Hc(){return wc?!!Ac&&!!Ac.platform:!1}
function Ic(){return C("iPhone")&&!C("iPod")&&!C("iPad")}
;function Jc(a){Jc[" "](a);return a}
Jc[" "]=function(){};var Kc=Ec(),Lc=Dc()?!1:C("Trident")||C("MSIE"),Mc=C("Edge"),Nc=C("Gecko")&&!(zc().toLowerCase().indexOf("webkit")!=-1&&!C("Edge"))&&!(C("Trident")||C("MSIE"))&&!C("Edge"),Oc=zc().toLowerCase().indexOf("webkit")!=-1&&!C("Edge");Oc&&C("Mobile");Hc()||C("Macintosh");Hc()||C("Windows");(Hc()?Ac.platform==="Linux":C("Linux"))||Hc()||C("CrOS");var Pc=Hc()?Ac.platform==="Android":C("Android");Ic();C("iPad");C("iPod");Ic()||C("iPad")||C("iPod");zc().toLowerCase().indexOf("kaios");Fc();const Qc=Ic()||C("iPod"),Rc=C("iPad");!C("Android")||Gc()||Fc()||Ec()||C("Silk");Gc();const Sc=C("Safari")&&!(Gc()||(Dc()?0:C("Coast"))||Ec()||(Dc()?0:C("Edge"))||(Dc()?Cc("Microsoft Edge"):C("Edg/"))||(Dc()?Cc("Opera"):C("OPR"))||Fc()||C("Silk")||C("Android"))&&!(Ic()||C("iPad")||C("iPod"));const Tc={};let Uc=null;function Vc(a,b){la(a);b===void 0&&(b=0);Wc();b=Tc[b];const c=Array(Math.floor(a.length/3)),d=b[64]||"";let e=0,f=0;for(;e<a.length-2;e+=3){var g=a[e],h=a[e+1],k=a[e+2],l=b[g>>2];g=b[(g&3)<<4|h>>4];h=b[(h&15)<<2|k>>6];k=b[k&63];c[f++]=""+l+g+h+k}l=0;k=d;switch(a.length-e){case 2:l=a[e+1],k=b[(l&15)<<2]||d;case 1:a=a[e],c[f]=""+b[a>>2]+b[(a&3)<<4|l>>4]+k+d}return c.join("")}
function Xc(a){const b=a.length;let c=b*3/4;c%3?c=Math.floor(c):"=.".indexOf(a[b-1])!=-1&&(c="=.".indexOf(a[b-2])!=-1?c-2:c-1);const d=new Uint8Array(c);let e=0;Yc(a,function(f){d[e++]=f});
return e!==c?d.subarray(0,e):d}
function Yc(a,b){function c(e){for(;d<a.length;){const f=a.charAt(d++),g=Uc[f];if(g!=null)return g;if(!/^[\s\xa0]*$/.test(f))throw Error("Unknown base64 encoding at char: "+f);}return e}
Wc();let d=0;for(;;){const e=c(-1),f=c(0),g=c(64),h=c(64);if(h===64&&e===-1)break;b(e<<2|f>>4);g!=64&&(b(f<<4&240|g>>2),h!=64&&b(g<<6&192|h))}}
function Wc(){if(!Uc){Uc={};var a="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789".split(""),b=["+/=","+/","-_=","-_.","-_"];for(let c=0;c<5;c++){const d=a.concat(b[c].split(""));Tc[c]=d;for(let e=0;e<d.length;e++){const f=d[e];Uc[f]===void 0&&(Uc[f]=e)}}}}
;const Zc=/[-_.]/g,$c={"-":"+",_:"/",".":"="};function ad(a){return $c[a]||""}
var bd={};function cd(){return dd||(dd=new ed(null,bd))}
function fd(a){gd(bd);var b=a.h;if(!(b==null||b!=null&&b instanceof Uint8Array))if(typeof b==="string"){b=Zc.test(b)?b.replace(Zc,ad):b;b=atob(b);const c=new Uint8Array(b.length);for(let d=0;d<b.length;d++)c[d]=b.charCodeAt(d);b=c}else ka(b),b=null;return b==null?b:a.h=b}
function hd(a){return new Uint8Array(fd(a)||0)}
var ed=class{sizeBytes(){const a=fd(this);return a?a.length:0}constructor(a,b){gd(b);this.h=a;if(a!=null&&a.length===0)throw Error("ByteString should be constructed with non-empty values");}};let dd;function gd(a){if(a!==bd)throw Error("illegal external caller");}
;let id=void 0;function jd(a){a=Error(a);qb(a,"warning");return a}
function kd(a,b){if(a!=null){var c=id??(id={});var d=c[a]||0;d>=b||(c[a]=d+1,a=Error(),qb(a,"incident"),uc(a))}}
;function ld(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()}
var E=ld("jas",!0),md=ld(),nd=ld(),od=ld(),pd=ld(),qd=ld(),rd=ld(),sd=ld("m_m",!0),td=ld(),ud=ld();[...Object.values({Mh:1,Lh:2,Kh:4,Qh:8,Sh:16,Oh:32,Yf:64,Ih:128,eg:256,Rh:512,fg:1024,Jh:2048,Ph:4096,Nh:8192})];var vd;const wd=[];wd[E]=7;vd=Object.freeze(wd);var xd={};function yd(a,b){return b===void 0?a.h!==zd&&!!(2&(a.X[E]|0)):!!(2&b)&&a.h!==zd}
const zd={};function Ad(a,b){if(a!=null)if(typeof a==="string")a=a?new ed(a,bd):cd();else if(a.constructor!==ed)if(a!=null&&a instanceof Uint8Array)a instanceof Uint8Array||Array.isArray(a),a=a.length?new ed(new Uint8Array(a),bd):cd();else{if(!b)throw Error();a=void 0}return a}
var Bd=Object.freeze({});function Cd(a,b,c){const d=b&128?0:-1,e=a.length;var f;if(f=!!e)f=a[e-1],f=f!=null&&typeof f==="object"&&f.constructor===Object;const g=e+(f?-1:0);for(b=b&128?1:0;b<g;b++)c(b-d,a[b]);if(f){a=a[e-1];for(const h in a)!isNaN(h)&&c(+h,a[h])}}
var Dd={};function Ed(a){a.ji=!0;return a}
;var Fd=Ed(a=>typeof a==="number"),Gd=Ed(a=>typeof a==="string");
function Hd(){var a=Id;return Ed(b=>{for(const c in a)if(b===a[c]&&!/^[0-9]+$/.test(c))return!0;return!1})}
var Jd=Ed(a=>a!=null&&typeof a==="object"&&typeof a.then==="function"),Kd=Ed(a=>!!a&&(typeof a==="object"||typeof a==="function"));function Ld(a){if(Gd(a)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(a))throw Error(String(a));}else if(Fd(a)&&!Number.isSafeInteger(a))throw Error(String(a));return BigInt(a)}
var Od=Ed(a=>a>=Md&&a<=Nd);
const Md=BigInt(Number.MIN_SAFE_INTEGER),Nd=BigInt(Number.MAX_SAFE_INTEGER);let Pd=0,Qd=0,Rd;function Sd(a){const b=a>>>0;Pd=b;Qd=(a-b)/4294967296>>>0}
function Td(a){if(a<0){Sd(0-a);a=Pd;var b=Qd;b=~b;a?a=~a+1:b+=1;const [c,d]=[a,b];Pd=c>>>0;Qd=d>>>0}else Sd(a)}
function Ud(a,b){const c=b*4294967296+(a>>>0);return Number.isSafeInteger(c)?c:Vd(a,b)}
function Vd(a,b){b>>>=0;a>>>=0;var c;b<=2097151?c=""+(4294967296*b+a):c=""+(BigInt(b)<<BigInt(32)|BigInt(a));return c}
function Wd(){var a=Pd,b=Qd,c;b&2147483648?c=""+(BigInt(b|0)<<BigInt(32)|BigInt(a>>>0)):c=Vd(a,b);return c}
function Xd(a){a.length<16?Td(Number(a)):(a=BigInt(a),Pd=Number(a&BigInt(4294967295))>>>0,Qd=Number(a>>BigInt(32)&BigInt(4294967295)))}
;const Yd=typeof BigInt==="function"?BigInt.asIntN:void 0,Zd=typeof BigInt==="function"?BigInt.asUintN:void 0,$d=Number.isSafeInteger,ae=Number.isFinite,be=Math.trunc;function ce(a){return a.displayName||a.name||"unknown type name"}
function de(a){if(a!=null&&typeof a!=="boolean")throw Error(`Expected boolean but got ${ka(a)}: ${a}`);return a}
const ee=/^-?([1-9][0-9]*|0)(\.[0-9]+)?$/;function fe(a){switch(typeof a){case "bigint":return!0;case "number":return ae(a);case "string":return ee.test(a);default:return!1}}
function ge(a){if(typeof a!=="number")throw jd("int32");if(!ae(a))throw jd("int32");return a|0}
function he(a){return a==null?a:ge(a)}
function ie(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return ae(a)?a|0:void 0}
function je(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return ae(a)?a>>>0:void 0}
function ke(a){var b=yc?1024:0;if(!fe(a))throw jd("int64");const c=typeof a;switch(b){case 512:switch(c){case "string":return le(a);case "bigint":return String(Yd(64,a));default:return me(a)}case 1024:switch(c){case "string":return ne(a);case "bigint":return Ld(Yd(64,a));default:return oe(a)}case 0:switch(c){case "string":return le(a);case "bigint":return Ld(Yd(64,a));default:return pe(a)}default:return Ua(b,"Unknown format requested type for int64")}}
function qe(a){return a==null?a:ke(a)}
function pe(a){fe(a);a=be(a);if(!$d(a)){Td(a);var b=Pd,c=Qd;if(a=c&2147483648)b=~b+1>>>0,c=~c>>>0,b==0&&(c=c+1>>>0);b=Ud(b,c);a=typeof b==="number"?a?-b:b:a?"-"+b:b}return a}
function me(a){fe(a);a=be(a);$d(a)?a=String(a):(Td(a),a=Wd());return a}
function le(a){fe(a);var b=be(Number(a));if($d(b))return String(b);b=a.indexOf(".");b!==-1&&(a=a.substring(0,b));a.indexOf(".");b=a.length;(a[0]==="-"?b<20||b===20&&a<="-9223372036854775808":b<19||b===19&&a<="9223372036854775807")||(Xd(a),a=Wd());return a}
function ne(a){var b=be(Number(a));if($d(b))return Ld(b);b=a.indexOf(".");b!==-1&&(a=a.substring(0,b));return Ld(Yd(64,BigInt(a)))}
function oe(a){return $d(a)?Ld(pe(a)):Ld(me(a))}
function re(a){if(a==null)return a;if(typeof a==="bigint")return Od(a)?a=Number(a):(a=Yd(64,a),a=Od(a)?Number(a):String(a)),a;if(fe(a))return typeof a==="number"?pe(a):le(a)}
function se(a){const b=typeof a;if(a==null)return a;if(b==="bigint")return Ld(Yd(64,a));if(fe(a))return b==="string"?ne(a):oe(a)}
function te(a){if(a==null)return a;const b=typeof a;if(b==="bigint")return String(Yd(64,a));if(fe(a)){if(b==="string")return le(a);if(b==="number")return pe(a)}}
function ue(a){if(a==null)return a;var b=typeof a;if(b==="bigint")return String(Zd(64,a));if(fe(a)){if(b==="string")return fe(a),b=be(Number(a)),$d(b)&&b>=0?a=String(b):(b=a.indexOf("."),b!==-1&&(a=a.substring(0,b)),a.indexOf("."),a[0]==="-"?b=!1:(b=a.length,b=b<20?!0:b===20&&a<="18446744073709551615"),b||(Xd(a),a=Vd(Pd,Qd))),a;if(b==="number")return fe(a),a=be(a),a>=0&&$d(a)||(Td(a),a=Ud(Pd,Qd)),a}}
function ve(a){if(typeof a!=="string")throw Error();return a}
function we(a){if(a!=null&&typeof a!=="string")throw Error();return a}
function xe(a){return a==null||typeof a==="string"?a:void 0}
function ye(a,b){if(!(a instanceof b))throw Error(`Expected instanceof ${ce(b)} but got ${a&&ce(a.constructor)}`);}
function ze(a,b,c){if(a!=null&&a[sd]===xd)return a;if(Array.isArray(a)){var d=a[E]|0;c=d|c&32|c&2;c!==d&&(a[E]=c);return new b(a)}}
;const Ae={};function Be(a){return a}
;function Ce(a){const b=ua(nd);return b?a[b]:void 0}
const De={Ci:!0};function Ee(a,b){b<100||kd(pd,1)}
;function Fe(a,b,c,d){const e=d!==void 0;d=!!d;var f=ua(nd),g;!e&&f&&(g=a[f])&&g.Oe(Ee);f=[];var h=a.length;let k;g=4294967295;let l=!1;const n=!!(b&64),m=n?b&128?0:-1:void 0;b&1||(k=h&&a[h-1],k!=null&&typeof k==="object"&&k.constructor===Object?(h--,g=h):k=void 0,!n||b&128||e||(l=!0,g=(Ge??Be)(g-m,m,a,k,void 0)+m));b=void 0;for(var u=0;u<h;u++){let p=a[u];if(p!=null&&(p=c(p,d))!=null)if(n&&u>=g){const z=u-m;(b??(b={}))[z]=p}else f[u]=p}if(k)for(let p in k){h=k[p];if(h==null||(h=c(h,d))==null)continue;
u=+p;let z;n&&!Number.isNaN(u)&&(z=u+m)<g?f[z]=h:(b??(b={}))[p]=h}b&&(l?f.push(b):f[g]=b);e&&ua(nd)&&Ce(a);return f}
function He(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return Od(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){var b=a[E]|0;return a.length===0&&b&1?void 0:Fe(a,b,He)}if(a!=null&&a[sd]===xd)return Ie(a);if(a instanceof ed){b=a.h;if(b==null)a="";else if(typeof b==="string")a=b;else{let c="",d=0;const e=b.length-10240;for(;d<e;)c+=String.fromCharCode.apply(null,b.subarray(d,d+=10240));c+=String.fromCharCode.apply(null,d?b.subarray(d):
b);a=a.h=btoa(c)}return a}return}return a}
let Ge;function Je(a,b){if(b){Ge=b==null||b===Be||b[td]!==Ae?Be:b;try{return Ie(a)}finally{Ge=void 0}}return Ie(a)}
function Ie(a){a=a.X;return Fe(a,a[E]|0,He)}
;let Ke,Le;function Me(a){switch(typeof a){case "boolean":return Ke||(Ke=[0,void 0,!0]);case "number":return a>0?void 0:a===0?Le||(Le=[0,void 0]):[-a,void 0];case "string":return[0,a];case "object":return a}}
function Ne(a,b,c,d=0){if(a==null){var e=32;c?(a=[c],e|=128):a=[];b&&(e=e&-16760833|(b&1023)<<14)}else{if(!Array.isArray(a))throw Error("narr");e=a[E]|0;if(xc&&1&e)throw Error("rfarr");2048&e&&!(2&e)&&Oe();if(e&256)throw Error("farr");if(e&64)return(e|d)!==e&&(a[E]=e|d),a;if(c&&(e|=128,c!==a[0]))throw Error("mid");a:{c=a;e|=64;var f=c.length;if(f){var g=f-1;const k=c[g];if(k!=null&&typeof k==="object"&&k.constructor===Object){b=e&128?0:-1;g-=b;if(g>=1024)throw Error("pvtlmt");for(var h in k)if(f=
+h,f<g)c[f+b]=k[h],delete k[h];else break;e=e&-16760833|(g&1023)<<14;break a}}if(b){h=Math.max(b,f-(e&128?0:-1));if(h>1024)throw Error("spvt");e=e&-16760833|(h&1023)<<14}}}a[E]=e|64|d;return a}
function Oe(){if(xc)throw Error("carr");kd(rd,5)}
;function Pe(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){var c=a[E]|0;a.length===0&&c&1?a=void 0:c&2||(!b||4096&c||16&c?a=Qe(a,c,!1,b&&!(c&16)):(a[E]|=34,c&4&&Object.freeze(a)));return a}if(a!=null&&a[sd]===xd)return b=a.X,c=b[E]|0,yd(a,c)?a:Re(a,b,c)?Se(a,b):Qe(b,c);if(a instanceof ed)return a}
function Se(a,b,c){a=new a.constructor(b);c&&(a.h=zd);a.i=zd;return a}
function Qe(a,b,c,d){d??(d=!!(34&b));a=Fe(a,b,Pe,d);d=32;c&&(d|=2);b=b&16769217|d;a[E]=b;return a}
function Te(a){const b=a.X,c=b[E]|0;return yd(a,c)?Re(a,b,c)?Se(a,b,!0):new a.constructor(Qe(b,c,!1)):a}
function Ue(a){if(a.h!==zd)return!1;var b=a.X;b=Qe(b,b[E]|0);b[E]|=2048;a.X=b;a.h=void 0;a.i=void 0;return!0}
function Ve(a){if(!Ue(a)&&yd(a,a.X[E]|0))throw Error();}
function We(a,b){b===void 0&&(b=a[E]|0);b&32&&!(b&4096)&&(a[E]=b|4096)}
function Re(a,b,c){return c&2?!0:c&32&&!(c&4096)?(b[E]=c|2,a.h=zd,!0):!1}
;const Xe=Ld(0),Ye={};function Ze(a,b,c,d,e){Object.isExtensible(a);b=$e(a.X,b,c,e);if(b!==null||d&&a.i!==zd)return b}
function $e(a,b,c,d){if(b===-1)return null;const e=b+(c?0:-1),f=a.length-1;let g,h;if(!(f<1+(c?0:-1))){if(e>=f)if(g=a[f],g!=null&&typeof g==="object"&&g.constructor===Object)c=g[b],h=!0;else if(e===f)c=g;else return;else c=a[e];if(d&&c!=null){d=d(c);if(d==null)return d;if(!Object.is(d,c))return h?g[b]=d:a[e]=d,d}return c}}
function F(a,b,c,d){Ve(a);const e=a.X;af(e,e[E]|0,b,c,d);return a}
function af(a,b,c,d,e){const f=c+(e?0:-1);var g=a.length-1;if(g>=1+(e?0:-1)&&f>=g){const h=a[g];if(h!=null&&typeof h==="object"&&h.constructor===Object)return h[c]=d,b}if(f<=g)return a[f]=d,b;d!==void 0&&(g=(b??(b=a[E]|0))>>14&1023||536870912,c>=g?d!=null&&(a[g+(e?0:-1)]={[c]:d}):a[f]=d);return b}
function bf(a,b,c){a=$e(a,b,c);return Array.isArray(a)?a:vd}
function cf(a,b){2&b&&(a|=2);return a|1}
function df(a){return!!(2&a)&&!!(4&a)||!!(256&a)}
function ef(a){return Ad(a,!0)}
function ff(a){a=Ze(a,1,void 0,void 0,ef);return a==null?cd():a}
function gf(a,b,c){Ve(a);const d=a.X;let e=d[E]|0;if(b==null)return af(d,e,3),a;if(!Array.isArray(b))throw jd();let f=b===vd?7:b[E]|0,g=f;var h=df(f);let k=h||Object.isFrozen(b);h||(f=0);k||(b=[...b],g=0,f=hf(f,e),k=!1);f|=5;h=(4&f?512&f?512:1024&f?1024:0:void 0)??(yc?1024:0);f|=h;for(let l=0;l<b.length;l++){const n=b[l],m=c(n,h);Object.is(n,m)||(k&&(b=[...b],g=0,f=hf(f,e),k=!1),b[l]=m)}f!==g&&(k&&(b=[...b],f=hf(f,e)),b[E]=f);af(d,e,3,b);return a}
function jf(a,b,c,d){Ve(a);const e=a.X;af(e,e[E]|0,b,c===""?void 0:c,d);return a}
function kf(a,b,c,d){Ve(a);a=a.X;var e=a[E]|0;if(d==null){var f=a[md]??(a[md]=new Map);if(lf(f,a,e,c)===b)f.set(c,0);else return}else{b===0||c.includes(b);f=a[md]??(a[md]=new Map);const g=lf(f,a,e,c);g!==b&&(g&&(e=af(a,e,g)),f.set(c,b))}af(a,e,b,d)}
function lf(a,b,c,d){let e=a.get(d);if(e!=null)return e;e=0;for(let f=0;f<d.length;f++){const g=d[f];$e(b,g)!=null&&(e!==0&&(c=af(b,c,e)),e=g)}a.set(d,e);return e}
function mf(a,b,c,d,e){let f=!1;d=$e(a,d,e,g=>{const h=ze(g,c,b);f=h!==g&&h!=null;return h});
if(d!=null)return f&&!yd(d)&&We(a,b),d}
function nf(a,b,c,d){let e=a.X,f=e[E]|0;b=mf(e,f,b,c,d);if(b==null)return b;f=e[E]|0;if(!yd(a,f)){const g=Te(b);g!==b&&(Ue(a)&&(e=a.X,f=e[E]|0),b=g,f=af(e,f,c,b,d),We(e,f))}return b}
function Yb(a,b,c){var d=void 0===Bd?2:4;var e=a.X,f=e,g=e[E]|0,h=yd(a,g);e=h?1:d;d=e===3;var k=!h;(e===2||k)&&Ue(a)&&(f=a.X,g=f[E]|0);h=bf(f,c);var l=h===vd?7:h[E]|0,n=cf(l,g);if(a=!(4&n)){var m=h,u=g;const p=!!(2&n);p&&(u|=2);let z=!p,D=!0,B=0,M=0;for(;B<m.length;B++){const K=ze(m[B],b,u);if(K instanceof b){if(!p){const aa=yd(K);z&&(z=!aa);D&&(D=aa)}m[M++]=K}}M<B&&(m.length=M);n|=4;n=D?n&-4097:n|4096;n=z?n|8:n&-9}n!==l&&(h[E]=n,2&n&&Object.freeze(h));if(k&&!(8&n||!h.length&&(e===1||(e!==4?0:2&n||
!(16&n)&&32&g)))){df(n)&&(h=[...h],n=hf(n,g),g=af(f,g,c,h));b=h;k=n;for(l=0;l<b.length;l++)m=b[l],n=Te(m),m!==n&&(b[l]=n);k|=8;n=k=b.length?k|4096:k&-4097;h[E]=n}k=b=n;e===1||(e!==4?0:2&b||!(16&b)&&32&g)?df(b)||(b|=!h.length||a&&!(4096&b)||32&g&&!(4096&b||16&b)?2:256,b!==k&&(h[E]=b),Object.freeze(h)):(e===2&&df(b)&&(h=[...h],k=0,b=hf(b,g),g=af(f,g,c,h)),df(b)||(d||(b|=16),b!==k&&(h[E]=b)));2&b||!(4096&b||16&b)||We(f,g);return h}
function of(a,b){a!=null?ye(a,b):a=void 0;return a}
function pf(a,b,c,d,e){d=of(d,b);F(a,c,d,e);d&&!yd(d)&&We(a.X);return a}
function qf(a,b,c,d){Ve(a);const e=a.X;let f=e[E]|0;if(d==null)return af(e,f,c),a;if(!Array.isArray(d))throw jd();let g=d===vd?7:d[E]|0,h=g;const k=df(g),l=k||Object.isFrozen(d);let n=!0,m=!0;for(let p=0;p<d.length;p++){var u=d[p];ye(u,b);k||(u=yd(u),n&&(n=!u),m&&(m=u))}k||(g=n?13:5,g=m?g&-4097:g|4096);l&&g===h||(d=[...d],h=0,g=hf(g,f));g!==h&&(d[E]=g);f=af(e,f,c,d);2&g||!(4096&g||16&g)||We(e,f);return a}
function hf(a,b){return a=(2&b?a|2:a&-3)&-273}
function $b(a,b,c=0){return ie(Ze(a,b))??c}
function rf(a,b,c=Xe){return(yc?Ze(a,b,void 0,void 0,se):se(Ze(a,b)))??c}
function sf(a,b,c="",d){return xe(Ze(a,b,d))??c}
function tf(a){a=Ze(a,1);return(a==null?a:ae(a)?a|0:void 0)??0}
function uf(a,b,c){return F(a,b,we(c))}
function vf(a,b,c){if(c!=null){if(!ae(c))throw jd("enum");c|=0}return F(a,b,c)}
;function wf(a){if(!a)return xf||(xf=new yf(0,0));if(!/^\d+$/.test(a))return null;Xd(a);return new yf(Pd,Qd)}
var yf=class{constructor(a,b){this.i=a>>>0;this.h=b>>>0}};let xf;function zf(a){if(!a)return Af||(Af=new Bf(0,0));if(!/^-?\d+$/.test(a))return null;Xd(a);return new Bf(Pd,Qd)}
var Bf=class{constructor(a,b){this.i=a>>>0;this.h=b>>>0}};let Af;function Cf(a,b,c){for(;c>0||b>127;)a.h.push(b&127|128),b=(b>>>7|c<<25)>>>0,c>>>=7;a.h.push(b)}
function Df(a,b){a.h.push(b>>>0&255);a.h.push(b>>>8&255);a.h.push(b>>>16&255);a.h.push(b>>>24&255)}
function Ef(a,b){for(;b>127;)a.h.push(b&127|128),b>>>=7;a.h.push(b)}
var Ff=class{constructor(){this.h=[]}length(){return this.h.length}end(){const a=this.h;this.h=[];return a}writeUint8(a){this.h.push(a>>>0&255)}writeInt8(a){this.h.push(a>>>0&255)}};function Gf(a,b){b.length!==0&&(a.j.push(b),a.i+=b.length)}
function Hf(a,b){Ef(a.h,b*8+2);b=a.h.end();Gf(a,b);b.push(a.i);return b}
function If(a,b){var c=b.pop();for(c=a.i+a.h.length()-c;c>127;)b.push(c&127|128),c>>>=7,a.i++;b.push(c);a.i++}
function Jf(a,b,c){if(c!=null){switch(typeof c){case "string":wf(c)}Ef(a.h,b*8+1);switch(typeof c){case "number":a=a.h;Sd(c);Df(a,Pd);Df(a,Qd);break;case "bigint":c=BigInt.asUintN(64,c);c=new yf(Number(c&BigInt(4294967295)),Number(c>>BigInt(32)));a=a.h;b=c.h;Df(a,c.i);Df(a,b);break;default:c=wf(c),a=a.h,b=c.h,Df(a,c.i),Df(a,b)}}}
var Kf=class{constructor(){this.j=[];this.i=0;this.h=new Ff}};function Lf(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a}
var Mf=Lf(),Nf=Lf(),Of=Lf(),Pf=Lf(),Qf=Lf(),Rf=Lf(),Sf=Lf();function Tf(a,b){if(b==null||b=="")return new a;b=JSON.parse(b);if(!Array.isArray(b))throw Error("dnarr");b[E]|=32;return new a(b)}
var G=class{constructor(a,b,c){this.X=Ne(a,b,c,2048)}toJSON(){return Je(this)}serialize(a){return JSON.stringify(Je(this,a))}clone(){const a=this.X,b=a[E]|0;return Re(this,a,b)?Se(this,a,!0):new this.constructor(Qe(a,b,!1))}};G.prototype[sd]=xd;G.prototype.toString=function(){return this.X.toString()};var H=class{constructor(a,b){this.Lc=a;a=ua(Mf);this.h=!!a&&b===a||!1}};function Uf(a,b,c,d,e){b=Vf(b,d);b!=null&&(c=Hf(a,c),e(b,a),If(a,c))}
const Wf=new H(Uf,Mf),Xf=new H(Uf,Mf);var Yf=Symbol(),Zf=Symbol();let $f,ag;
function bg(a){var b=cg,c=dg,d=a[Yf];if(d)return d;d={};d.Vh=a;d.yd=Me(a[0]);var e=a[1];let f=1;e&&e.constructor===Object&&(d.extensions=e,e=a[++f],typeof e==="function"&&(d.Ye=!0,$f??($f=e),ag??(ag=a[f+1]),e=a[f+=2]));const g={};for(;e&&eg(e);){for(var h=0;h<e.length;h++)g[e[h]]=e;e=a[++f]}for(h=1;e!==void 0;){typeof e==="number"&&(h+=e,e=a[++f]);let n;var k=void 0;e instanceof H?n=e:(n=Wf,f--);if(n?.h){e=a[++f];k=a;var l=f;typeof e==="function"&&(e=e(),k[l]=e);k=e}e=a[++f];l=h+1;typeof e==="number"&&
e<0&&(l-=e,e=a[++f]);for(;h<l;h++){const m=g[h];k?c(d,h,n,k,m):b(d,h,n,m)}}return a[Yf]=d}
function eg(a){return Array.isArray(a)&&!!a.length&&typeof a[0]==="number"&&a[0]>0}
function Vf(a,b){if(a instanceof G)return a.X;if(Array.isArray(a))return Ne(a,b[0],b[1])}
;function cg(a,b,c){a[b]=c.Lc}
function dg(a,b,c,d){let e,f;const g=c.Lc;a[b]=(h,k,l)=>g(h,k,l,f||(f=bg(d).yd),e||(e=fg(d)))}
function fg(a){let b=a[Zf];if(!b){const c=bg(a);b=(d,e)=>gg(d,e,c);
a[Zf]=b}return b}
function gg(a,b,c){Cd(a,a[E]|0,(d,e)=>{if(e!=null){var f=hg(c,d);f?f(b,e,d):d<500||kd(qd,3)}});
(a=Ce(a))&&a.Oe((d,e,f)=>{Gf(b,b.h.end());for(d=0;d<f.length;d++)Gf(b,fd(f[d])||new Uint8Array(0))})}
function hg(a,b){var c=a[b];if(c)return c;if(c=a.extensions)if(c=c[b]){c=Array.isArray(c)?c[0]instanceof H?c:[Xf,c]:[c,void 0];var d=c[0].Lc;if(c=c[1]){const e=fg(c),f=bg(c).yd;c=a.Ye?ag(f,e):(g,h,k)=>d(g,h,k,f,e)}else c=d;
return a[b]=c}}
;function ig(a,b,c){if(Array.isArray(b)){var d=b[E]|0;if(d&4)return b;for(var e=0,f=0;e<b.length;e++){const g=a(b[e]);g!=null&&(b[f++]=g)}f<e&&(b.length=f);a=d|1;c&&(a=(a|4)&-1537);a!==d&&(b[E]=a);c&&a&2&&Object.freeze(b);return b}}
function jg(a,b,c){b=b==null||typeof b==="number"?b:b==="NaN"||b==="Infinity"||b==="-Infinity"?Number(b):void 0;b!=null&&(Ef(a.h,c*8+1),a=a.h,c=Rd||(Rd=new DataView(new ArrayBuffer(8))),c.setFloat64(0,+b,!0),Pd=c.getUint32(0,!0),Qd=c.getUint32(4,!0),Df(a,Pd),Df(a,Qd))}
function kg(a,b,c){b=te(b);if(b!=null){switch(typeof b){case "string":zf(b)}if(b!=null)switch(Ef(a.h,c*8),typeof b){case "number":a=a.h;Td(b);Cf(a,Pd,Qd);break;case "bigint":c=BigInt.asUintN(64,b);c=new Bf(Number(c&BigInt(4294967295)),Number(c>>BigInt(32)));Cf(a.h,c.i,c.h);break;default:c=zf(b),Cf(a.h,c.i,c.h)}}}
function lg(a,b,c){b=ie(b);if(b!=null&&b!=null)if(Ef(a.h,c*8),a=a.h,c=b,c>=0)Ef(a,c);else{for(b=0;b<9;b++)a.h.push(c&127|128),c>>=7;a.h.push(1)}}
function mg(a,b,c){b=b==null||typeof b==="boolean"?b:typeof b==="number"?!!b:void 0;b!=null&&(Ef(a.h,c*8),a.h.h.push(b?1:0))}
function ng(a,b,c){b=xe(b);b!=null&&(b=tc(b),Ef(a.h,c*8+2),Ef(a.h,b.length),Gf(a,a.h.end()),Gf(a,b))}
function og(a,b,c,d,e){b=Vf(b,d);b!=null&&(c=Hf(a,c),e(b,a),If(a,c))}
var pg=new H(mg,Nf),qg=new H(ng,Of),rg=function(a,b,c=Mf){return new H(b,c)}(function(a,b,c,d,e){if(a.h()!==2)return!1;
var f=a.i;d=Ne(void 0,d[0],d[1]);var g=b[E]|0;if(g&2)throw Error();const h=g&128?Dd:void 0;let k=bf(b,c,h),l=k===vd?7:k[E]|0,n=cf(l,g);if(2&n||df(n)||16&n)n===l||df(n)||(k[E]=n),k=[...k],l=0,n=hf(n,g),af(b,g,c,k,h);n&=-13;n!==l&&(k[E]=n);k.push(d);f.call(a,d,e);return!0},function(a,b,c,d,e){if(Array.isArray(b)){for(let f=0;f<b.length;f++)og(a,b[f],c,d,e);
a=b[E]|0;a&1||(b[E]=a|1)}}),sg=new H(og,Mf);class tg{constructor(a){var b=ug;this.ctor=a;this.isRepeated=0;this.h=nf;this.defaultValue=void 0;this.i=b.gf!=null?Dd:void 0}register(){Jc(this)}};function vg(a){return b=>Tf(a,b)}
;function wg(a,b){return gf(a,b,ge)}
var xg=class extends G{constructor(a){super(a)}};var yg=class extends G{constructor(a){super(a)}},zg=[1,2,3];var Ag=class extends G{constructor(a){super(a)}},Bg=[1,2,3];var Cg=class extends G{constructor(a){super(a)}};var Dg=class extends G{constructor(a){super(a)}};var Eg=class extends G{constructor(a){super(a)}},Fg=[1,2,3];var Gg=class extends G{constructor(a){super(a)}};Gg.prototype.j=function(a){return function(){const b=new Kf;gg(this.X,b,bg(a));Gf(b,b.h.end());const c=new Uint8Array(b.i),d=b.j,e=d.length;let f=0;for(let g=0;g<e;g++){const h=d[g];c.set(h,f);f+=h.length}b.j=[c];return c}}([0,
qg,[0,Fg,sg,[0,qg,-1,pg],sg,[0,qg,-1,new H(lg,Pf),pg],sg,[0,qg]],new H(function(a,b,c){b=ig(xe,b,!0);if(b!=null)for(let g=0;g<b.length;g++){var d=a,e=c,f=b[g];f!=null&&(f=tc(f),Ef(d.h,e*8+2),Ef(d.h,f.length),Gf(d,d.h.end()),Gf(d,f))}},Of),
rg,[0,rg,[0,zg,new H(ng,Of),new H(lg,Pf),new H(mg,Nf)],[0,Bg,new H(kg,Qf),new H(jg,Sf),sg,[0,rg,[0,new H(jg,Sf),new H(kg,Qf)]]]],new H(function(a,b,c){Jf(a,c,ue(b))},Rf),
new H(function(a,b,c){b=ig(ue,b,!1);if(b!=null)for(let d=0;d<b.length;d++)Jf(a,c,b[d])},Rf)]);var Hg=class extends G{constructor(a){super(a)}};function Ig(a){var b=new Gg;b=uf(b,1,a.i);var c=Jg(a);b=gf(b,c,ve);c=[];const d=[];for(var e of a.h.keys())d.push(e.split(","));for(e=0;e<d.length;e++){const u=d[e];var f=a.j,g=Kg(a,u)||[],h=[];for(var k=0;k<g.length;k++){var l=g[k],n=l&&l.h;l=new Ag;switch(f){case 3:n=Number(n);Number.isFinite(n)&&kf(l,1,Bg,qe(n));break;case 2:n=Number(n);if(n!=null&&typeof n!=="number")throw Error(`Value of float/double field must be a number, found ${typeof n}: ${n}`);kf(l,2,Bg,n)}h.push(l)}f=h;for(g=0;g<f.length;g++){k=
f[g];h=new Cg;h=pf(h,Ag,2,k);k=[];l=Lg(a);for(n=0;n<l.length;n++){var m=l[n];const p=u[n],z=new yg;switch(m){case 3:kf(z,1,zg,we(String(p)));break;case 2:m=Number(p);Number.isFinite(m)&&kf(z,2,zg,he(m));break;case 1:kf(z,3,zg,de(p==="true"))}k.push(z)}qf(h,yg,1,k);c.push(h)}}qf(b,Cg,4,c);return b}
;function Mg(a){if(!a)return"";if(/^about:(?:blank|srcdoc)$/.test(a))return window.origin||"";a.indexOf("blob:")===0&&(a=a.substring(5));a=a.split("#")[0].split("?")[0];a=a.toLowerCase();a.indexOf("//")==0&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");c!=-1&&(b=b.substring(0,c));c=a.substring(0,a.indexOf("://"));if(!c)throw Error("URI is missing protocol: "+a);if(c!=="http"&&c!=="https"&&c!=="chrome-extension"&&
c!=="moz-extension"&&c!=="file"&&c!=="android-app"&&c!=="chrome-search"&&c!=="chrome-untrusted"&&c!=="chrome"&&c!=="app"&&c!=="devtools")throw Error("Invalid URI scheme in origin: "+c);a="";var d=b.indexOf(":");if(d!=-1){var e=b.substring(d+1);b=b.substring(0,d);if(c==="http"&&e!=="80"||c==="https"&&e!=="443")a=":"+e}return c+"://"+b+a}
;function Ng(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;n=l=0}
function b(m){for(var u=g,p=0;p<64;p+=4)u[p/4]=m[p]<<24|m[p+1]<<16|m[p+2]<<8|m[p+3];for(p=16;p<80;p++)m=u[p-3]^u[p-8]^u[p-14]^u[p-16],u[p]=(m<<1|m>>>31)&4294967295;m=e[0];var z=e[1],D=e[2],B=e[3],M=e[4];for(p=0;p<80;p++){if(p<40)if(p<20){var K=B^z&(D^B);var aa=1518500249}else K=z^D^B,aa=1859775393;else p<60?(K=z&D|B&(z|D),aa=2400959708):(K=z^D^B,aa=3395469782);K=((m<<5|m>>>27)&4294967295)+K+M+aa+u[p]&4294967295;M=B;B=D;D=(z<<30|z>>>2)&4294967295;z=m;m=K}e[0]=e[0]+m&4294967295;e[1]=e[1]+z&4294967295;
e[2]=e[2]+D&4294967295;e[3]=e[3]+B&4294967295;e[4]=e[4]+M&4294967295}
function c(m,u){if(typeof m==="string"){m=unescape(encodeURIComponent(m));for(var p=[],z=0,D=m.length;z<D;++z)p.push(m.charCodeAt(z));m=p}u||(u=m.length);p=0;if(l==0)for(;p+64<u;)b(m.slice(p,p+64)),p+=64,n+=64;for(;p<u;)if(f[l++]=m[p++],n++,l==64)for(l=0,b(f);p+64<u;)b(m.slice(p,p+64)),p+=64,n+=64}
function d(){var m=[],u=n*8;l<56?c(h,56-l):c(h,64-(l-56));for(var p=63;p>=56;p--)f[p]=u&255,u>>>=8;b(f);for(p=u=0;p<5;p++)for(var z=24;z>=0;z-=8)m[u++]=e[p]>>z&255;return m}
for(var e=[],f=[],g=[],h=[128],k=1;k<64;++k)h[k]=0;var l,n;a();return{reset:a,update:c,digest:d,xe:function(){for(var m=d(),u="",p=0;p<m.length;p++)u+="0123456789ABCDEF".charAt(Math.floor(m[p]/16))+"0123456789ABCDEF".charAt(m[p]%16);return u}}}
;function Og(a,b,c){var d=String(t.location.href);return d&&a&&b?[b,Pg(Mg(d),a,c||null)].join(" "):null}
function Pg(a,b,c){var d=[];let e=[];if((Array.isArray(c)?2:1)==1)return e=[b,a],hb(d,function(h){e.push(h)}),Qg(e.join(" "));
const f=[],g=[];hb(c,function(h){g.push(h.key);f.push(h.value)});
c=Math.floor((new Date).getTime()/1E3);e=f.length==0?[c,b,a]:[f.join(":"),c,b,a];hb(d,function(h){e.push(h)});
a=Qg(e.join(" "));a=[c,a];g.length==0||a.push(g.join(""));return a.join("_")}
function Qg(a){const b=Ng();b.update(a);return b.xe().toLowerCase()}
;function Rg(a){this.h=a||{cookie:""}}
r=Rg.prototype;r.isEnabled=function(){if(!t.navigator.cookieEnabled)return!1;if(this.h.cookie)return!0;this.set("TESTCOOKIESENABLED","1",{wc:60});if(this.get("TESTCOOKIESENABLED")!=="1")return!1;this.remove("TESTCOOKIESENABLED");return!0};
r.set=function(a,b,c){let d;var e=!1;let f;if(typeof c==="object"){f=c.sameSite;e=c.secure||!1;d=c.domain||void 0;var g=c.path||void 0;var h=c.wc}if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');h===void 0&&(h=-1);c=d?";domain="+d:"";g=g?";path="+g:"";e=e?";secure":"";h=h<0?"":h==0?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(Date.now()+h*1E3)).toUTCString();this.h.cookie=a+"="+b+c+g+h+e+(f!=null?
";samesite="+f:"")};
r.get=function(a,b){const c=a+"=",d=(this.h.cookie||"").split(";");for(let e=0,f;e<d.length;e++){f=d[e].trim();if(f.lastIndexOf(c,0)==0)return f.slice(c.length);if(f==a)return""}return b};
r.remove=function(a,b,c){const d=this.get(a)!==void 0;this.set(a,"",{wc:0,path:b,domain:c});return d};
r.Vb=function(){return Sg(this).keys};
r.ab=function(){return Sg(this).values};
r.clear=function(){const a=Sg(this).keys;for(let b=a.length-1;b>=0;b--)this.remove(a[b])};
function Sg(a){a=(a.h.cookie||"").split(";");const b=[],c=[];let d,e;for(let f=0;f<a.length;f++)e=a[f].trim(),d=e.indexOf("="),d==-1?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));return{keys:b,values:c}}
var Tg=new Rg(typeof document=="undefined"?null:document);function Ug(){var a=t.__SAPISID||t.__APISID||t.__3PSAPISID||t.__1PSAPISID||t.__OVERRIDE_SID;if(a)return!0;typeof document!=="undefined"&&(a=new Rg(document),a=a.get("SAPISID")||a.get("APISID")||a.get("__Secure-3PAPISID")||a.get("__Secure-1PAPISID"));return!!a}
function Vg(a,b,c,d){(a=t[a])||typeof document==="undefined"||(a=(new Rg(document)).get(b));return a?Og(a,c,d):null}
function Wg(a){var b=Mg(t?.location.href);const c=[];if(Ug()){b=b.indexOf("https:")==0||b.indexOf("chrome-extension:")==0||b.indexOf("chrome-untrusted://new-tab-page")==0||b.indexOf("moz-extension:")==0;var d,e=(d=b)?t.__SAPISID:t.__APISID;e||typeof document==="undefined"||(e=new Rg(document),e=e.get(d?"SAPISID":"APISID")||e.get("__Secure-3PAPISID"));(d=e?Og(e,d?"SAPISIDHASH":"APISIDHASH",a):null)&&c.push(d);b&&((b=Vg("__1PSAPISID","__Secure-1PAPISID","SAPISID1PHASH",a))&&c.push(b),(a=Vg("__3PSAPISID",
"__Secure-3PAPISID","SAPISID3PHASH",a))&&c.push(a))}return c.length==0?null:c.join(" ")}
;var Xg=class{async compress(a){var b=new CompressionStream("gzip");const c=(new Response(b.readable)).arrayBuffer();b=b.writable.getWriter();await b.write((new TextEncoder).encode(a));await b.close();return new Uint8Array(await c)}isSupported(a){return a<1024?!1:typeof CompressionStream!=="undefined"}};var Yg=class extends G{constructor(a){super(a)}};var Zg=class{constructor(a,b){this.intervalMs=a;this.callback=b;this.enabled=!1;this.h=()=>ta();
this.i=this.h()}setInterval(a){this.intervalMs=a;this.timer&&this.enabled?(this.stop(),this.start()):this.timer&&this.stop()}start(){this.enabled=!0;this.timer||(this.timer=setTimeout(()=>{this.tick()},this.intervalMs),this.i=this.h())}stop(){this.enabled=!1;
this.timer&&(clearTimeout(this.timer),this.timer=void 0)}tick(){if(this.enabled){const a=Math.max(this.h()-this.i,0);a<this.intervalMs*.8?this.timer=setTimeout(()=>{this.tick()},this.intervalMs-a):(this.timer&&(clearTimeout(this.timer),this.timer=void 0),this.callback(),this.enabled&&(this.stop(),this.start()))}else this.timer=void 0}};var $g=class extends G{constructor(a){super(a)}};var ah=class extends G{constructor(a){super(a)}};function bh(a,b){this.x=a!==void 0?a:0;this.y=b!==void 0?b:0}
r=bh.prototype;r.clone=function(){return new bh(this.x,this.y)};
r.equals=function(a){return a instanceof bh&&(this==a?!0:this&&a?this.x==a.x&&this.y==a.y:!1)};
r.ceil=function(){this.x=Math.ceil(this.x);this.y=Math.ceil(this.y);return this};
r.floor=function(){this.x=Math.floor(this.x);this.y=Math.floor(this.y);return this};
r.round=function(){this.x=Math.round(this.x);this.y=Math.round(this.y);return this};
r.scale=function(a,b){this.x*=a;this.y*=typeof b==="number"?b:a;return this};function ch(a,b){this.width=a;this.height=b}
r=ch.prototype;r.clone=function(){return new ch(this.width,this.height)};
r.aspectRatio=function(){return this.width/this.height};
r.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
r.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
r.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};
r.scale=function(a,b){this.width*=a;this.height*=typeof b==="number"?b:a;return this};function dh(a,b){for(const c in a)b.call(void 0,a[c],c,a)}
function eh(a){const b=[];let c=0;for(const d in a)b[c++]=a[d];return b}
function fh(a){var b=gh;for(const c in b)if(a.call(void 0,b[c],c,b))return c}
function hh(a){for(const b in a)return!1;return!0}
function ih(a,b){if(a!==null&&b in a)throw Error(`The object already contains the key "${b}"`);a[b]=!0}
function jh(a){return a!==null&&"privembed"in a?a.privembed:!1}
function kh(a,b){for(const c in a)if(!(c in b)||a[c]!==b[c])return!1;for(const c in b)if(!(c in a))return!1;return!0}
function lh(a){const b={};for(const c in a)b[c]=a[c];return b}
function mh(a){if(!a||typeof a!=="object")return a;if(typeof a.clone==="function")return a.clone();if(typeof Map!=="undefined"&&a instanceof Map)return new Map(a);if(typeof Set!=="undefined"&&a instanceof Set)return new Set(a);if(a instanceof Date)return new Date(a.getTime());const b=Array.isArray(a)?[]:typeof ArrayBuffer!=="function"||typeof ArrayBuffer.isView!=="function"||!ArrayBuffer.isView(a)||a instanceof DataView?{}:new a.constructor(a.length);for(const c in a)b[c]=mh(a[c]);return b}
const nh="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function oh(a,b){let c,d;for(let e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(let f=0;f<nh.length;f++)c=nh[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var qh=class{constructor(a,b){this.h=a===ph&&b||""}toString(){return this.h}},ph={};new qh(ph,"");function db(a){return new bb(a[0].toLowerCase())}
;"ARTICLE SECTION NAV ASIDE H1 H2 H3 H4 H5 H6 HEADER FOOTER ADDRESS P HR PRE BLOCKQUOTE OL UL LH LI DL DT DD FIGURE FIGCAPTION MAIN DIV EM STRONG SMALL S CITE Q DFN ABBR RUBY RB RT RTC RP DATA TIME CODE VAR SAMP KBD SUB SUP I B U MARK BDI BDO SPAN BR WBR NOBR INS DEL PICTURE PARAM TRACK MAP TABLE CAPTION COLGROUP COL TBODY THEAD TFOOT TR TD TH SELECT DATALIST OPTGROUP OPTION OUTPUT PROGRESS METER FIELDSET LEGEND DETAILS SUMMARY MENU DIALOG SLOT CANVAS FONT CENTER ACRONYM BASEFONT BIG DIR HGROUP STRIKE TT".split(" ").concat(["BUTTON",
"INPUT"]);function rh(a){var b=document;return typeof a==="string"?b.getElementById(a):a}
function sh(a){var b=document;a=String(a);b.contentType==="application/xhtml+xml"&&(a=a.toLowerCase());return b.createElement(a)}
function th(a){let b;for(;b=a.firstChild;)a.removeChild(b)}
function uh(a){a&&a.parentNode&&a.parentNode.removeChild(a)}
function vh(a,b){let c=0;for(;a;){if(b(a))return a;a=a.parentNode;c++}return null}
;var wh=class extends G{constructor(a){super(a)}qc(){return tf(this)}};var xh=class extends G{constructor(a){super(a)}};function yh(a){qf(zh,xh,1,a)}
var Ah=class extends G{constructor(a){super(a)}},Bh=vg(Ah);var Ch=class extends G{constructor(a){super(a)}};var Dh=["platform","platformVersion","architecture","model","uaFullVersion"];const zh=new Ah;let Eh=null;function Fh(a,b=Dh){if(!Eh){a=a.navigator?.userAgentData;if(!a||typeof a.getHighEntropyValues!=="function"||a.brands&&typeof a.brands.map!=="function")return Promise.reject(Error("UACH unavailable"));yh((a.brands||[]).map(d=>{var e=new xh;e=uf(e,1,d.brand);return uf(e,2,d.version)}));
typeof a.mobile==="boolean"&&F(zh,2,de(a.mobile));Eh=a.getHighEntropyValues(b)}const c=new Set(b);return Eh.then(d=>{const e=zh.clone();c.has("platform")&&uf(e,3,d.platform);c.has("platformVersion")&&uf(e,4,d.platformVersion);c.has("architecture")&&uf(e,5,d.architecture);c.has("model")&&uf(e,6,d.model);c.has("uaFullVersion")&&uf(e,7,d.uaFullVersion);return e.serialize()}).catch(()=>zh.serialize())}
;function Gh(a){return vf(a,1,1)}
var Hh=class extends G{constructor(a){super(a)}};var Ih=class extends G{constructor(a){super(a,4)}};var Jh=class extends G{constructor(a){super(a,37)}};var Kh=class extends G{constructor(a){super(a,19)}bc(a){return vf(this,2,a)}};function Lh(a,b){pf(a.h,Hh,1,b);tf(b)||Gh(b);a.Sa||(b=Mh(a),sf(b,5)||uf(b,5,a.locale));a.j&&(b=Mh(a),nf(b,Ah,9)||pf(b,Ah,9,a.j))}
function Mh(a){var b=nf(a.h,Hh,1);b||(b=new Hh,Lh(a,b));a=b;b=nf(a,Ch,11);b||(b=new Ch,pf(a,Ch,11,b));return b}
function Nh(a,b){a.i=b}
function Oh(a){const b=a.Sa?void 0:window;b?Fh(b,Dh).then(c=>{a.j=Bh(c??"[]");c=Mh(a);pf(c,Ah,9,a.j);return!0}).catch(()=>!1):Promise.resolve(!1)}
function Ph(a,b,c=0,d=0,e=null,f=0,g=0){if(!a.Sa){var h=Mh(a);var k=new wh;k=vf(k,1,a.i);k=F(k,2,de(a.isFinal));d=F(k,3,he(d>0?d:void 0));f=F(d,4,he(f>0?f:void 0));g=F(f,5,he(g>0?g:void 0));f=g.X;d=f[E]|0;g=yd(g,d)?g:Re(g,f,d)?Se(g,f):new g.constructor(Qe(f,d,!0));pf(h,wh,10,g)}a=a.h.clone();h=Date.now().toString();a=F(a,4,qe(h));b=b.slice();b=qf(a,Jh,3,b);e&&(a=new $g,e=F(a,13,he(e)),a=new ah,e=pf(a,$g,2,e),a=new Ih,e=pf(a,ah,1,e),e=vf(e,2,9),pf(b,Ih,18,e));c&&F(b,14,qe(c));return b}
var Qh=class{constructor(a,b=!1){this.Sa=b;this.j=this.locale=null;this.i=0;this.isFinal=!1;this.h=new Kh;Number.isInteger(a)&&this.h.bc(a);b||(this.locale=document.documentElement.getAttribute("lang"));Lh(this,new Hh)}bc(a){this.h.bc(a);return this}};function Rh(a,b,c,d){this.o=a;this.u=b;this.h=this.j=a;this.H=c||0;this.A=d||2}
Rh.prototype.i=0;Rh.prototype.reset=function(){this.h=this.j=this.o;this.i=0};
Rh.prototype.getValue=function(){return this.j};
function Sh(a){a.h=Math.min(a.u,a.h*a.A);a.j=Math.min(a.u,a.h+(a.H?Math.round(a.H*(Math.random()-.5)*2*a.h):0));a.i++}
;var ug=class extends G{constructor(a){super(a,8)}},Th=vg(ug);var Uh;Uh=new tg(class extends G{constructor(a){super(a)}});function Vh(){return"https://play.google.com/log?format=json&hasfast=true"}
function Wh(a,b){if(!a.Ba)return()=>{};
const c=()=>{a.flush()};
return b?()=>{b().then(c)}:c}
function Xh(a){a.j.isFinal=!0;a.flush();a.j.isFinal=!1}
function Yh(a){a.G||(a.G=Vh());try{return(new URL(a.G)).toString()}catch(b){return(new URL(a.G,window.location.origin)).toString()}}
function Zh(a){$h(a,(b,c)=>{b=new URL(b);b.searchParams.set("format","json");let d=!1;try{d=window.navigator.sendBeacon(b.toString(),c.serialize())}catch{}d||(a.P=!1);return d})}
function ai(a,b,c=null,d=a.withCredentials){const e={},f=new URL(Yh(a));c&&(e.Authorization=c);a.sessionIndex&&(e["X-Goog-AuthUser"]=a.sessionIndex,f.searchParams.set("authuser",a.sessionIndex));a.pageId&&(Object.defineProperty(e,"X-Goog-PageId",{value:a.pageId}),f.searchParams.set("pageId",a.pageId));return{url:f.toString(),body:b,ne:1,Fc:e,requestType:"POST",withCredentials:d,timeoutMillis:a.timeoutMillis}}
function $h(a,b){if(a.h.length!==0){var c=new URL(Yh(a));c.searchParams.delete("format");var d=a.zb();d&&c.searchParams.set("auth",d);c.searchParams.set("authuser",a.sessionIndex||"0");for(d=0;d<10&&a.h.length;++d){const e=a.h.slice(0,32),f=Ph(a.j,e,a.o,a.A,a.nb,a.Z,a.Y);if(!b(c.toString(),f)){++a.A;break}a.o=0;a.A=0;a.Z=0;a.Y=0;a.h=a.h.slice(e.length)}a.i.enabled&&a.i.stop()}}
var bi=class extends y{constructor(a){super();this.componentId="";this.h=[];this.Fa="";this.pageId=null;this.Ja=this.ga=-1;this.F=this.experimentIds=null;this.Y=this.Z=this.A=this.o=0;this.Wa=1;this.timeoutMillis=0;this.la=!1;this.logSource=a.logSource;this.zb=a.zb||(()=>{});
this.j=new Qh(a.logSource,a.Sa);this.network=a.network||null;this.nb=a.nb||null;this.bufferSize=1E3;this.G=a.Jf||null;this.sessionIndex=a.sessionIndex||null;this.Tb=a.Tb||!1;this.logger=null;this.withCredentials=!a.Oc;this.Sa=a.Sa||!1;this.P=!this.Sa&&!!window&&!!window.navigator&&window.navigator.sendBeacon!==void 0;this.Ba=typeof URLSearchParams!=="undefined"&&!!(new URL(Vh())).searchParams&&!!(new URL(Vh())).searchParams.set;const b=Gh(new Hh);Lh(this.j,b);this.u=new Rh(1E4,3E5,.1);a=Wh(this,a.md);
this.i=new Zg(this.u.getValue(),a);this.qa=new Zg(6E5,a);this.Tb||this.qa.start();this.Sa||(document.addEventListener("visibilitychange",()=>{document.visibilityState==="hidden"&&Xh(this)}),document.addEventListener("pagehide",()=>{Xh(this)}))}ba(){Xh(this);
this.i.stop();this.qa.stop();super.ba()}log(a){if(this.Ba){a=a.clone();var b=this.Wa++;a=F(a,21,qe(b));this.componentId&&uf(a,26,this.componentId);b=a;{var c=Ze(b,1);const d=typeof c;c=c==null?c:d==="bigint"?String(Yd(64,c)):fe(c)?d==="string"?le(c):pe(c):void 0}c==null&&(c=Date.now(),c=Number.isFinite(c)?c.toString():"0",F(b,1,qe(c)));(yc?re(Ze(b,15,void 0,void 0,se)):re(Ze(b,15)))==null&&F(b,15,qe((new Date).getTimezoneOffset()*60));this.experimentIds&&(c=this.experimentIds.clone(),pf(b,Yg,16,c));
b=this.h.length-this.bufferSize+1;b>0&&(this.h.splice(0,b),this.o+=b);this.h.push(a);this.Tb||this.i.enabled||this.i.start()}}flush(a,b){if(this.h.length===0)a&&a();else if(this.la&&this.P)this.j.i=3,Zh(this);else{var c=Date.now();if(this.Ja>c&&this.ga<c)b&&b("throttled");else{this.network&&(typeof this.network.qc==="function"?Nh(this.j,this.network.qc()):this.j.i=0);var d=Ph(this.j,this.h,this.o,this.A,this.nb,this.Z,this.Y),e=this.zb();if(e&&this.Fa===e)b&&b("stale-auth-token");else{this.h=[];this.i.enabled&&
this.i.stop();this.o=0;c=d.serialize();let f;this.F&&this.F.isSupported(c.length)&&(f=this.F.compress(c));const g=ai(this,c,e),h=n=>{this.u.reset();this.i.setInterval(this.u.getValue());if(n){var m=null;try{var u=JSON.stringify(JSON.parse(n.replace(")]}'\n","")));m=Th(u)}catch(p){}if(m){n=Number(rf(m,1,Ld("-1")));n>0&&(this.ga=Date.now(),this.Ja=this.ga+n);(n=ua(nd))&&m.X[n]?.[175237375]!=null&&kd(od,3);if(ua(ud)&&ua(nd)&&void 0===ud&&(n=m.X,u=n[nd])&&(u=u.Di))try{u(n,175237375,De)}catch(p){uc(p)}m=
Uh.ctor?Uh.h(m,Uh.ctor,175237375,Uh.i):Uh.h(m,175237375,null,Uh.i);if(m=m===null?void 0:m)m=$b(m,1,-1),m!==-1&&(this.u=new Rh(m<1?1:m,3E5,.1),this.i.setInterval(this.u.getValue()))}}a&&a();this.A=0},k=(n,m)=>{var u=Yb(d,Jh,3);
var p=Number(rf(d,14));Sh(this.u);this.i.setInterval(this.u.getValue());n===401&&e&&(this.Fa=e);p&&(this.o+=p);m===void 0&&(m=this.isRetryable(n));m&&(this.h=u.concat(this.h),this.Tb||this.i.enabled||this.i.start());b&&b("net-send-failed",n);++this.A},l=()=>{this.network&&this.network.send(g,h,k)};
f?f.then(n=>{g.Fc["Content-Encoding"]="gzip";g.Fc["Content-Type"]="application/binary";g.body=n;g.ne=2;l()},()=>{l()}):l()}}}}isRetryable(a){return 500<=a&&a<600||a===401||a===0}};var ci=class{constructor(){this.ee=typeof AbortController!=="undefined"}async send(a,b,c){const d=this.ee?new AbortController:void 0,e=d?setTimeout(()=>{d.abort()},a.timeoutMillis):void 0;
try{const f=await fetch(a.url,{method:a.requestType,headers:{...a.Fc},...(a.body&&{body:a.body}),...(a.withCredentials&&{credentials:"include"}),signal:a.timeoutMillis&&d?d.signal:null});f.status===200?b?.(await f.text()):c?.(f.status)}catch(f){switch(f?.name){case "AbortError":c?.(408);break;default:c?.(400)}}finally{clearTimeout(e)}}qc(){return 4}};function di(a,b){a.buildLabel=b;return a}
function ei(a){a.network=new fi;return a}
function gi(a,b){a.h=b}
function hi(a){a.i=!0;return a}
function ii(a){a.network||(a.network=new ci);const b=new bi({logSource:a.logSource,zb:a.zb?a.zb:Wg,sessionIndex:a.sessionIndex,Jf:a.hb,Sa:!1,Tb:!1,Oc:a.j,md:a.md,network:a.network});Ob(a,b);if(a.buildLabel){var c=a.buildLabel,d=Mh(b.j);uf(d,7,c)}b.F=new Xg;a.componentId&&(b.componentId=a.componentId);a.nb&&(b.nb=a.nb);a.pageId&&(b.pageId=a.pageId);a.h&&((d=a.h)?(b.experimentIds||(b.experimentIds=new Yg),c=b.experimentIds,d=d.serialize(),uf(c,4,d)):b.experimentIds&&F(b.experimentIds,4));a.i&&(b.la=
b.P);Oh(b.j);a.bufferSize&&(b.bufferSize=a.bufferSize);a.network.bc&&a.network.bc(a.logSource);a.network.xf&&a.network.xf(b);return b}
var ji=class extends y{constructor(){super();this.logSource=1828;this.sessionIndex="0";this.hb="https://play.google.com/log?format=json&hasfast=true";this.network=this.buildLabel=null;this.componentId="";this.h=this.nb=null;this.i=!1;this.pageId=null;this.bufferSize=void 0;this.logger=null}Oc(){this.j=!0;return this}};var ki=class extends y{constructor(a){super();this.logSource=1828;this.componentId="";a||(a=new ji,a.componentId="",Ob(this,a),a=ii(a));this.h=a}flush(a){a=a||[];if(a.length){var b=new Hg;const f=[];for(let g=0;g<a.length;g++){const h=a[g],k=Ig(h);f.push(k);h.clear()}qf(b,Gg,1,f);a=b;b=this.h;if(a instanceof Jh)b.log(a);else try{var c=new Jh,d=a.serialize();var e=uf(c,8,d);b.log(e)}catch{}this.h.flush()}}};var li=class{constructor(a){this.h=a}};function Lg(a){return a.fields.map(b=>b.fieldType)}
function Kg(a,...b){b=mi(b);return a.h.has(b)?a.h.get(b):void 0}
function Jg(a){return a.fields.map(b=>b.fieldName)}
function mi(...a){return a?a.join(","):"key"}
var ni=class{constructor(a,b,c){this.i=a;this.j=b;this.fields=c||[];this.h=new Map}clear(){this.h.clear()}};var oi=class extends ni{constructor(a,b){super(a,3,b)}};var pi=class extends ni{constructor(a,b){super(a,2,b)}record(a,...b){b=[b];const c=Kg(this,b);c?c.push(new li(a)):(b=mi([b]),this.h.set(b,[new li(a)]))}};function qi(a,b){this.type=a;this.h=this.target=b;this.defaultPrevented=this.j=!1}
qi.prototype.stopPropagation=function(){this.j=!0};
qi.prototype.preventDefault=function(){this.defaultPrevented=!0};function ri(a,b){qi.call(this,a?a.type:"");this.relatedTarget=this.h=this.target=null;this.button=this.screenY=this.screenX=this.clientY=this.clientX=0;this.key="";this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.altKey=this.ctrlKey=!1;this.state=null;this.pointerId=0;this.pointerType="";this.i=null;a&&this.init(a,b)}
va(ri,qi);
ri.prototype.init=function(a,b){const c=this.type=a.type,d=a.changedTouches&&a.changedTouches.length?a.changedTouches[0]:null;this.target=a.target||a.srcElement;this.h=b;b=a.relatedTarget;b||(c=="mouseover"?b=a.fromElement:c=="mouseout"&&(b=a.toElement));this.relatedTarget=b;d?(this.clientX=d.clientX!==void 0?d.clientX:d.pageX,this.clientY=d.clientY!==void 0?d.clientY:d.pageY,this.screenX=d.screenX||0,this.screenY=d.screenY||0):(this.clientX=a.clientX!==void 0?a.clientX:a.pageX,this.clientY=a.clientY!==
void 0?a.clientY:a.pageY,this.screenX=a.screenX||0,this.screenY=a.screenY||0);this.button=a.button;this.keyCode=a.keyCode||0;this.key=a.key||"";this.charCode=a.charCode||(c=="keypress"?a.keyCode:0);this.ctrlKey=a.ctrlKey;this.altKey=a.altKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.pointerId=a.pointerId||0;this.pointerType=a.pointerType;this.state=a.state;this.i=a;a.defaultPrevented&&ri.Ea.preventDefault.call(this)};
ri.prototype.stopPropagation=function(){ri.Ea.stopPropagation.call(this);this.i.stopPropagation?this.i.stopPropagation():this.i.cancelBubble=!0};
ri.prototype.preventDefault=function(){ri.Ea.preventDefault.call(this);const a=this.i;a.preventDefault?a.preventDefault():a.returnValue=!1};var si="closure_listenable_"+(Math.random()*1E6|0);var ti=0;function ui(a,b,c,d,e){this.listener=a;this.proxy=null;this.src=b;this.type=c;this.capture=!!d;this.handler=e;this.key=++ti;this.ac=this.jc=!1}
function vi(a){a.ac=!0;a.listener=null;a.proxy=null;a.src=null;a.handler=null}
;function wi(a){this.src=a;this.listeners={};this.h=0}
wi.prototype.add=function(a,b,c,d,e){const f=a.toString();a=this.listeners[f];a||(a=this.listeners[f]=[],this.h++);const g=xi(a,b,d,e);g>-1?(b=a[g],c||(b.jc=!1)):(b=new ui(b,this.src,f,!!d,e),b.jc=c,a.push(b));return b};
wi.prototype.remove=function(a,b,c,d){a=a.toString();if(!(a in this.listeners))return!1;const e=this.listeners[a];b=xi(e,b,c,d);return b>-1?(vi(e[b]),Array.prototype.splice.call(e,b,1),e.length==0&&(delete this.listeners[a],this.h--),!0):!1};
function yi(a,b){const c=b.type;c in a.listeners&&mb(a.listeners[c],b)&&(vi(b),a.listeners[c].length==0&&(delete a.listeners[c],a.h--))}
function xi(a,b,c,d){for(let e=0;e<a.length;++e){const f=a[e];if(!f.ac&&f.listener==b&&f.capture==!!c&&f.handler==d)return e}return-1}
;var zi="closure_lm_"+(Math.random()*1E6|0),Ai={},Bi=0;function Ci(a,b,c,d,e){if(d&&d.once)Di(a,b,c,d,e);else if(Array.isArray(b))for(let f=0;f<b.length;f++)Ci(a,b[f],c,d,e);else c=Ei(c),a&&a[si]?a.listen(b,c,ma(d)?!!d.capture:!!d,e):Fi(a,b,c,!1,d,e)}
function Fi(a,b,c,d,e,f){if(!b)throw Error("Invalid event type");const g=ma(e)?!!e.capture:!!e;let h=Gi(a);h||(a[zi]=h=new wi(a));c=h.add(b,c,d,g,f);if(!c.proxy){d=Hi();c.proxy=d;d.src=a;d.listener=c;if(a.addEventListener)e===void 0&&(e=!1),a.addEventListener(b.toString(),d,e);else if(a.attachEvent)a.attachEvent(Ii(b.toString()),d);else if(a.addListener&&a.removeListener)a.addListener(d);else throw Error("addEventListener and attachEvent are unavailable.");Bi++}}
function Hi(){function a(c){return b.call(a.src,a.listener,c)}
const b=Ji;return a}
function Di(a,b,c,d,e){if(Array.isArray(b))for(let f=0;f<b.length;f++)Di(a,b[f],c,d,e);else c=Ei(c),a&&a[si]?Ki(a,b,c,ma(d)?!!d.capture:!!d,e):Fi(a,b,c,!0,d,e)}
function Li(a,b,c,d,e){if(Array.isArray(b))for(let f=0;f<b.length;f++)Li(a,b[f],c,d,e);else(d=ma(d)?!!d.capture:!!d,c=Ei(c),a&&a[si])?a.i.remove(String(b),c,d,e):a&&(a=Gi(a))&&(b=a.listeners[b.toString()],a=-1,b&&(a=xi(b,c,d,e)),(c=a>-1?b[a]:null)&&Mi(c))}
function Mi(a){if(typeof a!=="number"&&a&&!a.ac){var b=a.src;if(b&&b[si])yi(b.i,a);else{var c=a.type,d=a.proxy;b.removeEventListener?b.removeEventListener(c,d,a.capture):b.detachEvent?b.detachEvent(Ii(c),d):b.addListener&&b.removeListener&&b.removeListener(d);Bi--;(c=Gi(b))?(yi(c,a),c.h==0&&(c.src=null,b[zi]=null)):vi(a)}}}
function Ii(a){return a in Ai?Ai[a]:Ai[a]="on"+a}
function Ji(a,b){if(a.ac)a=!0;else{b=new ri(b,this);const c=a.listener,d=a.handler||a.src;a.jc&&Mi(a);a=c.call(d,b)}return a}
function Gi(a){a=a[zi];return a instanceof wi?a:null}
var Ni="__closure_events_fn_"+(Math.random()*1E9>>>0);function Ei(a){if(typeof a==="function")return a;a[Ni]||(a[Ni]=function(b){return a.handleEvent(b)});
return a[Ni]}
;function Oi(){y.call(this);this.i=new wi(this);this.qa=this;this.Z=null}
va(Oi,y);Oi.prototype[si]=!0;r=Oi.prototype;r.addEventListener=function(a,b,c,d){Ci(this,a,b,c,d)};
r.removeEventListener=function(a,b,c,d){Li(this,a,b,c,d)};
function Pi(a,b){var c=a.Z;if(c){var d=[];for(var e=1;c;c=c.Z)d.push(c),++e}a=a.qa;c=b.type||b;typeof b==="string"?b=new qi(b,a):b instanceof qi?b.target=b.target||a:(e=b,b=new qi(c,a),oh(b,e));e=!0;let f,g;if(d)for(g=d.length-1;!b.j&&g>=0;g--)f=b.h=d[g],e=Qi(f,c,!0,b)&&e;b.j||(f=b.h=a,e=Qi(f,c,!0,b)&&e,b.j||(e=Qi(f,c,!1,b)&&e));if(d)for(g=0;!b.j&&g<d.length;g++)f=b.h=d[g],e=Qi(f,c,!1,b)&&e}
r.ba=function(){Oi.Ea.ba.call(this);this.removeAllListeners();this.Z=null};
r.listen=function(a,b,c,d){return this.i.add(String(a),b,!1,c,d)};
function Ki(a,b,c,d,e){a.i.add(String(b),c,!0,d,e)}
r.removeAllListeners=function(a){if(this.i){var b=this.i;a=a&&a.toString();let c=0;for(const d in b.listeners)if(!a||d==a){const e=b.listeners[d];for(let f=0;f<e.length;f++)++c,vi(e[f]);delete b.listeners[d];b.h--}b=c}else b=0;return b};
function Qi(a,b,c,d){b=a.i.listeners[String(b)];if(!b)return!0;b=b.concat();let e=!0;for(let f=0;f<b.length;++f){const g=b[f];if(g&&!g.ac&&g.capture==c){const h=g.listener,k=g.handler||g.src;g.jc&&yi(a.i,g);e=h.call(k,d)!==!1&&e}}return e&&!d.defaultPrevented}
;var Ri=typeof AsyncContext!=="undefined"&&typeof AsyncContext.Snapshot==="function"?a=>a&&AsyncContext.Snapshot.wrap(a):a=>a;function Si(a,b){a.o(b);a.i<100&&(a.i++,b.next=a.h,a.h=b)}
class Ti{constructor(a,b){this.j=a;this.o=b;this.i=0;this.h=null}get(){let a;this.i>0?(this.i--,a=this.h,this.h=a.next,a.next=null):a=this.j();return a}};class Ui{constructor(){this.i=this.h=null}add(a,b){const c=Vi.get();c.set(a,b);this.i?this.i.next=c:this.h=c;this.i=c}remove(){let a=null;this.h&&(a=this.h,this.h=this.h.next,this.h||(this.i=null),a.next=null);return a}}var Vi=new Ti(()=>new Wi,a=>a.reset());
class Wi{constructor(){this.next=this.scope=this.h=null}set(a,b){this.h=a;this.scope=b;this.next=null}reset(){this.next=this.scope=this.h=null}};let Xi,Yi=!1,Zi=new Ui,aj=(a,b)=>{Xi||$i();Yi||(Xi(),Yi=!0);Zi.add(a,b)},$i=()=>{const a=Promise.resolve(void 0);
Xi=()=>{a.then(bj)}};
function bj(){let a;for(;a=Zi.remove();){try{a.h.call(a.scope)}catch(b){uc(b)}Si(Vi,a)}Yi=!1}
;function cj(){}
function dj(a){let b=!1,c;return function(){b||(c=a(),b=!0);return c}}
;function ej(a){this.B=0;this.ob=void 0;this.ub=this.Ya=this.parent_=null;this.sc=this.Qc=!1;if(a!=cj)try{const b=this;a.call(void 0,function(c){fj(b,2,c)},function(c){fj(b,3,c)})}catch(b){fj(this,3,b)}}
function gj(){this.next=this.context=this.h=this.i=this.child=null;this.j=!1}
gj.prototype.reset=function(){this.context=this.h=this.i=this.child=null;this.j=!1};
var hj=new Ti(function(){return new gj},function(a){a.reset()});
function ij(a,b,c){const d=hj.get();d.i=a;d.h=b;d.context=c;return d}
function jj(a){return new ej(function(b,c){c(a)})}
ej.prototype.then=function(a,b,c){return kj(this,Ri(typeof a==="function"?a:null),Ri(typeof b==="function"?b:null),c)};
ej.prototype.$goog_Thenable=!0;function lj(a,b,c,d){mj(a,ij(b||cj,c||null,d))}
r=ej.prototype;r.finally=function(a){a=Ri(a);return new ej((b,c)=>{lj(this,d=>{a();b(d)},d=>{a();
c(d)})})};
r.Jc=function(a,b){return kj(this,null,Ri(a),b)};
r.catch=ej.prototype.Jc;r.cancel=function(a){if(this.B==0){const b=new nj(a);aj(function(){oj(this,b)},this)}};
function oj(a,b){if(a.B==0)if(a.parent_){var c=a.parent_;if(c.Ya){var d=0,e=null,f=null;for(let g=c.Ya;g&&(g.j||(d++,g.child==a&&(e=g),!(e&&d>1)));g=g.next)e||(f=g);e&&(c.B==0&&d==1?oj(c,b):(f?(d=f,d.next==c.ub&&(c.ub=d),d.next=d.next.next):pj(c),qj(c,e,3,b)))}a.parent_=null}else fj(a,3,b)}
function mj(a,b){a.Ya||a.B!=2&&a.B!=3||rj(a);a.ub?a.ub.next=b:a.Ya=b;a.ub=b}
function kj(a,b,c,d){const e=ij(null,null,null);e.child=new ej(function(f,g){e.i=b?function(h){try{const k=b.call(d,h);f(k)}catch(k){g(k)}}:f;
e.h=c?function(h){try{const k=c.call(d,h);k===void 0&&h instanceof nj?g(h):f(k)}catch(k){g(k)}}:g});
e.child.parent_=a;mj(a,e);return e.child}
r.Hf=function(a){this.B=0;fj(this,2,a)};
r.If=function(a){this.B=0;fj(this,3,a)};
function fj(a,b,c){if(a.B==0){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.B=1;a:{var d=c,e=a.Hf,f=a.If;if(d instanceof ej){lj(d,e,f,a);var g=!0}else{if(d)try{var h=!!d.$goog_Thenable}catch(k){h=!1}else h=!1;if(h)d.then(e,f,a),g=!0;else{if(ma(d))try{const k=d.then;if(typeof k==="function"){sj(d,k,e,f,a);g=!0;break a}}catch(k){f.call(a,k);g=!0;break a}g=!1}}}g||(a.ob=c,a.B=b,a.parent_=null,rj(a),b!=3||c instanceof nj||tj(a,c))}}
function sj(a,b,c,d,e){function f(k){h||(h=!0,d.call(e,k))}
function g(k){h||(h=!0,c.call(e,k))}
let h=!1;try{b.call(a,g,f)}catch(k){f(k)}}
function rj(a){a.Qc||(a.Qc=!0,aj(a.He,a))}
function pj(a){let b=null;a.Ya&&(b=a.Ya,a.Ya=b.next,b.next=null);a.Ya||(a.ub=null);return b}
r.He=function(){let a;for(;a=pj(this);)qj(this,a,this.B,this.ob);this.Qc=!1};
function qj(a,b,c,d){if(c==3&&b.h&&!b.j)for(;a&&a.sc;a=a.parent_)a.sc=!1;if(b.child)b.child.parent_=null,uj(b,c,d);else try{b.j?b.i.call(b.context):uj(b,c,d)}catch(e){vj.call(null,e)}Si(hj,b)}
function uj(a,b,c){b==2?a.i.call(a.context,c):a.h&&a.h.call(a.context,c)}
function tj(a,b){a.sc=!0;aj(function(){a.sc&&vj.call(null,b)})}
var vj=uc;function nj(a){Ca.call(this,a)}
va(nj,Ca);nj.prototype.name="cancel";function wj(a,b){Oi.call(this);this.j=a||1;this.h=b||t;this.o=ra(this.Ff,this);this.u=ta()}
va(wj,Oi);r=wj.prototype;r.enabled=!1;r.Ia=null;r.setInterval=function(a){this.j=a;this.Ia&&this.enabled?(this.stop(),this.start()):this.Ia&&this.stop()};
r.Ff=function(){if(this.enabled){const a=ta()-this.u;a>0&&a<this.j*.8?this.Ia=this.h.setTimeout(this.o,this.j-a):(this.Ia&&(this.h.clearTimeout(this.Ia),this.Ia=null),Pi(this,"tick"),this.enabled&&(this.stop(),this.start()))}};
r.start=function(){this.enabled=!0;this.Ia||(this.Ia=this.h.setTimeout(this.o,this.j),this.u=ta())};
r.stop=function(){this.enabled=!1;this.Ia&&(this.h.clearTimeout(this.Ia),this.Ia=null)};
r.ba=function(){wj.Ea.ba.call(this);this.stop();delete this.h};function ec(a,b,...c){a.i.has(b)||a.i.set(b,new pi(b,c))}
function ic(a,b,...c){a.i.has(b)||a.i.set(b,new oi(b,c))}
function xj(a){a.h.enabled||a.h.start();a.u++;a.u>=a.j&&a.o()}
function yj(a){for(let b=0;b<a.length;b++)a[b].clear()}
function zj(a,b){return a.F.has(b)?void 0:a.i.get(b)}
function jc(a,b,...c){if((b=zj(a,b))&&b instanceof oi){c=[c];var d=0,e;(e=(e=Kg(b,[c]))&&e.length?e[0]:void 0)&&(d=e.h);d+=1;c=mi([c]);b.h.set(c,[new li(d)]);xj(a)}}
var Aj=class extends y{constructor(a){super();this.G=a;this.u=0;this.j=100;this.A=!1;this.i=new Map;this.F=new Set;this.flushInterval=3E4;this.h=new wj(this.flushInterval);this.h.listen("tick",this.o,!1,this);Ob(this,this.h)}sendIsolatedPayload(a){this.A=a;this.j=1}o(){const a=[...this.i.values()].filter(b=>b.h.size);
a.length&&this.G.flush(a,this.A);yj(a);this.u=0;this.h.enabled&&this.h.stop()}record(a,b,...c){(a=zj(this,a))&&a instanceof pi&&(a.record(b,c),xj(this))}};function Bj(a){switch(a){case 200:return 0;case 400:return 3;case 401:return 16;case 403:return 7;case 404:return 5;case 409:return 10;case 412:return 9;case 429:return 8;case 499:return 1;case 500:return 2;case 501:return 12;case 503:return 14;case 504:return 4;default:return 2}}
function Cj(a){switch(a){case 0:return"OK";case 1:return"CANCELLED";case 2:return"UNKNOWN";case 3:return"INVALID_ARGUMENT";case 4:return"DEADLINE_EXCEEDED";case 5:return"NOT_FOUND";case 6:return"ALREADY_EXISTS";case 7:return"PERMISSION_DENIED";case 16:return"UNAUTHENTICATED";case 8:return"RESOURCE_EXHAUSTED";case 9:return"FAILED_PRECONDITION";case 10:return"ABORTED";case 11:return"OUT_OF_RANGE";case 12:return"UNIMPLEMENTED";case 13:return"INTERNAL";case 14:return"UNAVAILABLE";case 15:return"DATA_LOSS";
default:return""}}
;var Dj=class extends Error{constructor(a,b){super(b);this.code=a;this.metadata={};this.name="RpcError";Object.setPrototypeOf(this,new.target.prototype)}toString(){let a=`RpcError(${Cj(this.code)||String(this.code)})`;this.message&&(a+=": "+this.message);return a}};function Ej(){}
Ej.prototype.serialize=function(a){const b=[];Fj(this,a,b);return b.join("")};
function Fj(a,b,c){if(b==null)c.push("null");else{if(typeof b=="object"){if(Array.isArray(b)){var d=b;b=d.length;c.push("[");var e="";for(var f=0;f<b;f++)c.push(e),Fj(a,d[f],c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");e="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(f=b[d],typeof f!="function"&&(c.push(e),Gj(d,c),c.push(":"),Fj(a,f,c),e=","));c.push("}");return}}switch(typeof b){case "string":Gj(b,c);break;
case "number":c.push(isFinite(b)&&!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var Hj={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\v":"\\u000b"},Ij=/\uffff/.test("\uffff")?/[\\"\x00-\x1f\x7f-\uffff]/g:/[\\"\x00-\x1f\x7f-\xff]/g;function Gj(a,b){b.push('"',a.replace(Ij,function(c){let d=Hj[c];d||(d="\\u"+(c.charCodeAt(0)|65536).toString(16).slice(1),Hj[c]=d);return d}),'"')}
;function Jj(){Oi.call(this);this.headers=new Map;this.h=!1;this.M=null;this.o=this.Y="";this.j=this.P=this.A=this.G=!1;this.F=0;this.u=null;this.la="";this.ga=!1}
va(Jj,Oi);var Kj=/^https?$/i,Lj=["POST","PUT"],Mj=[];function Nj(a,b,c,d,e,f,g){const h=new Jj;Mj.push(h);b&&h.listen("complete",b);Ki(h,"ready",h.re);f&&(h.F=Math.max(0,f));g&&(h.ga=g);h.send(a,c,d,e)}
r=Jj.prototype;r.re=function(){this.dispose();mb(Mj,this)};
r.send=function(a,b,c,d){if(this.M)throw Error("[goog.net.XhrIo] Object is active with another request="+this.Y+"; newUri="+a);b=b?b.toUpperCase():"GET";this.Y=a;this.o="";this.G=!1;this.h=!0;this.M=new XMLHttpRequest;this.M.onreadystatechange=Ri(ra(this.Ad,this));try{this.getStatus(),this.P=!0,this.M.open(b,String(a),!0),this.P=!1}catch(f){this.getStatus();Oj(this,f);return}a=c||"";c=new Map(this.headers);if(d)if(Object.getPrototypeOf(d)===Object.prototype)for(var e in d)c.set(e,d[e]);else if(typeof d.keys===
"function"&&typeof d.get==="function")for(const f of d.keys())c.set(f,d.get(f));else throw Error("Unknown input type for opt_headers: "+String(d));d=Array.from(c.keys()).find(f=>"content-type"==f.toLowerCase());
e=t.FormData&&a instanceof t.FormData;!(gb(Lj,b)>=0)||d||e||c.set("Content-Type","application/x-www-form-urlencoded;charset=utf-8");for(const [f,g]of c)this.M.setRequestHeader(f,g);this.la&&(this.M.responseType=this.la);"withCredentials"in this.M&&this.M.withCredentials!==this.ga&&(this.M.withCredentials=this.ga);try{this.u&&(clearTimeout(this.u),this.u=null),this.F>0&&(this.getStatus(),this.u=setTimeout(this.Gf.bind(this),this.F)),this.getStatus(),this.A=!0,this.M.send(a),this.A=!1}catch(f){this.getStatus(),
Oj(this,f)}};
r.Gf=function(){typeof ia!="undefined"&&this.M&&(this.o="Timed out after "+this.F+"ms, aborting",this.getStatus(),Pi(this,"timeout"),this.abort(8))};
function Oj(a,b){a.h=!1;a.M&&(a.j=!0,a.M.abort(),a.j=!1);a.o=b;Pj(a);Qj(a)}
function Pj(a){a.G||(a.G=!0,Pi(a,"complete"),Pi(a,"error"))}
r.abort=function(){this.M&&this.h&&(this.getStatus(),this.h=!1,this.j=!0,this.M.abort(),this.j=!1,Pi(this,"complete"),Pi(this,"abort"),Qj(this))};
r.ba=function(){this.M&&(this.h&&(this.h=!1,this.j=!0,this.M.abort(),this.j=!1),Qj(this,!0));Jj.Ea.ba.call(this)};
r.Ad=function(){this.I||(this.P||this.A||this.j?Rj(this):this.nf())};
r.nf=function(){Rj(this)};
function Rj(a){if(a.h&&typeof ia!="undefined")if(a.A&&(a.M?a.M.readyState:0)==4)setTimeout(a.Ad.bind(a),0);else if(Pi(a,"readystatechange"),a.isComplete()){a.getStatus();a.h=!1;try{if(Sj(a))Pi(a,"complete"),Pi(a,"success");else{try{var b=(a.M?a.M.readyState:0)>2?a.M.statusText:""}catch(c){b=""}a.o=b+" ["+a.getStatus()+"]";Pj(a)}}finally{Qj(a)}}}
function Qj(a,b){if(a.M){a.u&&(clearTimeout(a.u),a.u=null);const c=a.M;a.M=null;b||Pi(a,"ready");try{c.onreadystatechange=null}catch(d){}}}
r.isActive=function(){return!!this.M};
r.isComplete=function(){return(this.M?this.M.readyState:0)==4};
function Sj(a){var b=a.getStatus();a:switch(b){case 200:case 201:case 202:case 204:case 206:case 304:case 1223:var c=!0;break a;default:c=!1}if(!c){if(b=b===0)a=String(a.Y).match(xb)[1]||null,!a&&t.self&&t.self.location&&(a=t.self.location.protocol.slice(0,-1)),b=!Kj.test(a?a.toLowerCase():"");c=b}return c}
r.getStatus=function(){try{return(this.M?this.M.readyState:0)>2?this.M.status:-1}catch(a){return-1}};
r.getLastError=function(){return typeof this.o==="string"?this.o:String(this.o)};var fi=class{send(a,b=()=>{},c=()=>{}){Nj(a.url,d=>{d=d.target;
if(Sj(d)){try{var e=d.M?d.M.responseText:""}catch(f){e=""}b(e)}else c(d.getStatus())},a.requestType,a.body,a.Fc,a.timeoutMillis,a.withCredentials)}qc(){return 1}};var Uj=class{constructor(a,b){this.logger=a;this.event=b;this.startTime=Tj()}done(){this.logger.j(this.event,Tj()-this.startTime)}};function Vj(a,b,c){const d=Tj();b=b();a.j(c,Tj()-d);return b}
var Wj=class extends cc{constructor(){super(...arguments)}},Xj=class extends Wj{o(){}h(){}j(){}ta(){}F(){}A(){}i(){}P(){}u(){}G(){}},Yj=class extends Wj{constructor(a){super();this.logger=a;this.addOnDisposeCallback(()=>void this.logger.dispose())}update(a){this.logger.dispose();
this.logger=a}h(a){this.logger.h(a)}j(a,b){this.logger.j(a,b)}ta(a){this.logger.ta(a)}F(a){this.logger.F(a)}A(a,b){this.logger.A(a,b)}i(){this.logger.i()}P(a){this.logger.P(a)}u(a){this.logger.u(a)}G(a){this.logger.G(a)}o(a){this.logger.o(a)}};function Zj(a,b,c,d){a=hi(ei(di(new ji,a))).Oc();b.length&&gi(a,wg(new xg,b));d!==void 0&&(a.hb=d);const e=new ki(ii(a));Ob(e,a);const f=new Aj({flush(g){try{e.flush(g)}catch(h){c(h)}}});f.addOnDisposeCallback(()=>{setTimeout(()=>{try{f.o()}finally{e.dispose()}})});
f.j=1E5;f.flushInterval=3E4;f.h.setInterval(3E4);return f}
function ak(a){if(a.timer===void 0){const b=Math.max(0,a.h+a.i-Tj());a.timer=setTimeout(()=>{try{a.callback()}finally{a.h=Tj(),a.timer=void 0}},b)}}
class bk extends y{constructor(a,b){super();this.callback=a;this.i=b;this.h=-b;this.addOnDisposeCallback(()=>void clearTimeout(this.timer))}}
class ck extends Wj{constructor(a,b){super();this.metrics=a;this.ka=b}o(a){this.metrics.Bf.record(a,this.ka)}h(a){this.metrics.eventCount.h(a,this.ka)}j(a,b){this.metrics.Ge.record(b,a,this.ka)}ta(a){this.metrics.errorCount.h(a,this.ka)}P(a){this.metrics.Mf.h(a,this.ka)}u(a){this.metrics.oe.h(a,this.ka)}G(a){this.metrics.Lf.h(a,this.ka)}F(a){this.metrics.payloadSize.record(a,this.ka)}A(a,b){this.metrics.mf.record(b,a,this.ka)}}function dk(a,b=[]){return new ek(a,b)}
var ek=class extends ck{constructor(a,b=[]){const c={ka:a.ka||"_",Rc:a.Rc||[],Vc:a.Vc|0,hb:a.hb,Ac:a.Ac||(()=>{}),
Mb:a.Mb||((e,f)=>Zj(e,f,c.Ac,c.hb))},d=c.Mb("53",c.Rc.concat(b));
super({Bf:new fc(d),errorCount:new mc(d),eventCount:new kc(d),Ge:new lc(d),Mi:new hc(d),Mf:new nc(d),oe:new oc(d),Lf:new pc(d),payloadSize:new qc(d),mf:new rc(d)},c.ka);this.options=c;this.service=d;this.ga=!a.Mb;this.Y=new bk(()=>void this.service.o(),c.Vc);
this.addOnDisposeCallback(()=>{this.Y.dispose();this.ga&&this.service.dispose()});
b.slice().sort(pb)}i(){ak(this.Y)}};function Tj(){return globalThis.performance?.now?.()??Date.now()}
;var fk=class extends G{constructor(a){super(a)}};var gk=class extends G{constructor(a){super(a)}};var hk=class extends G{constructor(a){super(a,0,"bfkj")}},ik=function(a){return Ed(b=>b instanceof a&&!yd(b))}(hk);
hk.gf="bfkj";var Zb=class extends G{constructor(a){super(a)}};var jk=class extends G{constructor(a){super(a)}},kk=vg(jk);class lk{constructor(){this.promise=new Promise((a,b)=>{this.resolve=a;this.reject=b})}}
;function mk(a,b){if(a.disable)return new Xj;b=b?Xb(b):[];return dk({ka:a.ka,Rc:a.Je,Vc:a.hf,hb:a.hb,Ac:a.Ac,Mb:a.Mb},b)}
class nk extends y{constructor(a){super();this.j=Math.floor(Math.random()*200);this.h=new jk;let b;if("challenge"in a&&ik(a.challenge)){b=sf(a.challenge,4,void 0,Dd);var c=sf(a.challenge,5,void 0,Dd);sf(a.challenge,7,void 0,Dd)&&(this.h=kk(sf(a.challenge,7,void 0,Dd)))}else({program:b,globalName:c}=a);this.addOnDisposeCallback(async()=>{const {Af:n}=await this.i;n?.()});
this.logger=mk(a.Gb||{},this.h);Ob(this,this.logger);const d=new lk;this.i=d.promise;this.logger.h("t");const e=this.logger.share(),f=new Uj(e,"t"),g=(n,m,u,p)=>{if(!this.logger.I){var z="k";m?z="h":u&&(z="u");z!=="k"?p!==0&&(this.logger.h(z),this.logger.j(z,n)):this.j<=0?(this.logger.h(z),this.logger.j(z,n),this.j=Math.floor(Math.random()*200)):this.j--}},h=(n,m,u,p)=>{Promise.resolve().then(()=>{f.done();
e.i();e.dispose();d.resolve({ge:n,Af:m,rf:u,pe:p})})},k=[(n,m)=>{this.logger.j(n,m)},
n=>{this.logger.ta(n)},
n=>{this.logger.F(n)},
(n,m)=>{this.logger.A(n,m)}];
if(!t[c])throw this.logger.ta(25),Error("EGOU");if(!t[c].a)throw this.logger.ta(26),Error("ELIU");try{const n=t[c].a;c=[];const m=[];var l=Xb(this.h);for(let z=0;z<l.length;z++)c.push(l[z]),m.push(1);const u=ac(this.h);for(l=0;l<u.length;l++)c.push(u[l]),m.push(2);const [p]=n(b,h,!0,a.Rd,g,[c,m],sf(this.h,5),!1,k);this.o=p;this.Kb=d.promise.then(()=>{})}catch(n){throw this.logger.ta(28),n;
}}snapshot(a){if(this.I)throw Error("Already disposed");this.logger.h("n");const b=this.logger.share();return this.i.then(({ge:c})=>new Promise(d=>{const e=new Uj(b,"n");c(f=>{e.done();b.o(f.length);b.i();b.dispose();d(f)},[a.Ka,
a.Ic,a.Ud,a.gd])}))}Kd(a){if(this.I)throw Error("Already disposed");
this.logger.h("n");const b=Vj(this.logger,()=>this.o([a.Ka,a.Ic,a.Ud,a.gd]),"n");
this.logger.o(b.length);this.logger.i();return b}Xb(a){this.i.then(({rf:b})=>{b?.(a)})}kc(a,b){return this.i.then(({pe:c})=>c?.(a,b,!1))}cc(){return this.logger.share()}}
;function ok(a){if(!a)return null;a=xe(Ze(a,4,void 0,Ye));return a===null||a===void 0?null:Ia(a)}
;function pk(){qk.instance||(qk.instance=new qk);return qk.instance}
function rk(a,b,c,d){if(!b&&!c)return Promise.resolve();if(!d)return sk(b,c);let e;(e=a.promises)[d]||(e[d]=new Promise((f,g)=>{sk(b,c).then(()=>{a.h=d;f()},h=>{delete a.promises[d];
g(h)})}));
return a.promises[d]}
function tk(a,b){return rk(a,nf(b,fk,1,Dd),nf(b,gk,2,Dd),sf(b,3,void 0,Dd))}
var qk=class{constructor(){this.promises={};this.h=null}};function sk(a,b){return b?uk(b):a?vk(a):Promise.resolve()}
function uk(a){return new Promise((b,c)=>{const d=sh("SCRIPT"),e=ok(a);ab(d,e);d.onload=()=>{uh(d);b()};
d.onerror=()=>{uh(d);c(Error("EWLS"))};
(document.getElementsByTagName("HEAD")[0]||document.documentElement).appendChild(d)})}
function vk(a){return new Promise(b=>{const c=sh("SCRIPT");if(a){var d=xe(Ze(a,6,void 0,Ye));d=d===null||d===void 0?null:Ya(d)}else d=null;c.textContent=Za(d);$a(c);(document.getElementsByTagName("HEAD")[0]||document.documentElement).appendChild(c);uh(c);b()})}
;function wk(a,b){return jf(a,1,we(b))}
function xk(a,b){return jf(a,2,we(b))}
var yk=class extends G{constructor(a){super(a)}};async function zk(a,b,c,d=pk(),e=Promise.resolve(void 0),f){await 0;let g;for(;;){let h=null;if(g){Ak(a,7);try{h=await Bk(g.snapshot({}),f.ue,()=>Promise.resolve("E:CTO"))}catch(n){h="E:UCE"}}let k;
const l=new Rh(g?f.Ce:f.De,f.Ee,f.Fe,f.Be);for(let n=1;n<=f.maxAttempts;n++){if(n!==1){Ak(a,0);a.h=new Ck(l.getValue(),f.Kc,f.Od);const m=await a.h.promise;a.h=void 0;m===1?(n=1,l.reset()):Sh(l)}try{let m;c?m=c:(Ak(a,5),m=await Bk(Dk(b,d.h,h),f.Me,()=>Promise.reject(Error("RGF:Fetch timed out"))));
Ak(a,3);await Bk(tk(d,m),f.bf,()=>Promise.reject(Error("DTZ:Script timed out")));
Ak(a,8);await e;const u=new nk({challenge:m,Gb:a.options.Gb,Rd:a.options.Rd});await Bk(u.Kb,f.zf,()=>Promise.reject(Error("QEG:Setup timed out")));
k=u;break}catch(m){a.handleError(m),Ek(a)}}if(a.I)break;k&&(c=void 0,Fk(a,g),g=k,Gk(a,k),Ek(a));Ak(a,2);a.h=new Ck(f.Fd,f.Kc,f.Od);a.isPaused&&a.h.pause();await a.h.promise;a.h=void 0;if(a.I)break}g?.dispose()}
function Hk(a){a.F=Error("Cancelled by dispose");a.u.resolve();bc(a.A.promise);a.A.reject(Error("Cancelled by dispose"));a.logger.dispose();Promise.all(a.o).then(async()=>{a.i?.dispose();a.i=void 0});
a.o=[];a.h?.i();bc(a.j.promise);a.j.reject(Error("Cancelled by dispose"))}
function Ik(a,b){const c=a.Bc;a.Bc=()=>{c();b()}}
function Gk(a,b){a.I||(a.i=b,a.logger.update(b.cc()),a.u.resolve(),a.A.resolve(void 0),a.Bc())}
function Fk(a,b){b&&(Promise.all(a.o).then(()=>void b.dispose()),a.o=[])}
function Ak(a,b){a.P=b;a.options.ti?.(b)}
function Ek(a){a.I||(a.j.resolve(),a.j=new lk)}
var Lk=class extends y{constructor(a){super();this.options=a;this.A=new lk;this.Kb=this.A.promise;this.u=new lk;this.P=1;this.j=new lk;this.o=[];this.isPaused=!1;this.Bc=a.Bc||(()=>{});
this.logger=new Yj(mk(a.Gb||{}));zk(this,a.Oa,a.Se,a.Ei,a.Gi,{...Jk,...(a.Nb||{})});this.addOnDisposeCallback(()=>void Hk(this))}async snapshot(a){if(this.I)throw Error("Already disposed");
this.i||this.F||await this.u.promise;if(this.i)return await this.i.snapshot(a);throw this.F;}pause(){this.I||this.isPaused||(this.isPaused=!0,this.h&&this.h.pause())}resume(){!this.I&&this.isPaused&&(this.isPaused=!1,this.h&&this.h.resume())}async checkForRefresh(){if(this.I)throw Error("Already disposed");if(this.h){var a=this.h;a.isExpired()?(Kk(a),a.Gc(0),a=!0):a=!1;a&&await this.j.promise}else await this.j.promise}async G(){if(this.I)throw Error("Already disposed");this.h?.i();await this.j.promise}Xb(a){this.i?.Xb?.(a)}kc(a,
b){return this.i?.kc?.(a,b)??Promise.resolve()}handleError(a){this.I||(this.F=a,this.u.resolve(),this.options.zc?.(a))}cc(){return this.logger.share()}},Jk={Fd:432E5,Kc:3E5,Od:10,ue:1E4,Me:3E4,bf:3E4,zf:6E4,De:1E3,Ce:6E4,Ee:6E5,Fe:.25,Be:2,maxAttempts:10};function Bk(a,b,c){let d;const e=new Promise(f=>{d=setTimeout(f,b)});
return Promise.race([a.finally(()=>void clearTimeout(d)),
e.then(c)])}
function Mk(a,b){a.endTimeMs=Date.now()+b;a.tick()}
function Kk(a){a.h&&(clearTimeout(a.h),a.h=null)}
class Ck{constructor(a,b,c){this.endTimeMs=0;this.h=null;this.isPaused=!1;this.tick=()=>{if(!this.isPaused){var d=this.endTimeMs-Date.now();d<=this.j?(this.h=null,this.Gc(0)):this.h=setTimeout(this.tick,Math.min(d,this.Kc))}};
this.Kc=b;this.j=c;this.promise=new Promise(d=>{this.Gc=d});
Mk(this,a)}pause(){this.isPaused||(this.isPaused=!0,Kk(this))}resume(){this.isPaused&&(this.isPaused=!1,this.tick())}i(){Kk(this);this.endTimeMs=0;this.isPaused=!1;this.Gc(1)}isExpired(){return Date.now()>this.endTimeMs}};function Nk(a,b){try{return globalThis.sessionStorage.setItem(a,b),!0}catch(c){return!1}}
const Ok=Math.imul??((a,b)=>a*b|0);
function Pk(a,b=0,c=a.length,d){let e=0;for(d&&(e=Pk(d));b<c;b++)e=Ok(31,e)+(typeof a==="string"?a.charCodeAt(b):a[b])|0;return e}
const Qk=[196,200,224,18];function Rk(a){const [b,c]=[Pk(a,0,a.length>>1,Qk),Pk(a,a.length>>1)];return b.toString(16)+c.toString(16)}
function Sk(a,b){var c=[Pk(b,0,b.length>>1,void 0),Pk(b,b.length>>1)];a=new Uint32Array(a.buffer);b=a[0];const [d,e]=c;for(c=1;c<a.length;c+=2){var f=b,g=c,h=d,k=e;for(let l=0;l<22;l++)g=g>>>8|g<<24,g+=f|0,g^=h+38293,f=f<<3|f>>>29,f^=g,k=k>>>8|k<<24,k+=h|0,k^=l+38293,h=h<<3|h>>>29,h^=k;f=[f,g];a[c]^=f[0];c+1<a.length&&(a[c+1]^=f[1])}}
function Tk(a,b,c,d,e){const f=(4-(Qk.length+c.length)%4)%4,g=new Uint8Array(4+f+Qk.length+4+c.length),h=new DataView(g.buffer);let k=0;h.setUint32(k,Math.random()*4294967295);k=k+4+f;g.set(Qk,k);k+=Qk.length;h.setUint32(k,e);g.set(c,k+4);Sk(g,d);return a.oa(b,l=>void globalThis.sessionStorage.removeItem(l))?Nk(b,Vc(g))?"s":"t":"i"}
function Uk(a,b){var c=globalThis.sessionStorage.getItem(a);if(!c)return["m"];let d;try{d=Xc(c),Sk(d,b)}catch(e){return globalThis.sessionStorage.removeItem(a),["c"]}for(b=4;b<7&&d[b]===0;)b++;for(c=0;c<Qk.length;c++)if(d[b++]!==Qk[c])return globalThis.sessionStorage.removeItem(a),["d"];c=(new DataView(d.buffer)).getUint32(b);return Math.floor(Date.now()/1E3)>=c?(globalThis.sessionStorage.removeItem(a),["e"]):["a",new Uint8Array(d.buffer,b+4)]}
function Vk(a){var b=globalThis.sessionStorage.getItem("iU5q-!O9@$");if(!b)return new Wk(a);var c=b.split(",");if(c.length<2)return globalThis.sessionStorage.removeItem("iU5q-!O9@$"),new Wk(a);b=c.slice(1);b.length===1&&b[0]===""&&(b=[]);c=Number(c[0]);return isNaN(c)||c<0||c>b.length?(globalThis.sessionStorage.removeItem("iU5q-!O9@$"),new Wk(a)):new Wk(a,c,b)}
class Wk{constructor(a,b=0,c=[]){this.maxItems=a;this.h=b;this.i=c}serialize(){return String(this.h)+","+this.i.join()}oa(a,b){let c=void 0;if(this.i[this.h]!==a){const d=this.i.indexOf(a);d!==-1?(this.i.splice(d,1),d<this.h&&this.h--,this.i.splice(this.h,0,a)):(c=this.i[this.h],this.i[this.h]=a)}this.h=(this.h+1)%this.maxItems;a=Nk("iU5q-!O9@$",this.serialize());c&&a&&b(c);return a}}
var Ub=class{constructor(a,b){this.logger=b;try{var c=globalThis.sessionStorage&&!!globalThis.sessionStorage.getItem&&!!globalThis.sessionStorage.setItem&&!!globalThis.sessionStorage.removeItem}catch(d){c=!1}c&&(this.index=Vk(a))}h(a,b,c,d){const e=this.index?Vj(this.logger,()=>Tk(this.index,Rk(a),b,c,d),"W"):"u";
this.logger.G(e)}i(a,b){const [c,d]=this.index?Vj(this.logger,()=>Uk(Rk(a),b),"R"):["u"];
this.logger.u(c);return d}};var Xk={toString:function(a){let b=[],c=0;a-=-2147483648;b[c++]="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".charAt(a%52);for(a=Math.floor(a/52);a>0;)b[c++]="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".charAt(a%62),a=Math.floor(a/62);return b.join("")}};function Yk(a){function b(){c-=d;c-=e;c^=e>>>13;d-=e;d-=c;d^=c<<8;e-=c;e-=d;e^=d>>>13;c-=d;c-=e;c^=e>>>12;d-=e;d-=c;d^=c<<16;e-=c;e-=d;e^=d>>>5;c-=d;c-=e;c^=e>>>3;d-=e;d-=c;d^=c<<10;e-=c;e-=d;e^=d>>>15}
a=Zk(a);let c=2654435769,d=2654435769,e=314159265;const f=a.length;let g=f,h=0;for(;g>=12;g-=12,h+=12)c+=$k(a,h),d+=$k(a,h+4),e+=$k(a,h+8),b();e+=f;switch(g){case 11:e+=a[h+10]<<24;case 10:e+=a[h+9]<<16;case 9:e+=a[h+8]<<8;case 8:d+=a[h+7]<<24;case 7:d+=a[h+6]<<16;case 6:d+=a[h+5]<<8;case 5:d+=a[h+4];case 4:c+=a[h+3]<<24;case 3:c+=a[h+2]<<16;case 2:c+=a[h+1]<<8;case 1:c+=a[h+0]}b();return Xk.toString(e)}
function Zk(a){const b=[];for(let c=0;c<a.length;c++)b.push(a.charCodeAt(c));return b}
function $k(a,b){return a[b+0]+(a[b+1]<<8)+(a[b+2]<<16)+(a[b+3]<<24)}
;function al(a,b){const c=setTimeout(()=>{a.j.resolve()},b);
a.addOnDisposeCallback(()=>void clearTimeout(c))}
var bl=class extends y{constructor(a){super();this.logger=a;this.j=new lk}yc(a,b){const c=this.eb(a);b?.(c);return Vj(this.logger,()=>Vc(c,2),this.i)}Yc(a,b,c){return Vj(this.logger,()=>b?this.yc(a,c):this.eb(a,c),this.h)}},cl=class extends bl{constructor(a,b,c,d){super(a);
this.o=b;this.A=c;this.h="m";this.i="x";this.u=0;al(this,d)}eb(a,b){this.logger.h(this.h);++this.u>=this.A&&this.j.resolve();const c=a();a=Vj(this.logger,()=>this.o(c),"C");
if(a===void 0)throw new x(17,"YNJ:Undefined");if(!(a instanceof Uint8Array))throw new x(18,"ODM:Invalid");b?.(a);return a}},dl=class extends bl{constructor(a,b,c){super(a);this.o=b;this.h="f";this.i="z";al(this,c)}eb(){return this.o}},el=class extends bl{constructor(a,b,c){super(a);this.o=b;this.h="w";this.i="z";al(this,c)}eb(){return Vj(this.logger,()=>Xc(this.o),"d")}yc(){return this.o}};
function fl(a,b){var c=`${b(a.error.message)}:${b(a.error.stack)}`.substring(0,2048);b=c.length+1;c=gl(c);const d=new Uint8Array(4+c.length);d.set([42,b&127|128,b>>7,a.error.code]);d.set(c,4);return d}
var hl=class extends bl{constructor(a,b){super(a);this.error=b;this.h="e";this.i="y"}eb(){if(this.o)return this.o;this.o=fl(this,a=>"_"+Yk(a));
return fl(this,a=>a)}},il=class extends bl{constructor(a,b){super(a);
this.clientState=b;this.h="S";this.i="q"}eb(){var a=Math.floor(Date.now()/1E3),b=[Math.random()*255,Math.random()*255],c=b.concat([0,this.clientState],[a>>24&255,a>>16&255,a>>8&255,a&255]);a=new Uint8Array(2+c.length);a[0]=34;a[1]=c.length;a.set(c,2);c=a.subarray(2);b=b.length;for(let d=b;d<c.length;++d)c[d]^=c[d%b];this.logger.P(this.clientState);return a}};function gl(a){return globalThis.TextEncoder?(new TextEncoder).encode(a):vc(a)}
;var jl={Ne:3E4,Cf:2E4};function Vb(a,b){a.logger.ta(b.code);a.onError(b);return b}
async function kl(a){let b=void 0;a.j++;const c=new lk;a.vm instanceof Lk&&a.vm.o.push(c.promise);if(a.ld){const f=new lk;setTimeout(()=>void f.resolve());
await f.promise}const d=a.logger.share();try{a.state=5;const f=[],g=await Bk(a.vm.snapshot({Ka:{},Ud:f}),a.Nb.Cf,()=>Promise.reject(new x(15,"MDA:Timeout")));
if(a.I)throw new x(a.h?20:32,"MDA:Disposed");const h=f[0];a.state=6;const k=await Bk(ll(a.Oa,g),a.Nb.Ne,()=>Promise.reject(new x(10,"BWB:Timeout")));
if(a.I)throw new x(a.h?20:32,"BWB:Disposed");a.state=7;b=Vj(d,()=>{const l=ml(a,k,c,h);l.j.promise.then(()=>void a.o());
return l},"i")}catch(f){b?.dispose();
if(!a.i){const g=nl(a,f);c.resolve();var e;if(e=a.vm instanceof Lk&&a.j<2)a:if(f instanceof x)e=f.code!==32&&f.code!==20&&f.code!==10;else{if(f instanceof Dj)switch(f.code){case 2:case 13:case 14:case 4:break;default:e=!1;break a}e=!0}if(e){const h=setTimeout(()=>void a.o(),(1+Math.random()*.25)*(a.h?6E4:1E3));
a.addOnDisposeCallback(()=>void clearTimeout(h));
return}a.i=g}d.ta(a.h?13:14);a.Jb.reject(a.i);return}finally{d.dispose()}a.state=8;a.j=0;a.h?.dispose();a.h=b;a.Jb.resolve()}
function nl(a,b){if(!(b instanceof x))if(b instanceof Dj){const c=Error(b.toString());c.stack=b.stack;b=new x(11,"EBH:Error",c)}else b=new x(12,"BSO:Unknown",b);return Vb(a,b)}
function ml(a,b,c,d){const e=(je(Ze(b,2))??0)*1E3;if(e<=0)throw new x(31,"TTM:Invalid");if(sf(b,4))return new el(a.logger,sf(b,4),e);if(!(je(Ze(b,3))??0))return new dl(a.logger,hd(ff(b)),e);if(!d)throw new x(4,"PMD:Undefined");d=d(hd(ff(b)));if(typeof d!=="function")throw new x(16,"APF:Failed");a.u=Math.floor((Date.now()+e)/1E3);a=new cl(a.logger,d,je(Ze(b,3))??0,e);a.addOnDisposeCallback(()=>void c.resolve());
return a}
function ol(a,b,c){try{if(a.I)throw new x(21,"BNT:disposed");if(!a.h&&a.i)throw a.i;return pl(a,b,c)??ql(a,b,c)??rl(a,b,c)}catch(d){if(!b.kf)throw sl(a,d);return tl(a,c,d)}}
function sl(a,b){b=b instanceof x?b:new x(5,"TVD:error",b);return Vb(a,b)}
function pl(a,b,c){return a.h?.Yc(()=>ul(a,b),c,d=>{if(a.h instanceof cl&&b.hc?.Df)try{a.cache?.h(ul(a,b),d,b.hc.od,a.u-120)}catch(e){Vb(a,new x(24,"ELX:write",e))}})}
function ql(a,b,c){if(b.hc?.je)try{const d=a.cache?.i(ul(a,b),b.hc.od);return d?c?Vj(a.logger,()=>Vc(d,2),"a"):d:void 0}catch(d){Vb(a,new x(23,"RXO:read",d))}}
function rl(a,b,c){const d={stack:[],error:void 0,jb:!1};try{if(!b.jf)throw new x(29,"SDF:notready");return Aa(d,new il(a.logger,a.state)).Yc(()=>ul(a,b),c)}catch(e){d.error=e,d.jb=!0}finally{Ba(d)}}
function tl(a,b,c){const d={stack:[],error:void 0,jb:!1};try{const e=sl(a,c);return Aa(d,new hl(a.logger,e)).Yc(()=>[],b)}catch(e){d.error=e,d.jb=!0}finally{Ba(d)}}
function ul(a,b){return b.Pc?b.Pc:b.Ka?Vj(a.logger,()=>b.Pc=gl(b.Ka),"c"):[]}
class vl extends y{constructor(a){super();this.Jb=new lk;this.j=0;this.i=void 0;this.state=2;this.vm=a.vm;this.Oa=a.Oa;this.Nb={...jl,...(a.Nb||{})};this.logger=a.vm.cc();this.onError=a.onError??(()=>{});
this.ld=a.ld||!1;if(wl(a)){const d=this.vm;this.o=()=>d.G().catch(e=>{this.i=e=Vb(this,new x(this.h?20:32,"TRG:Disposed",e));this.h?.dispose();this.h=void 0;this.Jb.reject(e)});
Ik(d,()=>void kl(this));
d.P===2&&kl(this)}else this.o=a.si,kl(this);const b=this.logger.share();b.h("o");const c=new Uj(b,"o");this.Jb.promise.then(()=>{c.done();b.i();b.dispose()},()=>void b.dispose());
this.addOnDisposeCallback(()=>{this.h?(this.h.dispose(),this.h=void 0):this.i?this.logger.i():(this.i=Vb(this,new x(32,"TNP:Disposed")),this.logger.i(),this.Jb.reject(this.i))});
Ob(this,this.logger)}eb(a){return ol(this,{...a},!1)}yc(a){return ol(this,{...a},!0)}}const wl=function(a){return Ed(b=>{if(!Kd(b))return!1;for(const [c,d]of Object.entries(a)){const e=c,f=d;if(!(e in b)){if(f.ki===!0)continue;return!1}if(!f(b[e]))return!1}return!0})}({vm:function(a){return Ed(b=>b instanceof a)}(Lk)},"");var zl=class{constructor(){if(!xl){xl=new Aj(new yl);var a=I("client_streamz_web_flush_count",-1);a!==-1&&(xl.j=a)}this.i=a=xl;ic(a,"/client_streamz/youtube/aba/gac",dc("type"),dc("sequence"))}h(a,b){jc(this.i,"/client_streamz/youtube/aba/gac",[a,b])}};var Al=window;function Bl(a){var b=Cl;if(b)for(const c in b)Object.prototype.hasOwnProperty.call(b,c)&&a(b[c],c,b)}
function Dl(){const a=[];Bl(b=>{a.push(b)});
return a}
;var Cl={Nf:"allow-forms",Of:"allow-modals",Pf:"allow-orientation-lock",Qf:"allow-pointer-lock",Rf:"allow-popups",Sf:"allow-popups-to-escape-sandbox",Tf:"allow-presentation",Uf:"allow-same-origin",Vf:"allow-scripts",Wf:"allow-top-navigation",Xf:"allow-top-navigation-by-user-activation"};const El=dj(()=>Dl());
function Fl(){const a=document.createElement("iframe"),b={};hb(El(),c=>{a.sandbox&&a.sandbox.supports&&a.sandbox.supports(c)&&(b[c]=!0)});
return b}
;function Gl(a){typeof a=="number"&&(a=Math.round(a)+"px");return a}
;let Hl=(new Date).getTime();var Il=vg(class extends G{constructor(a){super(a)}});function Jl(){var a=Kl;Ll.instance||(Ll.instance=new Ll(a));return Ll.instance}
function Ml(a,b){return a.u?a.u:a.u=new Promise(async c=>{const d=window.AbortController?new window.AbortController:void 0,e=d?.signal;let f=!1;try{d&&(a.j=a.Ha.va(()=>{d.abort()},b||2E4)),await fetch("/generate_204",{method:"HEAD",
signal:e}),f=!0}catch{f=!1}finally{a.u=void 0,a.j&&(a.Ha.wa(a.j),a.j=0),f!==a.h&&(a.h=f,a.h?Pi(a,"networkstatus-online"):Pi(a,"networkstatus-offline")),c(f)}})}
function Nl(a){a.A=a.Ha.va(async()=>{a.h?window.navigator?.onLine||await Ml(a):await Ml(a);Nl(a)},3E4)}
var Ll=class extends Oi{constructor(a){super();this.A=this.j=0;this.Ha=a??{va:(b,c)=>setTimeout(b,c),
wa:b=>{clearTimeout(b)}};
this.h=window.navigator?.onLine??!0;this.o=async()=>{await Ml(this)};
window.addEventListener("offline",this.o);window.addEventListener("online",this.o);this.A||Nl(this)}dispose(){window.removeEventListener("offline",this.o);window.removeEventListener("online",this.o);this.Ha.wa(this.A);delete Ll.instance}ya(){return this.h}};function Ol(a){a.h===-1&&(a.h=a.data.reduce((b,c,d)=>b+(c?2**d:0),0));
return a.h}
var Pl=class{constructor(){this.data=[];this.h=-1}set(a,b=!0){0<=a&&a<52&&Number.isInteger(a)&&this.data[a]!==b&&(this.data[a]=b,this.h=-1)}get(a){return!!this.data[a]}};function Ql(){this.blockSize=-1}
;function Rl(a,b,c){c||(c=0);const d=a.H;if(typeof b==="string")for(var e=0;e<16;e++)d[e]=b.charCodeAt(c)<<24|b.charCodeAt(c+1)<<16|b.charCodeAt(c+2)<<8|b.charCodeAt(c+3),c+=4;else for(e=0;e<16;e++)d[e]=b[c]<<24|b[c+1]<<16|b[c+2]<<8|b[c+3],c+=4;for(b=16;b<80;b++)c=d[b-3]^d[b-8]^d[b-14]^d[b-16],d[b]=(c<<1|c>>>31)&4294967295;b=a.h[0];c=a.h[1];e=a.h[2];let f=a.h[3],g=a.h[4];let h;for(let l=0;l<80;l++){if(l<40)if(l<20){var k=f^c&(e^f);h=1518500249}else k=c^e^f,h=1859775393;else l<60?(k=c&e|f&(c|e),h=2400959708):
(k=c^e^f,h=3395469782);k=(b<<5|b>>>27)+k+g+h+d[l]&4294967295;g=f;f=e;e=(c<<30|c>>>2)&4294967295;c=b;b=k}a.h[0]=a.h[0]+b&4294967295;a.h[1]=a.h[1]+c&4294967295;a.h[2]=a.h[2]+e&4294967295;a.h[3]=a.h[3]+f&4294967295;a.h[4]=a.h[4]+g&4294967295}
class Sl extends Ql{constructor(){super();this.blockSize=64;this.h=[];this.u=[];this.H=[];this.j=[];this.j[0]=128;for(let a=1;a<this.blockSize;++a)this.j[a]=0;this.o=this.i=0;this.reset()}reset(){this.h[0]=1732584193;this.h[1]=4023233417;this.h[2]=2562383102;this.h[3]=271733878;this.h[4]=3285377520;this.o=this.i=0}update(a,b){if(a!=null){b===void 0&&(b=a.length);for(var c=b-this.blockSize,d=0,e=this.u,f=this.i;d<b;){if(f==0)for(;d<=c;)Rl(this,a,d),d+=this.blockSize;if(typeof a==="string")for(;d<b;){if(e[f]=
a.charCodeAt(d),++f,++d,f==this.blockSize){Rl(this,e);f=0;break}}else for(;d<b;)if(e[f]=a[d],++f,++d,f==this.blockSize){Rl(this,e);f=0;break}}this.i=f;this.o+=b}}digest(){const a=[];var b=this.o*8;this.i<56?this.update(this.j,56-this.i):this.update(this.j,this.blockSize-(this.i-56));for(var c=this.blockSize-1;c>=56;c--)this.u[c]=b&255,b/=256;Rl(this,this.u);b=0;for(c=0;c<5;c++)for(let d=24;d>=0;d-=8)a[b]=this.h[c]>>d&255,++b;return a}};function Tl(a){return typeof a.className=="string"?a.className:a.getAttribute&&a.getAttribute("class")||""}
function Ul(a,b){typeof a.className=="string"?a.className=b:a.setAttribute&&a.setAttribute("class",b)}
function Vl(a,b){a.classList?b=a.classList.contains(b):(a=a.classList?a.classList:Tl(a).match(/\S+/g)||[],b=gb(a,b)>=0);return b}
function Wl(){var a=document.body;a.classList?a.classList.remove("inverted-hdpi"):Vl(a,"inverted-hdpi")&&Ul(a,Array.prototype.filter.call(a.classList?a.classList:Tl(a).match(/\S+/g)||[],function(b){return b!="inverted-hdpi"}).join(" "))}
;function Xl(){}
Xl.prototype.next=function(){return Yl};
const Yl={done:!0,value:void 0};Xl.prototype.sb=function(){return this};function Zl(a){if(a instanceof $l||a instanceof am||a instanceof bm)return a;if(typeof a.next=="function")return new $l(()=>a);
if(typeof a[Symbol.iterator]=="function")return new $l(()=>a[Symbol.iterator]());
if(typeof a.sb=="function")return new $l(()=>a.sb());
throw Error("Not an iterator or iterable.");}
class $l{constructor(a){this.h=a}sb(){return new am(this.h())}[Symbol.iterator](){return new bm(this.h())}i(){return new bm(this.h())}}class am extends Xl{constructor(a){super();this.h=a}next(){return this.h.next()}[Symbol.iterator](){return new bm(this.h)}i(){return new bm(this.h)}}class bm extends $l{constructor(a){super(()=>a);
this.j=a}next(){return this.j.next()}};function cm(a){return a=="\r"||a=="\n"||a==" "||a=="\t"}
;function dm(){this.A=null;this.ob=[];this.H="";this.F=[];this.i=this.h=0;this.j=!1;this.u=0;this.G=/[\\"]/g;this.B=this.o=0}
dm.prototype.done=function(){return this.o===2};
function J(a,b,c){a.o=3;a.A="The stream is broken @"+a.i+"/"+c+". With input:\n"+b;throw Error(a.A);}
dm.prototype.parse=function(a){function b(){for(;m<a.length;)if(cm(a[m]))m++,f.i++;else break;return m<k}
function c(){for(var p;;){p=a[m++];if(!p)break;f.i++;switch(f.B){case 0:p==="{"?f.B=2:p==="["?f.B=4:cm(p)||J(f,a,m);continue;case 7:case 2:if(cm(p))continue;if(f.B===7)g.push(8);else if(p==="}"){e("{}");f.B=d();continue}else g.push(3);p==='"'?f.B=6:J(f,a,m);continue;case 8:case 3:if(cm(p))continue;p===":"?(f.B===3&&(g.push(3),f.h++),f.B=1):p==="}"?(f.h--,e(),f.B=d()):p===","?(f.B===3&&g.push(3),f.B=7):J(f,a,m);continue;case 4:case 1:if(cm(p))continue;if(f.B===4)if(f.h++,f.B=1,p==="]"){f.h--;if(f.h===
0){f.B=5;return}e("[]");f.B=d();continue}else g.push(5);p==='"'?f.B=6:p==="{"?f.B=2:p==="["?f.B=4:p==="t"?f.B=9:p==="f"?f.B=12:p==="n"?f.B=16:p!=="-"&&("0123456789".indexOf(p)!==-1?f.B=20:J(f,a,m));continue;case 5:if(p===",")g.push(5),f.B=1,f.h===1&&(n=m);else if(p==="]"){f.h--;if(f.h===0)return;e();f.B=d()}else if(cm(p))continue;else J(f,a,m);continue;case 6:const z=m;a:for(;;){for(;f.u>0;)if(p=a[m++],f.u===4?f.u=0:f.u++,!p)break a;if(p==='"'&&!f.j){f.B=d();break}if(p==="\\"&&!f.j&&(f.j=!0,p=a[m++],
!p))break;if(f.j)if(f.j=!1,p==="u"&&(f.u=1),p=a[m++])continue;else break;h.lastIndex=m;p=h.exec(a);if(!p){m=a.length+1;break}m=p.index+1;p=a[p.index];if(!p)break}f.i+=m-z;continue;case 9:if(!p)continue;p==="r"?f.B=10:J(f,a,m);continue;case 10:if(!p)continue;p==="u"?f.B=11:J(f,a,m);continue;case 11:if(!p)continue;p==="e"?f.B=d():J(f,a,m);continue;case 12:if(!p)continue;p==="a"?f.B=13:J(f,a,m);continue;case 13:if(!p)continue;p==="l"?f.B=14:J(f,a,m);continue;case 14:if(!p)continue;p==="s"?f.B=15:J(f,
a,m);continue;case 15:if(!p)continue;p==="e"?f.B=d():J(f,a,m);continue;case 16:if(!p)continue;p==="u"?f.B=17:J(f,a,m);continue;case 17:if(!p)continue;p==="l"?f.B=18:J(f,a,m);continue;case 18:if(!p)continue;p==="l"?f.B=d():J(f,a,m);continue;case 19:p==="."?f.B=20:J(f,a,m);continue;case 20:if("0123456789.eE+-".indexOf(p)!==-1)continue;else m--,f.i--,f.B=d();continue;default:J(f,a,m)}}}
function d(){const p=g.pop();return p!=null?p:1}
function e(p){f.h>1||(p||(p=n===-1?f.H+a.substring(l,m):a.substring(n,m)),f.ob.push(JSON.parse(p)),n=m)}
const f=this,g=f.F,h=f.G,k=a.length;let l=0,n=-1,m=0;for(;m<k;)switch(f.o){case 3:return J(f,a,m),null;case 2:return b()&&J(f,a,m),null;case 0:if(b()){var u=a[m++];f.i++;if(u==="["){f.o=1;l=m;f.B=4;continue}else J(f,a,m)}return null;case 1:return c(),f.h===0&&f.B==5?(f.o=2,f.H=a.substring(m)):f.H=n===-1?f.H+a.substring(l):a.substring(n),f.ob.length>0?(u=f.ob,f.ob=[],u):null}return null};function L(a){y.call(this);this.u=1;this.j=[];this.o=0;this.h=[];this.i={};this.A=!!a}
va(L,y);r=L.prototype;r.subscribe=function(a,b,c){let d=this.i[a];d||(d=this.i[a]=[]);const e=this.u;this.h[e]=a;this.h[e+1]=b;this.h[e+2]=c;this.u=e+3;d.push(e);return e};
r.unsubscribe=function(a,b,c){if(a=this.i[a]){const d=this.h;if(a=a.find(function(e){return d[e+1]==b&&d[e+2]==c}))return this.ec(a)}return!1};
r.ec=function(a){const b=this.h[a];if(b){const c=this.i[b];this.o!=0?(this.j.push(a),this.h[a+1]=()=>{}):(c&&mb(c,a),delete this.h[a],delete this.h[a+1],delete this.h[a+2])}return!!b};
r.rb=function(a,b){var c=this.i[a];if(c){const e=Array(arguments.length-1);var d=arguments.length;let f;for(f=1;f<d;f++)e[f-1]=arguments[f];if(this.A)for(f=0;f<c.length;f++)d=c[f],em(this.h[d+1],this.h[d+2],e);else{this.o++;try{for(f=0,d=c.length;f<d&&!this.I;f++){const g=c[f];this.h[g+1].apply(this.h[g+2],e)}}finally{if(this.o--,this.j.length>0&&this.o==0)for(;c=this.j.pop();)this.ec(c)}}return f!=0}return!1};
function em(a,b,c){aj(function(){a.apply(b,c)})}
r.clear=function(a){if(a){const b=this.i[a];b&&(b.forEach(this.ec,this),delete this.i[a])}else this.h.length=0,this.i={}};
r.ba=function(){L.Ea.ba.call(this);this.clear();this.j.length=0};function fm(a){this.h=a}
fm.prototype.set=function(a,b){b===void 0?this.h.remove(a):this.h.set(a,(new Ej).serialize(b))};
fm.prototype.get=function(a){let b;try{b=this.h.get(a)}catch(c){return}if(b!==null)try{return JSON.parse(b)}catch(c){throw"Storage: Invalid value was encountered";}};
fm.prototype.remove=function(a){this.h.remove(a)};function gm(a){this.h=a}
va(gm,fm);function hm(a){this.data=a}
function im(a){return a===void 0||a instanceof hm?a:new hm(a)}
gm.prototype.set=function(a,b){gm.Ea.set.call(this,a,im(b))};
gm.prototype.i=function(a){a=gm.Ea.get.call(this,a);if(a===void 0||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
gm.prototype.get=function(a){if(a=this.i(a)){if(a=a.data,a===void 0)throw"Storage: Invalid value was encountered";}else a=void 0;return a};function jm(a){this.h=a}
va(jm,gm);jm.prototype.set=function(a,b,c){if(b=im(b)){if(c){if(c<ta()){jm.prototype.remove.call(this,a);return}b.expiration=c}b.creation=ta()}jm.Ea.set.call(this,a,b)};
jm.prototype.i=function(a){const b=jm.Ea.i.call(this,a);if(b){const c=b.creation,d=b.expiration;if(d&&d<ta()||c&&c>ta())jm.prototype.remove.call(this,a);else return b}};function km(){}
;function lm(){}
va(lm,km);lm.prototype[Symbol.iterator]=function(){return Zl(this.sb(!0)).i()};
lm.prototype.clear=function(){const a=Array.from(this);for(const b of a)this.remove(b)};function mm(a){this.h=a;this.i=null}
va(mm,lm);r=mm.prototype;r.isAvailable=function(){if(this.i===null){var a=this.h;if(a)try{a.setItem("__sak","1");a.removeItem("__sak");var b=!0}catch(c){b=c instanceof DOMException&&(c.name==="QuotaExceededError"||c.code===22||c.code===1014||c.name==="NS_ERROR_DOM_QUOTA_REACHED")&&a&&a.length!==0}else b=!1;this.i=b}return this.i};
r.set=function(a,b){nm(this);try{this.h.setItem(a,b)}catch(c){if(this.h.length==0)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
r.get=function(a){nm(this);a=this.h.getItem(a);if(typeof a!=="string"&&a!==null)throw"Storage mechanism: Invalid value was encountered";return a};
r.remove=function(a){nm(this);this.h.removeItem(a)};
r.sb=function(a){nm(this);var b=0,c=this.h,d=new Xl;d.next=function(){if(b>=c.length)return Yl;var e=c.key(b++);if(a)return{value:e,done:!1};e=c.getItem(e);if(typeof e!=="string")throw"Storage mechanism: Invalid value was encountered";return{value:e,done:!1}};
return d};
r.clear=function(){nm(this);this.h.clear()};
r.key=function(a){nm(this);return this.h.key(a)};
function nm(a){if(a.h==null)throw Error("Storage mechanism: Storage unavailable");a.isAvailable()||uc(Error("Storage mechanism: Storage unavailable"))}
;function om(){let a=null;try{a=t.localStorage||null}catch(b){}mm.call(this,a)}
va(om,mm);function pm(a,b){this.i=a;this.h=b+"::"}
va(pm,lm);pm.prototype.set=function(a,b){this.i.set(this.h+a,b)};
pm.prototype.get=function(a){return this.i.get(this.h+a)};
pm.prototype.remove=function(a){this.i.remove(this.h+a)};
pm.prototype.sb=function(a){const b=this.i[Symbol.iterator](),c=this,d=new Xl;d.next=function(){var e=b.next();if(e.done)return e;for(e=e.value;e.slice(0,c.h.length)!=c.h;){e=b.next();if(e.done)return e;e=e.value}return{value:a?e.slice(c.h.length):c.i.get(e),done:!1}};
return d};function qm(a){if(a.ab&&typeof a.ab=="function")return a.ab();if(typeof Map!=="undefined"&&a instanceof Map||typeof Set!=="undefined"&&a instanceof Set)return Array.from(a.values());if(typeof a==="string")return a.split("");if(la(a)){const b=[],c=a.length;for(let d=0;d<c;d++)b.push(a[d]);return b}return eh(a)}
function rm(a){if(a.Vb&&typeof a.Vb=="function")return a.Vb();if(!a.ab||typeof a.ab!="function"){if(typeof Map!=="undefined"&&a instanceof Map)return Array.from(a.keys());if(!(typeof Set!=="undefined"&&a instanceof Set)){if(la(a)||typeof a==="string"){var b=[];a=a.length;for(var c=0;c<a;c++)b.push(c);return b}b=[];c=0;for(const d in a)b[c++]=d;return b}}}
function sm(a,b,c){if(a.forEach&&typeof a.forEach=="function")a.forEach(b,c);else if(la(a)||typeof a==="string")Array.prototype.forEach.call(a,b,c);else{const d=rm(a),e=qm(a),f=e.length;for(let g=0;g<f;g++)b.call(c,e[g],d&&d[g],a)}}
;function tm(a){this.i=this.A=this.j="";this.F=null;this.u=this.h="";this.o=!1;let b;a instanceof tm?(this.o=a.o,um(this,a.j),this.A=a.A,this.i=a.i,wm(this,a.F),this.h=a.h,xm(this,a.H.clone()),this.u=a.u):a&&(b=String(a).match(xb))?(this.o=!1,um(this,b[1]||"",!0),this.A=ym(b[2]||""),this.i=ym(b[3]||"",!0),wm(this,b[4]),this.h=ym(b[5]||"",!0),xm(this,b[6]||"",!0),this.u=ym(b[7]||"")):(this.o=!1,this.H=new zm(null,this.o))}
tm.prototype.toString=function(){const a=[];var b=this.j;b&&a.push(Am(b,Bm,!0),":");var c=this.i;if(c||b=="file")a.push("//"),(b=this.A)&&a.push(Am(b,Bm,!0),"@"),a.push(encodeURIComponent(String(c)).replace(/%25([0-9a-fA-F]{2})/g,"%$1")),c=this.F,c!=null&&a.push(":",String(c));if(c=this.h)this.i&&c.charAt(0)!="/"&&a.push("/"),a.push(Am(c,c.charAt(0)=="/"?Cm:Dm,!0));(c=this.H.toString())&&a.push("?",c);(c=this.u)&&a.push("#",Am(c,Em));return a.join("")};
tm.prototype.resolve=function(a){const b=this.clone();let c=!!a.j;c?um(b,a.j):c=!!a.A;c?b.A=a.A:c=!!a.i;c?b.i=a.i:c=a.F!=null;var d=a.h;if(c)wm(b,a.F);else if(c=!!a.h){if(d.charAt(0)!="/")if(this.i&&!this.h)d="/"+d;else{var e=b.h.lastIndexOf("/");e!=-1&&(d=b.h.slice(0,e+1)+d)}e=d;if(e==".."||e==".")d="";else if(e.indexOf("./")!=-1||e.indexOf("/.")!=-1){d=e.lastIndexOf("/",0)==0;e=e.split("/");const f=[];for(let g=0;g<e.length;){const h=e[g++];h=="."?d&&g==e.length&&f.push(""):h==".."?((f.length>1||
f.length==1&&f[0]!="")&&f.pop(),d&&g==e.length&&f.push("")):(f.push(h),d=!0)}d=f.join("/")}else d=e}c?b.h=d:c=a.H.toString()!=="";c?xm(b,a.H.clone()):c=!!a.u;c&&(b.u=a.u);return b};
tm.prototype.clone=function(){return new tm(this)};
function um(a,b,c){a.j=c?ym(b,!0):b;a.j&&(a.j=a.j.replace(/:$/,""))}
function wm(a,b){if(b){b=Number(b);if(isNaN(b)||b<0)throw Error("Bad port number "+b);a.F=b}else a.F=null}
function xm(a,b,c){b instanceof zm?(a.H=b,Fm(a.H,a.o)):(c||(b=Am(b,Gm)),a.H=new zm(b,a.o))}
function ym(a,b){return a?b?decodeURI(a.replace(/%25/g,"%2525")):decodeURIComponent(a):""}
function Am(a,b,c){return typeof a==="string"?(a=encodeURI(a).replace(b,Hm),c&&(a=a.replace(/%25([0-9a-fA-F]{2})/g,"%$1")),a):null}
function Hm(a){a=a.charCodeAt(0);return"%"+(a>>4&15).toString(16)+(a&15).toString(16)}
var Bm=/[#\/\?@]/g,Dm=/[#\?:]/g,Cm=/[#\?]/g,Gm=/[#\?@]/g,Em=/#/g;function zm(a,b){this.i=this.h=null;this.j=a||null;this.o=!!b}
function Im(a){a.h||(a.h=new Map,a.i=0,a.j&&Db(a.j,function(b,c){a.add(vb(b),c)}))}
r=zm.prototype;r.add=function(a,b){Im(this);this.j=null;a=Jm(this,a);let c=this.h.get(a);c||this.h.set(a,c=[]);c.push(b);this.i=this.i+1;return this};
r.remove=function(a){Im(this);a=Jm(this,a);return this.h.has(a)?(this.j=null,this.i=this.i-this.h.get(a).length,this.h.delete(a)):!1};
r.clear=function(){this.h=this.j=null;this.i=0};
function Km(a,b){Im(a);b=Jm(a,b);return a.h.has(b)}
r.forEach=function(a,b){Im(this);this.h.forEach(function(c,d){c.forEach(function(e){a.call(b,e,d,this)},this)},this)};
r.Vb=function(){Im(this);const a=Array.from(this.h.values()),b=Array.from(this.h.keys()),c=[];for(let d=0;d<b.length;d++){const e=a[d];for(let f=0;f<e.length;f++)c.push(b[d])}return c};
r.ab=function(a){Im(this);let b=[];if(typeof a==="string")Km(this,a)&&(b=b.concat(this.h.get(Jm(this,a))));else{a=Array.from(this.h.values());for(let c=0;c<a.length;c++)b=b.concat(a[c])}return b};
r.set=function(a,b){Im(this);this.j=null;a=Jm(this,a);Km(this,a)&&(this.i=this.i-this.h.get(a).length);this.h.set(a,[b]);this.i=this.i+1;return this};
r.get=function(a,b){if(!a)return b;a=this.ab(a);return a.length>0?String(a[0]):b};
r.toString=function(){if(this.j)return this.j;if(!this.h)return"";const a=[],b=Array.from(this.h.keys());for(let d=0;d<b.length;d++){var c=b[d];const e=encodeURIComponent(String(c));c=this.ab(c);for(let f=0;f<c.length;f++){let g=e;c[f]!==""&&(g+="="+encodeURIComponent(String(c[f])));a.push(g)}}return this.j=a.join("&")};
r.clone=function(){const a=new zm;a.j=this.j;this.h&&(a.h=new Map(this.h),a.i=this.i);return a};
function Jm(a,b){b=String(b);a.o&&(b=b.toLowerCase());return b}
function Fm(a,b){b&&!a.o&&(Im(a),a.j=null,a.h.forEach(function(c,d){const e=d.toLowerCase();d!=e&&(this.remove(d),this.remove(e),c.length>0&&(this.j=null,this.h.set(Jm(this,e),nb(c)),this.i=this.i+c.length))},a));
a.o=b}
r.extend=function(a){for(let b=0;b<arguments.length;b++)sm(arguments[b],function(c,d){this.add(d,c)},this)};/*

 (The MIT License)

 Copyright (C) 2014 by Vitaly Puzrin

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.

 -----------------------------------------------------------------------------
 Ported from zlib, which is under the following license
 https://github.com/madler/zlib/blob/master/zlib.h

 zlib.h -- interface of the 'zlib' general purpose compression library
   version 1.2.8, April 28th, 2013
   Copyright (C) 1995-2013 Jean-loup Gailly and Mark Adler
   This software is provided 'as-is', without any express or implied
   warranty.  In no event will the authors be held liable for any damages
   arising from the use of this software.
   Permission is granted to anyone to use this software for any purpose,
   including commercial applications, and to alter it and redistribute it
   freely, subject to the following restrictions:
   1. The origin of this software must not be misrepresented; you must not
      claim that you wrote the original software. If you use this software
      in a product, an acknowledgment in the product documentation would be
      appreciated but is not required.
   2. Altered source versions must be plainly marked as such, and must not be
      misrepresented as being the original software.
   3. This notice may not be removed or altered from any source distribution.
   Jean-loup Gailly        Mark Adler
   jloup@gzip.org          madler@alumni.caltech.edu
   The data format used by the zlib library is described by RFCs (Request for
   Comments) 1950 to 1952 in the files http://tools.ietf.org/html/rfc1950
   (zlib format), rfc1951 (deflate format) and rfc1952 (gzip format).
*/
let N={};var Lm=typeof Uint8Array!=="undefined"&&typeof Uint16Array!=="undefined"&&typeof Int32Array!=="undefined";N.assign=function(a){for(var b=Array.prototype.slice.call(arguments,1);b.length;){var c=b.shift();if(c){if(typeof c!=="object")throw new TypeError(c+"must be non-object");for(var d in c)Object.prototype.hasOwnProperty.call(c,d)&&(a[d]=c[d])}}return a};
N.ed=function(a,b){if(a.length===b)return a;if(a.subarray)return a.subarray(0,b);a.length=b;return a};
var Mm={tb:function(a,b,c,d,e){if(b.subarray&&a.subarray)a.set(b.subarray(c,c+d),e);else for(var f=0;f<d;f++)a[e+f]=b[c+f]},
rd:function(a){var b,c;var d=c=0;for(b=a.length;d<b;d++)c+=a[d].length;var e=new Uint8Array(c);d=c=0;for(b=a.length;d<b;d++){var f=a[d];e.set(f,c);c+=f.length}return e}},Nm={tb:function(a,b,c,d,e){for(var f=0;f<d;f++)a[e+f]=b[c+f]},
rd:function(a){return[].concat.apply([],a)}};
N.yf=function(){Lm?(N.qb=Uint8Array,N.Ma=Uint16Array,N.Yd=Int32Array,N.assign(N,Mm)):(N.qb=Array,N.Ma=Array,N.Yd=Array,N.assign(N,Nm))};
N.yf();var Om=!0;try{new Uint8Array(1)}catch(a){Om=!1}
function Pm(a){var b,c,d=a.length,e=0;for(b=0;b<d;b++){var f=a.charCodeAt(b);if((f&64512)===55296&&b+1<d){var g=a.charCodeAt(b+1);(g&64512)===56320&&(f=65536+(f-55296<<10)+(g-56320),b++)}e+=f<128?1:f<2048?2:f<65536?3:4}var h=new N.qb(e);for(b=c=0;c<e;b++)f=a.charCodeAt(b),(f&64512)===55296&&b+1<d&&(g=a.charCodeAt(b+1),(g&64512)===56320&&(f=65536+(f-55296<<10)+(g-56320),b++)),f<128?h[c++]=f:(f<2048?h[c++]=192|f>>>6:(f<65536?h[c++]=224|f>>>12:(h[c++]=240|f>>>18,h[c++]=128|f>>>12&63),h[c++]=128|f>>>
6&63),h[c++]=128|f&63);return h}
;let Qm={};Qm=function(a,b,c,d){var e=a&65535|0;a=a>>>16&65535|0;for(var f;c!==0;){f=c>2E3?2E3:c;c-=f;do e=e+b[d++]|0,a=a+e|0;while(--f);e%=65521;a%=65521}return e|a<<16|0};let Rm={};for(var Sm,Tm=[],Um=0;Um<256;Um++){Sm=Um;for(var Vm=0;Vm<8;Vm++)Sm=Sm&1?3988292384^Sm>>>1:Sm>>>1;Tm[Um]=Sm}Rm=function(a,b,c,d){c=d+c;for(a^=-1;d<c;d++)a=a>>>8^Tm[(a^b[d])&255];return a^-1};let Wm={};Wm={2:"need dictionary",1:"stream end",0:"","-1":"file error","-2":"stream error","-3":"data error","-4":"insufficient memory","-5":"buffer error","-6":"incompatible version"};function Xm(a){for(var b=a.length;--b>=0;)a[b]=0}
var Ym=[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0],Zm=[0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13],$m=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,7],an=[16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15],bn=Array(576);Xm(bn);var cn=Array(60);Xm(cn);var dn=Array(512);Xm(dn);var en=Array(256);Xm(en);var fn=Array(29);Xm(fn);var gn=Array(30);Xm(gn);function hn(a,b,c,d,e){this.Ld=a;this.Le=b;this.Ke=c;this.ze=d;this.ff=e;this.ud=a&&a.length}
var jn,kn,ln;function mn(a,b){this.qd=a;this.Fb=0;this.fb=b}
function nn(a,b){a.ea[a.pending++]=b&255;a.ea[a.pending++]=b>>>8&255}
function on(a,b,c){a.ja>16-c?(a.sa|=b<<a.ja&65535,nn(a,a.sa),a.sa=b>>16-a.ja,a.ja+=c-16):(a.sa|=b<<a.ja&65535,a.ja+=c)}
function pn(a,b,c){on(a,c[b*2],c[b*2+1])}
function qn(a,b){var c=0;do c|=a&1,a>>>=1,c<<=1;while(--b>0);return c>>>1}
function rn(a,b,c){var d=Array(16),e=0,f;for(f=1;f<=15;f++)d[f]=e=e+c[f-1]<<1;for(c=0;c<=b;c++)e=a[c*2+1],e!==0&&(a[c*2]=qn(d[e]++,e))}
function sn(a){var b;for(b=0;b<286;b++)a.xa[b*2]=0;for(b=0;b<30;b++)a.ib[b*2]=0;for(b=0;b<19;b++)a.ma[b*2]=0;a.xa[512]=1;a.Ta=a.Lb=0;a.Ca=a.matches=0}
function tn(a){a.ja>8?nn(a,a.sa):a.ja>0&&(a.ea[a.pending++]=a.sa);a.sa=0;a.ja=0}
function un(a,b,c){tn(a);nn(a,c);nn(a,~c);N.tb(a.ea,a.window,b,c,a.pending);a.pending+=c}
function vn(a,b,c,d){var e=b*2,f=c*2;return a[e]<a[f]||a[e]===a[f]&&d[b]<=d[c]}
function wn(a,b,c){for(var d=a.fa[c],e=c<<1;e<=a.Ra;){e<a.Ra&&vn(b,a.fa[e+1],a.fa[e],a.depth)&&e++;if(vn(b,d,a.fa[e],a.depth))break;a.fa[c]=a.fa[e];c=e;e<<=1}a.fa[c]=d}
function xn(a,b,c){var d=0;if(a.Ca!==0){do{var e=a.ea[a.Sb+d*2]<<8|a.ea[a.Sb+d*2+1];var f=a.ea[a.Uc+d];d++;if(e===0)pn(a,f,b);else{var g=en[f];pn(a,g+256+1,b);var h=Ym[g];h!==0&&(f-=fn[g],on(a,f,h));e--;g=e<256?dn[e]:dn[256+(e>>>7)];pn(a,g,c);h=Zm[g];h!==0&&(e-=gn[g],on(a,e,h))}}while(d<a.Ca)}pn(a,256,b)}
function yn(a,b){var c=b.qd,d=b.fb.Ld,e=b.fb.ud,f=b.fb.ze,g,h=-1;a.Ra=0;a.Bb=573;for(g=0;g<f;g++)c[g*2]!==0?(a.fa[++a.Ra]=h=g,a.depth[g]=0):c[g*2+1]=0;for(;a.Ra<2;){var k=a.fa[++a.Ra]=h<2?++h:0;c[k*2]=1;a.depth[k]=0;a.Ta--;e&&(a.Lb-=d[k*2+1])}b.Fb=h;for(g=a.Ra>>1;g>=1;g--)wn(a,c,g);k=f;do g=a.fa[1],a.fa[1]=a.fa[a.Ra--],wn(a,c,1),d=a.fa[1],a.fa[--a.Bb]=g,a.fa[--a.Bb]=d,c[k*2]=c[g*2]+c[d*2],a.depth[k]=(a.depth[g]>=a.depth[d]?a.depth[g]:a.depth[d])+1,c[g*2+1]=c[d*2+1]=k,a.fa[1]=k++,wn(a,c,1);while(a.Ra>=
2);a.fa[--a.Bb]=a.fa[1];g=b.qd;k=b.Fb;d=b.fb.Ld;e=b.fb.ud;f=b.fb.Le;var l=b.fb.Ke,n=b.fb.ff,m,u=0;for(m=0;m<=15;m++)a.Na[m]=0;g[a.fa[a.Bb]*2+1]=0;for(b=a.Bb+1;b<573;b++){var p=a.fa[b];m=g[g[p*2+1]*2+1]+1;m>n&&(m=n,u++);g[p*2+1]=m;if(!(p>k)){a.Na[m]++;var z=0;p>=l&&(z=f[p-l]);var D=g[p*2];a.Ta+=D*(m+z);e&&(a.Lb+=D*(d[p*2+1]+z))}}if(u!==0){do{for(m=n-1;a.Na[m]===0;)m--;a.Na[m]--;a.Na[m+1]+=2;a.Na[n]--;u-=2}while(u>0);for(m=n;m!==0;m--)for(p=a.Na[m];p!==0;)d=a.fa[--b],d>k||(g[d*2+1]!==m&&(a.Ta+=(m-g[d*
2+1])*g[d*2],g[d*2+1]=m),p--)}rn(c,h,a.Na)}
function zn(a,b,c){var d,e=-1,f=b[1],g=0,h=7,k=4;f===0&&(h=138,k=3);b[(c+1)*2+1]=65535;for(d=0;d<=c;d++){var l=f;f=b[(d+1)*2+1];++g<h&&l===f||(g<k?a.ma[l*2]+=g:l!==0?(l!==e&&a.ma[l*2]++,a.ma[32]++):g<=10?a.ma[34]++:a.ma[36]++,g=0,e=l,f===0?(h=138,k=3):l===f?(h=6,k=3):(h=7,k=4))}}
function An(a,b,c){var d,e=-1,f=b[1],g=0,h=7,k=4;f===0&&(h=138,k=3);for(d=0;d<=c;d++){var l=f;f=b[(d+1)*2+1];if(!(++g<h&&l===f)){if(g<k){do pn(a,l,a.ma);while(--g!==0)}else l!==0?(l!==e&&(pn(a,l,a.ma),g--),pn(a,16,a.ma),on(a,g-3,2)):g<=10?(pn(a,17,a.ma),on(a,g-3,3)):(pn(a,18,a.ma),on(a,g-11,7));g=0;e=l;f===0?(h=138,k=3):l===f?(h=6,k=3):(h=7,k=4)}}}
function Bn(a){var b=4093624447,c;for(c=0;c<=31;c++,b>>>=1)if(b&1&&a.xa[c*2]!==0)return 0;if(a.xa[18]!==0||a.xa[20]!==0||a.xa[26]!==0)return 1;for(c=32;c<256;c++)if(a.xa[c*2]!==0)return 1;return 0}
var Cn=!1;function Dn(a,b,c){a.ea[a.Sb+a.Ca*2]=b>>>8&255;a.ea[a.Sb+a.Ca*2+1]=b&255;a.ea[a.Uc+a.Ca]=c&255;a.Ca++;b===0?a.xa[c*2]++:(a.matches++,b--,a.xa[(en[c]+256+1)*2]++,a.ib[(b<256?dn[b]:dn[256+(b>>>7)])*2]++);return a.Ca===a.Wb-1}
;function En(a,b){a.msg=Wm[b];return b}
function Fn(a){for(var b=a.length;--b>=0;)a[b]=0}
function Gn(a){var b=a.state,c=b.pending;c>a.V&&(c=a.V);c!==0&&(N.tb(a.output,b.ea,b.Yb,c,a.Hb),a.Hb+=c,b.Yb+=c,a.hd+=c,a.V-=c,b.pending-=c,b.pending===0&&(b.Yb=0))}
function Hn(a,b){var c=a.za>=0?a.za:-1,d=a.v-a.za,e=0;if(a.level>0){a.S.Nc===2&&(a.S.Nc=Bn(a));yn(a,a.vc);yn(a,a.nc);zn(a,a.xa,a.vc.Fb);zn(a,a.ib,a.nc.Fb);yn(a,a.nd);for(e=18;e>=3&&a.ma[an[e]*2+1]===0;e--);a.Ta+=3*(e+1)+5+5+4;var f=a.Ta+3+7>>>3;var g=a.Lb+3+7>>>3;g<=f&&(f=g)}else f=g=d+5;if(d+4<=f&&c!==-1)on(a,b?1:0,3),un(a,c,d);else if(a.strategy===4||g===f)on(a,2+(b?1:0),3),xn(a,bn,cn);else{on(a,4+(b?1:0),3);c=a.vc.Fb+1;d=a.nc.Fb+1;e+=1;on(a,c-257,5);on(a,d-1,5);on(a,e-4,4);for(f=0;f<e;f++)on(a,
a.ma[an[f]*2+1],3);An(a,a.xa,c-1);An(a,a.ib,d-1);xn(a,a.xa,a.ib)}sn(a);b&&tn(a);a.za=a.v;Gn(a.S)}
function O(a,b){a.ea[a.pending++]=b}
function In(a,b){a.ea[a.pending++]=b>>>8&255;a.ea[a.pending++]=b&255}
function Jn(a,b){var c=a.xd,d=a.v,e=a.Aa,f=a.zd,g=a.v>a.pa-262?a.v-(a.pa-262):0,h=a.window,k=a.gb,l=a.La,n=a.v+258,m=h[d+e-1],u=h[d+e];a.Aa>=a.td&&(c>>=2);f>a.D&&(f=a.D);do{var p=b;if(h[p+e]===u&&h[p+e-1]===m&&h[p]===h[d]&&h[++p]===h[d+1]){d+=2;for(p++;h[++d]===h[++p]&&h[++d]===h[++p]&&h[++d]===h[++p]&&h[++d]===h[++p]&&h[++d]===h[++p]&&h[++d]===h[++p]&&h[++d]===h[++p]&&h[++d]===h[++p]&&d<n;);p=258-(n-d);d=n-258;if(p>e){a.Eb=b;e=p;if(p>=f)break;m=h[d+e-1];u=h[d+e]}}}while((b=l[b&k])>g&&--c!==0);return e<=
a.D?e:a.D}
function Kn(a){var b=a.pa,c;do{var d=a.Wd-a.D-a.v;if(a.v>=b+(b-262)){N.tb(a.window,a.window,b,b,0);a.Eb-=b;a.v-=b;a.za-=b;var e=c=a.uc;do{var f=a.head[--e];a.head[e]=f>=b?f-b:0}while(--c);e=c=b;do f=a.La[--e],a.La[e]=f>=b?f-b:0;while(--c);d+=b}if(a.S.ra===0)break;e=a.S;c=a.window;f=a.v+a.D;var g=e.ra;g>d&&(g=d);g===0?c=0:(e.ra-=g,N.tb(c,e.input,e.mb,g,f),e.state.wrap===1?e.K=Qm(e.K,c,g,f):e.state.wrap===2&&(e.K=Rm(e.K,c,g,f)),e.mb+=g,e.pb+=g,c=g);a.D+=c;if(a.D+a.oa>=3)for(d=a.v-a.oa,a.U=a.window[d],
a.U=(a.U<<a.Qa^a.window[d+1])&a.Pa;a.oa&&!(a.U=(a.U<<a.Qa^a.window[d+3-1])&a.Pa,a.La[d&a.gb]=a.head[a.U],a.head[a.U]=d,d++,a.oa--,a.D+a.oa<3););}while(a.D<262&&a.S.ra!==0)}
function Ln(a,b){for(var c;;){if(a.D<262){Kn(a);if(a.D<262&&b===0)return 1;if(a.D===0)break}c=0;a.D>=3&&(a.U=(a.U<<a.Qa^a.window[a.v+3-1])&a.Pa,c=a.La[a.v&a.gb]=a.head[a.U],a.head[a.U]=a.v);c!==0&&a.v-c<=a.pa-262&&(a.W=Jn(a,c));if(a.W>=3)if(c=Dn(a,a.v-a.Eb,a.W-3),a.D-=a.W,a.W<=a.Wc&&a.D>=3){a.W--;do a.v++,a.U=(a.U<<a.Qa^a.window[a.v+3-1])&a.Pa,a.La[a.v&a.gb]=a.head[a.U],a.head[a.U]=a.v;while(--a.W!==0);a.v++}else a.v+=a.W,a.W=0,a.U=a.window[a.v],a.U=(a.U<<a.Qa^a.window[a.v+1])&a.Pa;else c=Dn(a,0,
a.window[a.v]),a.D--,a.v++;if(c&&(Hn(a,!1),a.S.V===0))return 1}a.oa=a.v<2?a.v:2;return b===4?(Hn(a,!0),a.S.V===0?3:4):a.Ca&&(Hn(a,!1),a.S.V===0)?1:2}
function Mn(a,b){for(var c,d;;){if(a.D<262){Kn(a);if(a.D<262&&b===0)return 1;if(a.D===0)break}c=0;a.D>=3&&(a.U=(a.U<<a.Qa^a.window[a.v+3-1])&a.Pa,c=a.La[a.v&a.gb]=a.head[a.U],a.head[a.U]=a.v);a.Aa=a.W;a.Cd=a.Eb;a.W=2;c!==0&&a.Aa<a.Wc&&a.v-c<=a.pa-262&&(a.W=Jn(a,c),a.W<=5&&(a.strategy===1||a.W===3&&a.v-a.Eb>4096)&&(a.W=2));if(a.Aa>=3&&a.W<=a.Aa){d=a.v+a.D-3;c=Dn(a,a.v-1-a.Cd,a.Aa-3);a.D-=a.Aa-1;a.Aa-=2;do++a.v<=d&&(a.U=(a.U<<a.Qa^a.window[a.v+3-1])&a.Pa,a.La[a.v&a.gb]=a.head[a.U],a.head[a.U]=a.v);
while(--a.Aa!==0);a.kb=0;a.W=2;a.v++;if(c&&(Hn(a,!1),a.S.V===0))return 1}else if(a.kb){if((c=Dn(a,0,a.window[a.v-1]))&&Hn(a,!1),a.v++,a.D--,a.S.V===0)return 1}else a.kb=1,a.v++,a.D--}a.kb&&(Dn(a,0,a.window[a.v-1]),a.kb=0);a.oa=a.v<2?a.v:2;return b===4?(Hn(a,!0),a.S.V===0?3:4):a.Ca&&(Hn(a,!1),a.S.V===0)?1:2}
function Nn(a,b){for(var c,d,e,f=a.window;;){if(a.D<=258){Kn(a);if(a.D<=258&&b===0)return 1;if(a.D===0)break}a.W=0;if(a.D>=3&&a.v>0&&(d=a.v-1,c=f[d],c===f[++d]&&c===f[++d]&&c===f[++d])){for(e=a.v+258;c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&c===f[++d]&&d<e;);a.W=258-(e-d);a.W>a.D&&(a.W=a.D)}a.W>=3?(c=Dn(a,1,a.W-3),a.D-=a.W,a.v+=a.W,a.W=0):(c=Dn(a,0,a.window[a.v]),a.D--,a.v++);if(c&&(Hn(a,!1),a.S.V===0))return 1}a.oa=0;return b===4?(Hn(a,!0),a.S.V===0?3:4):
a.Ca&&(Hn(a,!1),a.S.V===0)?1:2}
function On(a,b){for(var c;;){if(a.D===0&&(Kn(a),a.D===0)){if(b===0)return 1;break}a.W=0;c=Dn(a,0,a.window[a.v]);a.D--;a.v++;if(c&&(Hn(a,!1),a.S.V===0))return 1}a.oa=0;return b===4?(Hn(a,!0),a.S.V===0?3:4):a.Ca&&(Hn(a,!1),a.S.V===0)?1:2}
function Pn(a,b,c,d,e){this.Re=a;this.ef=b;this.lf=c;this.df=d;this.Pe=e}
var Qn;Qn=[new Pn(0,0,0,0,function(a,b){var c=65535;for(c>a.Da-5&&(c=a.Da-5);;){if(a.D<=1){Kn(a);if(a.D===0&&b===0)return 1;if(a.D===0)break}a.v+=a.D;a.D=0;var d=a.za+c;if(a.v===0||a.v>=d)if(a.D=a.v-d,a.v=d,Hn(a,!1),a.S.V===0)return 1;if(a.v-a.za>=a.pa-262&&(Hn(a,!1),a.S.V===0))return 1}a.oa=0;if(b===4)return Hn(a,!0),a.S.V===0?3:4;a.v>a.za&&Hn(a,!1);return 1}),
new Pn(4,4,8,4,Ln),new Pn(4,5,16,8,Ln),new Pn(4,6,32,32,Ln),new Pn(4,4,16,16,Mn),new Pn(8,16,32,32,Mn),new Pn(8,16,128,128,Mn),new Pn(8,32,128,256,Mn),new Pn(32,128,258,1024,Mn),new Pn(32,258,258,4096,Mn)];
function Rn(){this.S=null;this.status=0;this.ea=null;this.wrap=this.pending=this.Yb=this.Da=0;this.J=null;this.Ga=0;this.method=8;this.Db=-1;this.gb=this.kd=this.pa=0;this.window=null;this.Wd=0;this.head=this.La=null;this.zd=this.td=this.strategy=this.level=this.Wc=this.xd=this.Aa=this.D=this.Eb=this.v=this.kb=this.Cd=this.W=this.za=this.Qa=this.Pa=this.Sc=this.uc=this.U=0;this.xa=new N.Ma(1146);this.ib=new N.Ma(122);this.ma=new N.Ma(78);Fn(this.xa);Fn(this.ib);Fn(this.ma);this.nd=this.nc=this.vc=
null;this.Na=new N.Ma(16);this.fa=new N.Ma(573);Fn(this.fa);this.Bb=this.Ra=0;this.depth=new N.Ma(573);Fn(this.depth);this.ja=this.sa=this.oa=this.matches=this.Lb=this.Ta=this.Sb=this.Ca=this.Wb=this.Uc=0}
function Sn(a,b){if(!a||!a.state||b>5||b<0)return a?En(a,-2):-2;var c=a.state;if(!a.output||!a.input&&a.ra!==0||c.status===666&&b!==4)return En(a,a.V===0?-5:-2);c.S=a;var d=c.Db;c.Db=b;if(c.status===42)if(c.wrap===2)a.K=0,O(c,31),O(c,139),O(c,8),c.J?(O(c,(c.J.text?1:0)+(c.J.bb?2:0)+(c.J.extra?4:0)+(c.J.name?8:0)+(c.J.comment?16:0)),O(c,c.J.time&255),O(c,c.J.time>>8&255),O(c,c.J.time>>16&255),O(c,c.J.time>>24&255),O(c,c.level===9?2:c.strategy>=2||c.level<2?4:0),O(c,c.J.os&255),c.J.extra&&c.J.extra.length&&
(O(c,c.J.extra.length&255),O(c,c.J.extra.length>>8&255)),c.J.bb&&(a.K=Rm(a.K,c.ea,c.pending,0)),c.Ga=0,c.status=69):(O(c,0),O(c,0),O(c,0),O(c,0),O(c,0),O(c,c.level===9?2:c.strategy>=2||c.level<2?4:0),O(c,3),c.status=113);else{var e=8+(c.kd-8<<4)<<8;e|=(c.strategy>=2||c.level<2?0:c.level<6?1:c.level===6?2:3)<<6;c.v!==0&&(e|=32);c.status=113;In(c,e+(31-e%31));c.v!==0&&(In(c,a.K>>>16),In(c,a.K&65535));a.K=1}if(c.status===69)if(c.J.extra){for(e=c.pending;c.Ga<(c.J.extra.length&65535)&&(c.pending!==c.Da||
(c.J.bb&&c.pending>e&&(a.K=Rm(a.K,c.ea,c.pending-e,e)),Gn(a),e=c.pending,c.pending!==c.Da));)O(c,c.J.extra[c.Ga]&255),c.Ga++;c.J.bb&&c.pending>e&&(a.K=Rm(a.K,c.ea,c.pending-e,e));c.Ga===c.J.extra.length&&(c.Ga=0,c.status=73)}else c.status=73;if(c.status===73)if(c.J.name){e=c.pending;do{if(c.pending===c.Da&&(c.J.bb&&c.pending>e&&(a.K=Rm(a.K,c.ea,c.pending-e,e)),Gn(a),e=c.pending,c.pending===c.Da)){var f=1;break}f=c.Ga<c.J.name.length?c.J.name.charCodeAt(c.Ga++)&255:0;O(c,f)}while(f!==0);c.J.bb&&c.pending>
e&&(a.K=Rm(a.K,c.ea,c.pending-e,e));f===0&&(c.Ga=0,c.status=91)}else c.status=91;if(c.status===91)if(c.J.comment){e=c.pending;do{if(c.pending===c.Da&&(c.J.bb&&c.pending>e&&(a.K=Rm(a.K,c.ea,c.pending-e,e)),Gn(a),e=c.pending,c.pending===c.Da)){f=1;break}f=c.Ga<c.J.comment.length?c.J.comment.charCodeAt(c.Ga++)&255:0;O(c,f)}while(f!==0);c.J.bb&&c.pending>e&&(a.K=Rm(a.K,c.ea,c.pending-e,e));f===0&&(c.status=103)}else c.status=103;c.status===103&&(c.J.bb?(c.pending+2>c.Da&&Gn(a),c.pending+2<=c.Da&&(O(c,
a.K&255),O(c,a.K>>8&255),a.K=0,c.status=113)):c.status=113);if(c.pending!==0){if(Gn(a),a.V===0)return c.Db=-1,0}else if(a.ra===0&&(b<<1)-(b>4?9:0)<=(d<<1)-(d>4?9:0)&&b!==4)return En(a,-5);if(c.status===666&&a.ra!==0)return En(a,-5);if(a.ra!==0||c.D!==0||b!==0&&c.status!==666){d=c.strategy===2?On(c,b):c.strategy===3?Nn(c,b):Qn[c.level].Pe(c,b);if(d===3||d===4)c.status=666;if(d===1||d===3)return a.V===0&&(c.Db=-1),0;if(d===2&&(b===1?(on(c,2,3),pn(c,256,bn),c.ja===16?(nn(c,c.sa),c.sa=0,c.ja=0):c.ja>=
8&&(c.ea[c.pending++]=c.sa&255,c.sa>>=8,c.ja-=8)):b!==5&&(on(c,0,3),un(c,0,0),b===3&&(Fn(c.head),c.D===0&&(c.v=0,c.za=0,c.oa=0))),Gn(a),a.V===0))return c.Db=-1,0}if(b!==4)return 0;if(c.wrap<=0)return 1;c.wrap===2?(O(c,a.K&255),O(c,a.K>>8&255),O(c,a.K>>16&255),O(c,a.K>>24&255),O(c,a.pb&255),O(c,a.pb>>8&255),O(c,a.pb>>16&255),O(c,a.pb>>24&255)):(In(c,a.K>>>16),In(c,a.K&65535));Gn(a);c.wrap>0&&(c.wrap=-c.wrap);return c.pending!==0?0:1}
;let Tn={};Tn=function(){this.input=null;this.pb=this.ra=this.mb=0;this.output=null;this.hd=this.V=this.Hb=0;this.msg="";this.state=null;this.Nc=2;this.K=0};var Un=Object.prototype.toString;
function Vn(a){if(!(this instanceof Vn))return new Vn(a);a=this.options=N.assign({level:-1,method:8,chunkSize:16384,windowBits:15,memLevel:8,strategy:0,to:""},a||{});a.raw&&a.windowBits>0?a.windowBits=-a.windowBits:a.gzip&&a.windowBits>0&&a.windowBits<16&&(a.windowBits+=16);this.err=0;this.msg="";this.ended=!1;this.chunks=[];this.S=new Tn;this.S.V=0;var b=this.S;var c=a.level,d=a.method,e=a.windowBits,f=a.memLevel,g=a.strategy;if(b){var h=1;c===-1&&(c=6);e<0?(h=0,e=-e):e>15&&(h=2,e-=16);if(f<1||f>
9||d!==8||e<8||e>15||c<0||c>9||g<0||g>4)b=En(b,-2);else{e===8&&(e=9);var k=new Rn;b.state=k;k.S=b;k.wrap=h;k.J=null;k.kd=e;k.pa=1<<k.kd;k.gb=k.pa-1;k.Sc=f+7;k.uc=1<<k.Sc;k.Pa=k.uc-1;k.Qa=~~((k.Sc+3-1)/3);k.window=new N.qb(k.pa*2);k.head=new N.Ma(k.uc);k.La=new N.Ma(k.pa);k.Wb=1<<f+6;k.Da=k.Wb*4;k.ea=new N.qb(k.Da);k.Sb=1*k.Wb;k.Uc=3*k.Wb;k.level=c;k.strategy=g;k.method=d;if(b&&b.state){b.pb=b.hd=0;b.Nc=2;c=b.state;c.pending=0;c.Yb=0;c.wrap<0&&(c.wrap=-c.wrap);c.status=c.wrap?42:113;b.K=c.wrap===2?
0:1;c.Db=0;if(!Cn){d=Array(16);for(f=g=0;f<28;f++)for(fn[f]=g,e=0;e<1<<Ym[f];e++)en[g++]=f;en[g-1]=f;for(f=g=0;f<16;f++)for(gn[f]=g,e=0;e<1<<Zm[f];e++)dn[g++]=f;for(g>>=7;f<30;f++)for(gn[f]=g<<7,e=0;e<1<<Zm[f]-7;e++)dn[256+g++]=f;for(e=0;e<=15;e++)d[e]=0;for(e=0;e<=143;)bn[e*2+1]=8,e++,d[8]++;for(;e<=255;)bn[e*2+1]=9,e++,d[9]++;for(;e<=279;)bn[e*2+1]=7,e++,d[7]++;for(;e<=287;)bn[e*2+1]=8,e++,d[8]++;rn(bn,287,d);for(e=0;e<30;e++)cn[e*2+1]=5,cn[e*2]=qn(e,5);jn=new hn(bn,Ym,257,286,15);kn=new hn(cn,
Zm,0,30,15);ln=new hn([],$m,0,19,7);Cn=!0}c.vc=new mn(c.xa,jn);c.nc=new mn(c.ib,kn);c.nd=new mn(c.ma,ln);c.sa=0;c.ja=0;sn(c);c=0}else c=En(b,-2);c===0&&(b=b.state,b.Wd=2*b.pa,Fn(b.head),b.Wc=Qn[b.level].ef,b.td=Qn[b.level].Re,b.zd=Qn[b.level].lf,b.xd=Qn[b.level].df,b.v=0,b.za=0,b.D=0,b.oa=0,b.W=b.Aa=2,b.kb=0,b.U=0);b=c}}else b=-2;if(b!==0)throw Error(Wm[b]);a.header&&(b=this.S)&&b.state&&b.state.wrap===2&&(b.state.J=a.header);if(a.dictionary){var l;typeof a.dictionary==="string"?l=Pm(a.dictionary):
Un.call(a.dictionary)==="[object ArrayBuffer]"?l=new Uint8Array(a.dictionary):l=a.dictionary;a=this.S;f=l;g=f.length;if(a&&a.state)if(l=a.state,b=l.wrap,b===2||b===1&&l.status!==42||l.D)b=-2;else{b===1&&(a.K=Qm(a.K,f,g,0));l.wrap=0;g>=l.pa&&(b===0&&(Fn(l.head),l.v=0,l.za=0,l.oa=0),c=new N.qb(l.pa),N.tb(c,f,g-l.pa,l.pa,0),f=c,g=l.pa);c=a.ra;d=a.mb;e=a.input;a.ra=g;a.mb=0;a.input=f;for(Kn(l);l.D>=3;){f=l.v;g=l.D-2;do l.U=(l.U<<l.Qa^l.window[f+3-1])&l.Pa,l.La[f&l.gb]=l.head[l.U],l.head[l.U]=f,f++;while(--g);
l.v=f;l.D=2;Kn(l)}l.v+=l.D;l.za=l.v;l.oa=l.D;l.D=0;l.W=l.Aa=2;l.kb=0;a.mb=d;a.input=e;a.ra=c;l.wrap=b;b=0}else b=-2;if(b!==0)throw Error(Wm[b]);this.Th=!0}}
Vn.prototype.push=function(a,b){var c=this.S,d=this.options.chunkSize;if(this.ended)return!1;var e=b===~~b?b:b===!0?4:0;typeof a==="string"?c.input=Pm(a):Un.call(a)==="[object ArrayBuffer]"?c.input=new Uint8Array(a):c.input=a;c.mb=0;c.ra=c.input.length;do{c.V===0&&(c.output=new N.qb(d),c.Hb=0,c.V=d);a=Sn(c,e);if(a!==1&&a!==0)return Wn(this,a),this.ended=!0,!1;if(c.V===0||c.ra===0&&(e===4||e===2))if(this.options.to==="string"){var f=N.ed(c.output,c.Hb);b=f;f=f.length;if(f<65537&&(b.subarray&&Om||!b.subarray))b=
String.fromCharCode.apply(null,N.ed(b,f));else{for(var g="",h=0;h<f;h++)g+=String.fromCharCode(b[h]);b=g}this.chunks.push(b)}else b=N.ed(c.output,c.Hb),this.chunks.push(b)}while((c.ra>0||c.V===0)&&a!==1);if(e===4)return(c=this.S)&&c.state?(d=c.state.status,d!==42&&d!==69&&d!==73&&d!==91&&d!==103&&d!==113&&d!==666?a=En(c,-2):(c.state=null,a=d===113?En(c,-3):0)):a=-2,Wn(this,a),this.ended=!0,a===0;e===2&&(Wn(this,0),c.V=0);return!0};
function Wn(a,b){b===0&&(a.result=a.options.to==="string"?a.chunks.join(""):N.rd(a.chunks));a.chunks=[];a.err=b;a.msg=a.S.msg}
function Xn(a){var b=b||{};b.gzip=!0;b=new Vn(b);b.push(a,!0);if(b.err)throw b.msg||Wm[b.err];return b.result}
;function Yn(a){return a?(a=a.privateDoNotAccessOrElseSafeScriptWrappedValue)?Ya(a):null:null}
function Zn(a){return a?(a=a.privateDoNotAccessOrElseTrustedResourceUrlWrappedValue)?Ia(a):null:null}
;function $n(a){return Ia(a===null?"null":a===void 0?"undefined":a)}
;var ao=class{constructor(a){this.name=a}};var bo=new ao("rawColdConfigGroup");var co=new ao("rawHotConfigGroup");var eo=class extends G{constructor(a){super(a)}};var fo=class extends G{constructor(a){super(a)}setTrackingParams(a){return F(this,1,Ad(a,!1))}};var go=new ao("continuationCommand");var ho=new ao("webCommandMetadata");var io=new ao("signalServiceEndpoint");var jo={dg:"EMBEDDED_PLAYER_MODE_UNKNOWN",Zf:"EMBEDDED_PLAYER_MODE_DEFAULT",cg:"EMBEDDED_PLAYER_MODE_PFP",ag:"EMBEDDED_PLAYER_MODE_PFL"};var ko=new ao("feedbackEndpoint");var Id={th:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_UNKNOWN",Ag:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_FOR_TESTING",Yg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_RESUME_TO_HOME_TTL",jh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_START_TO_SHORTS_ANALYSIS_SLICE",og:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_DEVICE_LAYER_SLICE",sh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_UNIFIED_LAYER_SLICE",wh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_VISITOR_LAYER_SLICE",hh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_SHOW_SHEET_COMMAND_HANDLER_BLOCK",
zh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WIZ_NEXT_MIGRATED_COMPONENT",yh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WIZ_NEXT_CHANNEL_NAME_TOOLTIP",dh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ROTATION_LOCK_SUPPORTED",nh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_THEATER_MODE_ENABLED",Fh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_SHOW_PIN_SUGGESTION",Eh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_SHOW_LONG_PRESS_EDU_TOAST",Dh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_SHOW_AMBIENT",oh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_TIME_WATCHED_PANEL",
fh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_SEARCH_FROM_SEARCH_BAR_OVERLAY",Gh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_SHOW_VOICE_SEARCH_EDU_TOAST",mh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_SUGGESTED_LANGUAGE_SELECTED",Hh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_TRIGGER_SHORTS_PIP",Hg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_IN_ZP_VOICE_CRASHY_SET",Ug:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_REEL_FAST_SWIPE_SUPPRESSED",Tg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_REEL_FAST_SWIPE_ALLOWED",Wg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_REEL_PULL_TO_REFRESH_ATTEMPT",
Ah:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_BLOCK_KABUKI",Xg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_REEL_TALL_SCREEN",Vg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_REEL_NORMAL_SCREEN",hg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ACCESSIBILITY_MODE_ENABLED",gg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ACCESSIBILITY_MODE_DISABLED",ig:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_AUTOPLAY_ENABLED",jg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_CAST_MATCH_OCCURRED",tg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_EMC3DS_ELIGIBLE",wg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ENDSCREEN_TRIGGERED",
Sg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_POSTPLAY_TRIGGERED",Rg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_POSTPLAY_LACT_THRESHOLD_EXCEEDED",Bg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_IDENTITIES_STATE_MATCHED_ON_REMOTE_CONNECTION",Dg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_IDENTITIES_STATE_SWITCHABLE_ON_REMOTE_CONNECTION",Cg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_IDENTITIES_STATE_MISATTRIBUTED_ON_REMOTE_CONNECTION",Gg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_IDENTITIES_TV_IS_SIGNED_IN_ON_REMOTE_CONNECTION",qh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_TV_START_TYPE_COLD_ON_REMOTE_CONNECTION",
rh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_TV_START_TYPE_NON_COLD_ON_REMOTE_CONNECTION",Ng:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ON_REMOTE_CONNECTION",ng:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_COBALT_PERSISTENT_SETTINGS_TEST_VALID",lg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_COBALT_PERSISTENT_SETTINGS_TEST_INVALID",mg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_COBALT_PERSISTENT_SETTINGS_TEST_UNDEFINED",kg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_COBALT_PERSISTENT_SETTINGS_TEST_DEFINED",Ig:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_LACT_THRESHOLD_EXCEEDED",
eh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ROUND_TRIP_HANDLING_ON_REMOTE_CONNECTION",Fg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_IDENTITIES_STATE_SWITCHED_ON_REMOTE_CONNECTION_BEFORE_APP_RELOAD",Eg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_IDENTITIES_STATE_SWITCHED_ON_REMOTE_CONNECTION_AFTER_APP_RELOAD",ug:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_EMC3DS_INELIGIBLE",ph:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_TVHTML5_MID_ROLL_THRESHOLD_REACHED",yg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_EXP_COBALT_HTTP3_CONFIG_PENDING",
xg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_EXP_COBALT_HTTP3_CONFIG_ACTIVATED",vg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_EMC3DS_M2_ELIGIBLE",ah:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ROTATE_DEVICE_TO_LANDSCAPE",bh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ROTATE_DEVICE_TO_PORTRAIT",sg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_EMBEDS_FACEOFF_UI_EVENT",zg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_EXP_COBALT_HTTP3_CONFIG_RECEIVED",rg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_ELIGIBLE_TO_SUPPRESS_TRANSPORT_CONTROLS_BUTTONS",
uh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_USER_HAS_THEATER_MODE_COOKIE_ENABLED",qg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_DOCUMENT_PICTURE_IN_PICTURE_SUPPORTED",gh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_SHORTS_NON_DEFAULT_ASPECT_RATIO",Qg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_PLAYER_IN_SQUEEZEBACK",Jg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_LIVE_CREATOR_AR_GIFT_RECEIVED",Zg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_RETURNED_TO_VIDEO_AFTER_FAILED_ATTEMPT_TO_BACKGROUND",Bh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_ENTER_AUTO_ZOOM",
Og:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_PASSIVE_IN_CONTROL",Pg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_PASSIVE_IN_TREATMENT",pg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_DISABLE_PLAYER_OPEN_ON_FULLSCREEN",Mg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_MDX_RECONNECT_WITH_RETRY",ih:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_SINGLE_COLUMN_GRID_TRIGGERED",Lg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_MDX_CONNECTION_TIMEOUT",Kg:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_LIVE_GHOST_LOADING_ELIGIBLE",kh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_STREAMED_GET_WATCH_SUPPORTED",
xh:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WEBVIEW_CONTAINER",Ch:"GENERIC_CLIENT_EXPERIMENT_EVENT_TYPE_WOULD_ENTER_PIP"};var lo=new ao("shareEndpoint"),mo=new ao("shareEntityEndpoint"),no=new ao("shareEntityServiceEndpoint"),oo=new ao("webPlayerShareEntityServiceEndpoint");var po=new ao("playlistEditEndpoint");var qo=new ao("modifyChannelNotificationPreferenceEndpoint");var ro=new ao("undoFeedbackEndpoint");var so=new ao("unsubscribeEndpoint");var to=new ao("subscribeEndpoint");function uo(){var a=vo;w("yt.ads.biscotti.getId_")||v("yt.ads.biscotti.getId_",a)}
function wo(a){v("yt.ads.biscotti.lastId_",a)}
;function xo(a,b){b.length>1?a[b[0]]=b[1]:b.length===1&&Object.assign(a,b[0])}
;const yo=t.window,zo=yo?.yt?.config_||yo?.ytcfg?.data_||{};v("yt.config_",zo);function Ao(...a){xo(zo,arguments)}
function P(a,b){return a in zo?zo[a]:b}
function Bo(a){const b=zo.EXPERIMENT_FLAGS;return b?b[a]:void 0}
;const Co=[];function Do(a){Co.forEach(b=>b(a))}
function R(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){Eo(b)}}:a}
function Eo(a){var b=w("yt.logging.errors.log");b?b(a,"ERROR",void 0,void 0,void 0,void 0,void 0):(b=P("ERRORS",[]),b.push([a,"ERROR",void 0,void 0,void 0,void 0,void 0]),Ao("ERRORS",b));Do(a)}
function Fo(a,b,c,d,e){var f=w("yt.logging.errors.log");f?f(a,"WARNING",b,c,d,void 0,e):(f=P("ERRORS",[]),f.push([a,"WARNING",b,c,d,void 0,e]),Ao("ERRORS",f))}
;const Go=/^[\w.]*$/,Ho={q:!0,search_query:!0};function Io(a,b){b=a.split(b);const c={};for(let f=0,g=b.length;f<g;f++){const h=b[f].split("=");if(h.length===1&&h[0]||h.length===2)try{const k=Jo(h[0]||""),l=Jo(h[1]||"");if(k in c){const n=c[k];Array.isArray(n)?ob(n,l):c[k]=[n,l]}else c[k]=l}catch(k){var d=k,e=h[0];const l=String(Io);d.args=[{key:e,value:h[1],query:a,method:Ko===l?"unchanged":l}];Ho.hasOwnProperty(e)||Fo(d)}}return c}
const Ko=String(Io);function Lo(a){const b=[];dh(a,(c,d)=>{const e=encodeURIComponent(String(d));c=Array.isArray(c)?c:[c];hb(c,f=>{f==""?b.push(e):b.push(`${e}=${encodeURIComponent(String(f))}`)})});
return b.join("&")}
function Mo(a){a.charAt(0)==="?"&&(a=a.substring(1));return Io(a,"&")}
function No(a){return a.indexOf("?")!==-1?(a=(a||"").split("#")[0],a=a.split("?",2),Mo(a.length>1?a[1]:a[0])):{}}
function Oo(a,b){return Po(a,b||{},!0)}
function Po(a,b,c){var d=a.split("#",2);a=d[0];d=d.length>1?"#"+d[1]:"";var e=a.split("?",2);a=e[0];e=Mo(e[1]||"");for(const f in b)!c&&e!==null&&f in e||(e[f]=b[f]);return Gb(a,e)+d}
function Qo(a){if(!b)var b=window.location.href;const c=a.match(xb)[1]||null,d=zb(a);c&&d?(a=a.match(xb),b=b.match(xb),a=a[3]==b[3]&&a[1]==b[1]&&a[4]==b[4]):a=d?zb(b)===d&&(Number(b.match(xb)[4]||null)||null)===(Number(a.match(xb)[4]||null)||null):!0;return a}
function Jo(a){return a&&a.match(Go)?a:vb(a)}
;function Ro(a=w("yt.ads.biscotti.lastId_")||""){var b=So,c=Object,d=c.assign;a:{try{var e=b.h.top.location.href}catch(aa){e=2;break a}e=e?e===b.i.location.href?0:1:2}e={dt:Hl,flash:"0",frm:e};try{e.u_tz=-(new Date).getTimezoneOffset();try{var f=Al.history.length}catch(aa){f=0}e.u_his=f;e.u_h=Al.screen?.height;e.u_w=Al.screen?.width;e.u_ah=Al.screen?.availHeight;e.u_aw=Al.screen?.availWidth;e.u_cd=Al.screen?.colorDepth}catch(aa){}f=b.h;let g,h,k,l,n,m,u,p,z;try{var D=f.screenX;g=f.screenY}catch(aa){}try{h=
f.outerWidth,k=f.outerHeight}catch(aa){}try{l=f.innerWidth,n=f.innerHeight}catch(aa){}try{m=f.screenLeft,u=f.screenTop}catch(aa){}try{l=f.innerWidth,n=f.innerHeight}catch(aa){}try{p=f.screen.availWidth,z=f.screen.availTop}catch(aa){}D=[m,u,D,g,p,z,h,k,l,n];try{var B=(b.h.top||window).document,M=B.compatMode=="CSS1Compat"?B.documentElement:B.body;var K=(new ch(M.clientWidth,M.clientHeight)).round()}catch(aa){K=new ch(-12245933,-12245933)}M=K;K=new Pl;"SVGElement"in t&&"createElementNS"in t.document&&
K.set(0);B=Fl();B["allow-top-navigation-by-user-activation"]&&K.set(1);B["allow-popups-to-escape-sandbox"]&&K.set(2);t.crypto&&t.crypto.subtle&&K.set(3);"TextDecoder"in t&&"TextEncoder"in t&&K.set(4);K=Ol(K);B=M.height;M=M.width;D=D.join();b=b.i;c=d.call(c,e,{bc:K,bih:B,biw:M,brdim:D,vis:b.prerendering?3:{visible:1,hidden:2,prerender:3,preview:4,unloaded:5,"":0}[b.visibilityState||b.webkitVisibilityState||b.mozVisibilityState||""]??0,wgl:!!Al.WebGLRenderingContext});c.ca_type="image";a&&(c.bid=a);
return c}
const So=new class{constructor(a,b){this.h=a;this.i=b}}(window,window.document);v("yt.ads_.signals_.getAdSignalsString",function(a){return Lo(Ro(a))});ta();navigator.userAgent.indexOf(" (CrKey ");const To="XMLHttpRequest"in t?()=>new XMLHttpRequest:null;
function Uo(){if(!To)return null;const a=To();return"open"in a?a:null}
function Vo(a){switch(Wo(a)){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
function Wo(a){return a&&"status"in a?a.status:-1}
;function Xo(a,b){typeof a==="function"&&(a=R(a));return window.setTimeout(a,b)}
;var Yo="absolute_experiments client_dev_domain client_dev_expflag client_dev_regex_map client_dev_root_url client_rollout_override expflag forcedCapability jsfeat jsmode mods theme".split(" ");[...Yo];function S(a){a=Zo(a);return typeof a==="string"&&a==="false"?!1:!!a}
function I(a,b){a=Zo(a);return a===void 0&&b!==void 0?b:Number(a||0)}
function $o(){const a=Zo("html5_web_po_experiment_ids");return Array.isArray(a)?jb(a,b=>Number(b||0)):[Number(a||0)]}
function ap(a){a=Zo(a);return a!==void 0?String(a):""}
function Zo(a){return P("EXPERIMENT_FLAGS",{})[a]}
function bp(){const a=[],b=P("EXPERIMENTS_FORCED_FLAGS",{});for(var c of Object.keys(b))a.push({key:c,value:String(b[c])});c=P("EXPERIMENT_FLAGS",{});for(const d of Object.keys(c))d.startsWith("force_")&&b[d]===void 0&&a.push({key:d,value:String(c[d])});return a}
;const cp={Authorization:"AUTHORIZATION","X-Goog-EOM-Visitor-Id":"EOM_VISITOR_DATA","X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-Youtube-Domain-Admin-State":"DOMAIN_ADMIN_STATE","X-Youtube-Chrome-Connected":"CHROME_CONNECTED_HEADER","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-YouTube-Delegation-Context":"INNERTUBE_CONTEXT_SERIALIZED_DELEGATION_CONTEXT","X-YouTube-Device":"DEVICE","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL",
"X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-Goog-AuthUser":"SESSION_INDEX","X-Goog-PageId":"DELEGATED_SESSION_ID"},dp=["app","debugcss","debugjs","expflag","force_ad_params","force_ad_encrypted","force_viral_ad_response_params","forced_experiments","innertube_snapshots","innertube_goldens","internalcountrycode","internalipoverride","absolute_experiments","conditional_experiments","sbb","sr_bns_address",...Yo];let ep=!1;
function fp(a,b,c="GET",d="",e,f,g,h=!1,k){const l=Uo();if(!l)return null;const n=()=>{(l&&"readyState"in l?l.readyState:0)===4&&b&&R(b)(l)};
"onloadend"in l?l.addEventListener("loadend",n,!1):l.onreadystatechange=n;S("debug_forward_web_query_parameters")&&(a=gp(a));l.open(c,a,!0);f&&(l.responseType=f);g&&(l.withCredentials=!0);c=c==="POST"&&(window.FormData===void 0||!(d instanceof FormData));if(e=hp(a,e))for(const m in e)l.setRequestHeader(m,e[m]),"content-type"===m.toLowerCase()&&(c=!1);c&&l.setRequestHeader("Content-Type","application/x-www-form-urlencoded");k&&"onprogress"in l&&(l.onprogress=()=>{k(l.responseText)});
if(h&&"setAttributionReporting"in XMLHttpRequest.prototype){a={eventSourceEligible:!0,triggerEligible:!1};try{l.setAttributionReporting(a)}catch(m){Fo(m)}}l.send(d);return l}
function hp(a,b={}){const c=Qo(a),d=P("INNERTUBE_CLIENT_NAME"),e=S("web_ajax_ignore_global_headers_if_set");for(const h in cp){let k=P(cp[h]);const l=h==="X-Goog-AuthUser"||h==="X-Goog-PageId";h!=="X-Goog-Visitor-Id"||k||(k=P("VISITOR_DATA"));var f;if(!(f=!k)){if(!(f=c||(zb(a)?!1:!0))){f=a;var g;if(g=S("add_auth_headers_to_remarketing_google_dot_com_ping")&&h==="Authorization"&&(d==="TVHTML5"||d==="TVHTML5_UNPLUGGED"||d==="TVHTML5_SIMPLY"))g=zb(f),g=g!==null?g.split(".").reverse():null,g=g===null?
!1:g[1]==="google"?!0:g[2]==="google"?g[0]==="au"&&g[1]==="com"?!0:g[0]==="uk"&&g[1]==="co"?!0:!1:!1;g&&(f=Ab(f)||"",f=f.split("/"),f="/"+(f.length>1?f[1]:""),g=f==="/pagead");f=g?!0:!1}f=!f}f||e&&b[h]!==void 0||d==="TVHTML5_UNPLUGGED"&&l||(b[h]=k)}"X-Goog-EOM-Visitor-Id"in b&&"X-Goog-Visitor-Id"in b&&delete b["X-Goog-Visitor-Id"];if(c||!zb(a))b["X-YouTube-Utc-Offset"]=String(-(new Date).getTimezoneOffset());if(c||!zb(a)){let h;try{h=(new Intl.DateTimeFormat).resolvedOptions().timeZone}catch{}h&&
(b["X-YouTube-Time-Zone"]=h)}document.location.hostname.endsWith("youtubeeducation.com")||!c&&zb(a)||(b["X-YouTube-Ad-Signals"]=Lo(Ro()));return b}
function ip(a,b){b.method="POST";b.postParams||(b.postParams={});return jp(a,b)}
function jp(a,b){const c=b.format||"JSON";a=kp(a,b);var d=lp(a,b);let e=!1,f;const g=mp(a,h=>{if(!e){e=!0;f&&window.clearTimeout(f);var k=Vo(h),l=null,n=400<=h.status&&h.status<500,m=500<=h.status&&h.status<600;if(k||n||m)l=np(a,c,h,b.convertToSafeHtml);k&&(k=op(c,h,l));l=l||{};n=b.context||t;k?b.onSuccess&&b.onSuccess.call(n,h,l):b.onError&&b.onError.call(n,h,l);b.onFinish&&b.onFinish.call(n,h,l)}},b.method,d,b.headers,b.responseType,b.withCredentials,!1,b.onProgress);
d=b.timeout||0;if(b.onTimeout&&d>0){const h=b.onTimeout;f=Xo(()=>{e||(e=!0,g.abort(),window.clearTimeout(f),h.call(b.context||t,g))},d)}return g}
function kp(a,b){b.includeDomain&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);const c=P("XSRF_FIELD_NAME");if(b=b.urlParams)b[c]&&delete b[c],a=Oo(a,b);return a}
function lp(a,b){const c=P("XSRF_FIELD_NAME"),d=P("XSRF_TOKEN");var e=b.postBody||"",f=b.postParams;const g=P("XSRF_FIELD_NAME");let h;b.headers&&(h=b.headers["Content-Type"]);b.excludeXsrf||zb(a)&&!b.withCredentials&&zb(a)!==document.location.hostname||b.method!=="POST"||h&&h!=="application/x-www-form-urlencoded"||b.postParams&&b.postParams[g]||(f||(f={}),f[c]=d);(S("ajax_parse_query_data_only_when_filled")&&f&&Object.keys(f).length>0||f)&&typeof e==="string"&&(e=Mo(e),oh(e,f),e=b.postBodyFormat&&
b.postBodyFormat==="JSON"?JSON.stringify(e):Fb(e));f=e||f&&!hh(f);!ep&&f&&b.method!=="POST"&&(ep=!0,Eo(Error("AJAX request with postData should use POST")));return e}
function np(a,b,c,d){let e=null;switch(b){case "JSON":let f;try{f=c.responseText}catch(g){throw d=Error("Error reading responseText"),d.params=a,Fo(d),g;}a=c.getResponseHeader("Content-Type")||"";if(f&&a.indexOf("json")>=0){f.substring(0,5)===")]}'\n"&&(f=f.substring(5));try{e=JSON.parse(f)}catch(g){}}break;case "XML":if(a=(a=c.responseXML)?pp(a):null)e={},hb(a.getElementsByTagName("*"),g=>{e[g.tagName]=qp(g)})}d&&rp(e);
return e}
function rp(a){if(ma(a))for(const c in a){var b;(b=c==="html_content")||(b=c.length-5,b=b>=0&&c.indexOf("_html",b)==b);if(b){b=a[c];const d=Ga();b=d?d.createHTML(b):b;a[c]=new Va(b)}else rp(a[c])}}
function op(a,b,c){if(b&&b.status===204)return!0;switch(a){case "JSON":return!!c;case "XML":return Number(c&&c.return_code)===0;case "RAW":return!0;default:return!!c}}
function pp(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&a.length>0?a[0]:null:null}
function qp(a){let b="";hb(a.childNodes,c=>{b+=c.nodeValue});
return b}
function gp(a){var b=window.location.search,c=zb(a);S("debug_handle_relative_url_for_query_forward_killswitch")||!c&&Qo(a)&&(c=document.location.hostname);var d=Ab(a);d=(c=c&&(c.endsWith("youtube.com")||c.endsWith("youtube-nocookie.com")))&&d&&d.startsWith("/api/");if(!c||d)return a;const e=Mo(b),f={};hb(dp,g=>{e[g]&&(f[g]=e[g])});
return Po(a,f||{},!1)}
var mp=fp;const sp=[{Xc:a=>`Cannot read property '${a.key}'`,
Cc:{Error:[{regexp:/(Permission denied) to access property "([^']+)"/,groups:["reason","key"]}],TypeError:[{regexp:/Cannot read property '([^']+)' of (null|undefined)/,groups:["key","value"]},{regexp:/\u65e0\u6cd5\u83b7\u53d6\u672a\u5b9a\u4e49\u6216 (null|undefined) \u5f15\u7528\u7684\u5c5e\u6027\u201c([^\u201d]+)\u201d/,groups:["value","key"]},{regexp:/\uc815\uc758\ub418\uc9c0 \uc54a\uc74c \ub610\ub294 (null|undefined) \ucc38\uc870\uc778 '([^']+)' \uc18d\uc131\uc744 \uac00\uc838\uc62c \uc218 \uc5c6\uc2b5\ub2c8\ub2e4./,
groups:["value","key"]},{regexp:/No se puede obtener la propiedad '([^']+)' de referencia nula o sin definir/,groups:["key"]},{regexp:/Unable to get property '([^']+)' of (undefined or null) reference/,groups:["key","value"]},{regexp:/(null) is not an object \(evaluating '(?:([^.]+)\.)?([^']+)'\)/,groups:["value","base","key"]}]}},{Xc:a=>`Cannot call '${a.key}'`,
Cc:{TypeError:[{regexp:/(?:([^ ]+)?\.)?([^ ]+) is not a function/,groups:["base","key"]},{regexp:/([^ ]+) called on (null or undefined)/,groups:["key","value"]},{regexp:/Object (.*) has no method '([^ ]+)'/,groups:["base","key"]},{regexp:/Object doesn't support property or method '([^ ]+)'/,groups:["key"]},{regexp:/\u30aa\u30d6\u30b8\u30a7\u30af\u30c8\u306f '([^']+)' \u30d7\u30ed\u30d1\u30c6\u30a3\u307e\u305f\u306f\u30e1\u30bd\u30c3\u30c9\u3092\u30b5\u30dd\u30fc\u30c8\u3057\u3066\u3044\u307e\u305b\u3093/,
groups:["key"]},{regexp:/\uac1c\uccb4\uac00 '([^']+)' \uc18d\uc131\uc774\ub098 \uba54\uc11c\ub4dc\ub97c \uc9c0\uc6d0\ud558\uc9c0 \uc54a\uc2b5\ub2c8\ub2e4./,groups:["key"]}]}},{Xc:a=>`${a.key} is not defined`,
Cc:{ReferenceError:[{regexp:/(.*) is not defined/,groups:["key"]},{regexp:/Can't find variable: (.*)/,groups:["key"]}]}}];var vp={cb:[],Za:[{callback:tp,weight:500},{callback:up,weight:500}]};function tp(a){if(a.name==="JavaException")return!0;a=a.stack;return a.includes("chrome://")||a.includes("-extension://")||a.includes("webkit-masked-url://")}
function up(a){if(!a.stack)return!0;const b=!a.stack.includes("\n");return b&&a.stack.includes("ErrorType: ")||b&&a.stack.includes("Anonymous function (Unknown script")||a.stack.toLowerCase()==="not available"||a.fileName==="user-script"||a.fileName.startsWith("user-script:")?!0:!1}
;function wp(){if(!xp){var a=xp=new yp;a.cb.length=0;a.Za.length=0;zp(a,vp)}return xp}
function zp(a,b){b.cb&&a.cb.unshift.apply(a.cb,b.cb);b.Za&&a.Za.unshift.apply(a.Za,b.Za)}
var yp=class{constructor(){this.Za=[];this.cb=[]}},xp;const Ap=new L;function Bp(a){const b=a.length;let c=0;const d=()=>a.charCodeAt(c++);
do{var e=Cp(d);if(e===Infinity)break;const f=e>>3;switch(e&7){case 0:e=Cp(d);if(f===2)return e;break;case 1:if(f===2)return;c+=8;break;case 2:e=Cp(d);if(f===2)return a.substr(c,e);c+=e;break;case 5:if(f===2)return;c+=4;break;default:return}}while(c<b)}
function Cp(a){let b=a(),c=b&127;if(b<128)return c;b=a();c|=(b&127)<<7;if(b<128)return c;b=a();c|=(b&127)<<14;if(b<128)return c;b=a();return b<128?c|(b&127)<<21:Infinity}
;function Dp(a,b,c,d){if(a)if(Array.isArray(a)){var e=d;for(d=0;d<a.length&&!(a[d]&&(e+=Ep(d,a[d],b,c),e>500));d++);d=e}else if(typeof a==="object")for(e in a){if(a[e]){a:{var f=e;var g=a[e],h=b,k=c;if(typeof g!=="string"||f!=="clickTrackingParams"&&f!=="trackingParams"){f=0;break a}f=(g=Bp(atob(g.replace(/-/g,"+").replace(/_/g,"/"))))?Ep(`${f}.ve`,g,h,k):0}d+=f;d+=Ep(e,a[e],b,c);if(d>500)break}}else c[b]=Fp(a),d+=c[b].length;else c[b]=Fp(a),d+=c[b].length;return d}
function Ep(a,b,c,d){c+=`.${a}`;a=Fp(b);d[c]=a;return c.length+a.length}
function Fp(a){try{return(typeof a==="string"?a:String(JSON.stringify(a))).substr(0,500)}catch(b){return`unable to serialize ${typeof a} (${b.message})`}}
;function Gp(){if(!t.matchMedia)return"WEB_DISPLAY_MODE_UNKNOWN";try{return t.matchMedia("(display-mode: standalone)").matches?"WEB_DISPLAY_MODE_STANDALONE":t.matchMedia("(display-mode: minimal-ui)").matches?"WEB_DISPLAY_MODE_MINIMAL_UI":t.matchMedia("(display-mode: fullscreen)").matches?"WEB_DISPLAY_MODE_FULLSCREEN":t.matchMedia("(display-mode: browser)").matches?"WEB_DISPLAY_MODE_BROWSER":"WEB_DISPLAY_MODE_UNKNOWN"}catch(a){return"WEB_DISPLAY_MODE_UNKNOWN"}}
var Hp=class{constructor(a){this.i=void 0;this.h=!1;a.addEventListener("beforeinstallprompt",b=>{b.preventDefault();this.i=b});
a.addEventListener("appinstalled",()=>{this.h=!0},{once:!0})}};function Ip(a){const b={};var c=[];"USER_SESSION_ID"in zo&&c.push({key:"u",value:P("USER_SESSION_ID")});if(c=Wg(c))b.Authorization=c,c=a=a?.sessionIndex,c===void 0&&(c=Number(P("SESSION_INDEX",0)),c=isNaN(c)?0:c),S("voice_search_auth_header_removal")||(b["X-Goog-AuthUser"]=c.toString()),"INNERTUBE_HOST_OVERRIDE"in zo||(b["X-Origin"]=window.location.origin),a===void 0&&"DELEGATED_SESSION_ID"in zo&&(b["X-Goog-PageId"]=P("DELEGATED_SESSION_ID"));return b}
var Jp=class{constructor(){this.Md=!0}};var Kp={identityType:"UNAUTHENTICATED_IDENTITY_TYPE_UNKNOWN"};function Lp(a,b,c,d="youtube.com",e=!1){Tg.set(""+a,b,{wc:c,path:"/",domain:d,secure:e})}
function Mp(a){return Tg.get(""+a,void 0)}
function Np(a,b="/",c="youtube.com"){Tg.remove(""+a,b,c)}
function Op(){if(!Tg.isEnabled())return!1;if(Tg.h.cookie)return!0;Tg.set("TESTCOOKIESENABLED","1",{wc:60});if(Tg.get("TESTCOOKIESENABLED")!=="1")return!1;Tg.remove("TESTCOOKIESENABLED");return!0}
;const Pp=w("ytglobal.prefsUserPrefsPrefs_")||{};v("ytglobal.prefsUserPrefsPrefs_",Pp);function Qp(){Rp||(Rp=new Sp);return Rp}
function Tp(a){return!!((Up(`f${Math.floor(a/31)+1}`)||0)&1<<a%31)}
function Vp(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error(`ExpectedRegexMatch: ${a}`);}
function Wp(a){if(!/^\w+$/.test(a))throw Error(`ExpectedRegexMismatch: ${a}`);}
function Up(a){a=Pp[a]!==void 0?Pp[a].toString():null;return a!=null&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
var Sp=class{constructor(){this.h=P("ALT_PREF_COOKIE_NAME","PREF");this.i=P("ALT_PREF_COOKIE_DOMAIN","youtube.com");const a=Mp(this.h);a&&this.parse(a)}get(a,b){Wp(a);Vp(a);a=Pp[a]!==void 0?Pp[a].toString():null;return a!=null?a:b?b:""}set(a,b){Wp(a);Vp(a);if(b==null)throw Error("ExpectedNotNull");Pp[a]=b.toString()}remove(a){Wp(a);Vp(a);delete Pp[a]}clear(){for(const a in Pp)delete Pp[a]}parse(a){a=decodeURIComponent(a).split("&");for(let c=0;c<a.length;c++){var b=a[c].split("=");const d=b[0];(b=
b[1])&&(Pp[d]=b.toString())}}},Rp;const Xp={bluetooth:"CONN_DISCO",cellular:"CONN_CELLULAR_UNKNOWN",ethernet:"CONN_WIFI",none:"CONN_NONE",wifi:"CONN_WIFI",wimax:"CONN_CELLULAR_4G",other:"CONN_UNKNOWN",unknown:"CONN_UNKNOWN","slow-2g":"CONN_CELLULAR_2G","2g":"CONN_CELLULAR_2G","3g":"CONN_CELLULAR_3G","4g":"CONN_CELLULAR_4G"},Yp={"slow-2g":"EFFECTIVE_CONNECTION_TYPE_SLOW_2G","2g":"EFFECTIVE_CONNECTION_TYPE_2G","3g":"EFFECTIVE_CONNECTION_TYPE_3G","4g":"EFFECTIVE_CONNECTION_TYPE_4G"};
function Zp(){const a=t.navigator;return a?a.connection:void 0}
function $p(){var a=Zp();if(a){var b=Xp[a.type||"unknown"]||"CONN_UNKNOWN";a=Xp[a.effectiveType||"unknown"]||"CONN_UNKNOWN";b==="CONN_CELLULAR_UNKNOWN"&&a!=="CONN_UNKNOWN"&&(b=a);if(b!=="CONN_UNKNOWN")return b;if(a!=="CONN_UNKNOWN")return a}}
function aq(){var a=Zp();if(a?.effectiveType)return Yp.hasOwnProperty(a.effectiveType)?Yp[a.effectiveType]:"EFFECTIVE_CONNECTION_TYPE_UNKNOWN"}
;var T=class extends Error{constructor(a,...b){super(a);this.args=[...b];Object.setPrototypeOf(this,new.target.prototype)}};function bq(){try{return cq(),!0}catch(a){return!1}}
function cq(a="unknown"){if(P("DATASYNC_ID")!==void 0)return P("DATASYNC_ID");throw new T("Datasync ID not set",a);}
;function dq(a,b){return Kl.Xa(a,0,b)}
var eq=class{va(a,b){return this.Xa(a,1,b)}G(a){const b=w("yt.scheduler.instance.addImmediateJob");b?b(a):a()}};var fq=I("web_emulated_idle_callback_delay",300);const gq=1E3/60-3,hq=[8,5,4,3,2,1,0];function iq(a,b){try{b()}catch(c){a.ta(c)}}
function jq(a){if(a.i[8].length){if(a.Y)return 4;if(kq(a))return 3}for(let b=5;b>=a.o;b--)if(a.i[b].length>0)return b>0?kq(a)?3:2:1;return 0}
function lq(a){a.P.length=0;for(let b=5;b>=0;b--)a.i[b].length=0;a.i[8].length=0;a.j={};a.stop()}
function kq(a){return!a.isHidden()&&a.qa}
function mq(a){for(const b of hq)if(a.i[b].length)return!0;return!1}
function nq(a,b,c){a.Y&&a.A===4&&a.h||a.stop();a.u=!0;b=ta()+(b||a.F);for(var d=a.i[5];d.length;){var e=d.shift(),f=a.j[e];delete a.j[e];if(f){e=a;try{f(c)}catch(g){e.ta(g)}}}for(d=a.i[4];d.length;)c=d.shift(),f=a.j[c],delete a.j[c],f&&iq(a,f);d=a.la?0:1;d=a.o>d?a.o:d;if(!(ta()>=b)){do{a:{c=a;f=d;for(e=3;e>=f;e--){const g=c.i[e];for(;g.length;){const h=g.shift(),k=c.j[h];delete c.j[h];if(k){c=k;break a}}}c=null}c&&iq(a,c)}while(c&&ta()<b)}a.u=!1;oq(a);a.F=gq;mq(a)&&a.start()}
function pq(a){a.stop();a.u=!0;var b=ta();const c=a.i[8];for(;c.length;){const d=c.shift(),e=a.j[d];delete a.j[d];e&&iq(a,e)}oq(a);a.u=!1;mq(a)&&a.start();b=ta()-b;a.F-=b}
function oq(a){for(let b=0,c=a.P.length;b<c;b++){const d=a.P[b];a.i[d.priority].push(d.id)}a.P.length=0}
var qq=class extends y{constructor(a={}){super();this.i=[];this.j={};this.ga=this.h=0;this.Z=this.u=!1;this.P=[];this.Y=this.la=!1;for(const b of hq)this.i[b]=[];this.o=0;this.be=a.timeout||1;this.F=gq;this.A=0;this.Fa=this.de.bind(this);this.Zd=this.we.bind(this);this.Wa=this.Ja.bind(this);this.Ob=this.ce.bind(this);this.Mc=this.ke.bind(this);this.Ba=!!window.requestIdleCallback&&!!window.cancelIdleCallback&&!S("disable_scheduler_requestIdleCallback");(this.qa=a.useRaf!==!1&&!!window.requestAnimationFrame)&&
document.addEventListener("visibilitychange",this.Fa)}G(a){const b=ta();iq(this,a);a=ta()-b;this.u||(this.F-=a)}Xa(a,b,c){++this.ga;if(b===10)return this.G(a),this.ga;const d=this.ga;this.j[d]=a;this.u&&!c?this.P.push({id:d,priority:b}):(this.i[b].push(d),this.Z||this.u||(this.h!==0&&jq(this)!==this.A&&this.stop(),this.start()));return d}wa(a){delete this.j[a]}isHidden(){return!!document.hidden||!1}ta(a){const b=w("yt.logging.errors.log");b&&b(a)}ce(a){let b=void 0;a&&(b=a.timeRemaining());this.la=
!0;nq(this,b);this.la=!1}we(){nq(this)}Ja(){pq(this)}ke(a){this.Y=!0;const b=jq(this);b===4&&b!==this.A&&(this.stop(),this.start());nq(this,void 0,a);this.Y=!1}de(){this.isHidden()||pq(this);this.h&&(this.stop(),this.start())}start(){this.Z=!1;if(this.h===0)switch(this.A=jq(this),this.A){case 1:var a=this.Ob;this.h=this.Ba?window.requestIdleCallback(a,{timeout:3E3}):window.setTimeout(a,fq);break;case 2:this.h=window.setTimeout(this.Zd,this.be);break;case 3:this.h=window.requestAnimationFrame(this.Mc);
break;case 4:this.h=window.setTimeout(this.Wa,0)}}pause(){this.stop();this.Z=!0}stop(){if(this.h){switch(this.A){case 1:var a=this.h;this.Ba?window.cancelIdleCallback(a):window.clearTimeout(a);break;case 2:case 4:window.clearTimeout(this.h);break;case 3:window.cancelAnimationFrame(this.h)}this.h=0}}ba(){lq(this);this.stop();this.qa&&document.removeEventListener("visibilitychange",this.Fa);super.ba()}};const rq=w("yt.scheduler.instance.timerIdMap_")||{},sq=I("kevlar_tuner_scheduler_soft_state_timer_ms",800);let tq=0,uq=0;function vq(){let a=w("ytglobal.schedulerInstanceInstance_");if(!a||a.I)a=new qq(P("scheduler")||{}),v("ytglobal.schedulerInstanceInstance_",a);return a}
function wq(){xq();const a=w("ytglobal.schedulerInstanceInstance_");a&&(Mb(a),v("ytglobal.schedulerInstanceInstance_",null))}
function xq(){lq(vq());for(const a in rq)rq.hasOwnProperty(a)&&delete rq[Number(a)]}
function yq(a,b,c){if(!c)return c=c===void 0,-vq().Xa(a,b,c);const d=window.setTimeout(()=>{const e=vq().Xa(a,b);rq[d]=e},c);
return d}
function zq(a){vq().G(a)}
function Aq(a){const b=vq();if(a<0)b.wa(-a);else{var c=rq[a];c?(b.wa(c),delete rq[a]):window.clearTimeout(a)}}
function Bq(){Cq()}
function Cq(){window.clearTimeout(tq);vq().start()}
function Dq(){vq().pause();window.clearTimeout(tq);tq=window.setTimeout(Bq,sq)}
function Eq(){window.clearTimeout(uq);uq=window.setTimeout(()=>{Fq(0)},sq)}
function Fq(a){Eq();var b=vq();b.o=a;b.start()}
function Gq(a){Eq();var b=vq();b.o>a&&(b.o=a,b.start())}
function Hq(){window.clearTimeout(uq);var a=vq();a.o=0;a.start()}
;function Iq(){Jq.instance||(Jq.instance=new Jq);return Jq.instance}
var Jq=class extends eq{Xa(a,b,c){c!==void 0&&Number.isNaN(Number(c))&&(c=void 0);const d=w("yt.scheduler.instance.addJob");return d?d(a,b,c):c===void 0?(a(),NaN):Xo(a,c||0)}wa(a){if(a===void 0||!Number.isNaN(Number(a))){var b=w("yt.scheduler.instance.cancelJob");b?b(a):window.clearTimeout(a)}}start(){const a=w("yt.scheduler.instance.start");a&&a()}pause(){const a=w("yt.scheduler.instance.pause");a&&a()}},Kl=Iq();
w("yt.scheduler.initialized")||(v("yt.scheduler.instance.dispose",wq),v("yt.scheduler.instance.addJob",yq),v("yt.scheduler.instance.addImmediateJob",zq),v("yt.scheduler.instance.cancelJob",Aq),v("yt.scheduler.instance.cancelAllJobs",xq),v("yt.scheduler.instance.start",Cq),v("yt.scheduler.instance.pause",Dq),v("yt.scheduler.instance.setPriorityThreshold",Fq),v("yt.scheduler.instance.enablePriorityThreshold",Gq),v("yt.scheduler.instance.clearPriorityThreshold",Hq),v("yt.scheduler.initialized",!0));const Kq=class{constructor(a){const b=new om;this.h=(a=b.isAvailable()?a?new pm(b,a):b:null)?new jm(a):null;this.j=document.domain||window.location.hostname}i(){return!!this.h}set(a,b,c,d){c=c||31104E3;this.remove(a);if(this.i())try{this.h.set(a,b,Date.now()+c*1E3);return}catch(f){}var e="";if(d)try{e=escape((new Ej).serialize(b))}catch(f){return}else e=escape(b);Lp(a,e,c,this.j)}get(a,b){var c=void 0,d=!this.i();if(!d)try{c=this.h.get(a)}catch(e){d=!0}if(d&&(c=Mp(a))&&(c=unescape(c),b))try{c=JSON.parse(c)}catch(e){this.remove(a),
c=void 0}return c}remove(a){this.i()&&this.h.remove(a);Np(a,"/",this.j)}};const Lq=(()=>{let a;return()=>{a||(a=new Kq("ytidb"));return a}})();
function Mq(){return Lq()?.get("LAST_RESULT_ENTRY_KEY",!0)}
;const Nq=[];let Oq,Pq=!1;function Qq(){({handleError:a=Rq,logEvent:b=Sq}={});var a;for(Oq=new Tq(a,b);Nq.length>0;){var b=Nq.shift();switch(b.type){case "ERROR":Oq.ta(b.payload);break;case "EVENT":Oq.logEvent(b.eventType,b.payload)}}}
function Uq(a){Pq||(Oq?Oq.ta(a):(Nq.push({type:"ERROR",payload:a}),Nq.length>10&&Nq.shift()))}
function Vq(a,b){Pq||(Oq?Oq.logEvent(a,b):(Nq.push({type:"EVENT",eventType:a,payload:b}),Nq.length>10&&Nq.shift()))}
;function Wq(a){if(a.indexOf(":")>=0)throw Error("Database name cannot contain ':'");}
function Xq(a){return a.substr(0,a.indexOf(":"))||a}
;var Yq=Qc||Rc;function Zq(a){const b=zc();return b?b.toLowerCase().indexOf(a)>=0:!1}
;const $q={AUTH_INVALID:"No user identifier specified.",EXPLICIT_ABORT:"Transaction was explicitly aborted.",IDB_NOT_SUPPORTED:"IndexedDB is not supported.",MISSING_INDEX:"Index not created.",MISSING_OBJECT_STORES:"Object stores not created.",DB_DELETED_BY_MISSING_OBJECT_STORES:"Database is deleted because expected object stores were not created.",DB_REOPENED_BY_MISSING_OBJECT_STORES:"Database is reopened because expected object stores were not created.",UNKNOWN_ABORT:"Transaction was aborted for unknown reasons.",
QUOTA_EXCEEDED:"The current transaction exceeded its quota limitations.",QUOTA_MAYBE_EXCEEDED:"The current transaction may have failed because of exceeding quota limitations.",EXECUTE_TRANSACTION_ON_CLOSED_DB:"Can't start a transaction on a closed database",INCOMPATIBLE_DB_VERSION:"The binary is incompatible with the database version"},ar={AUTH_INVALID:"ERROR",EXECUTE_TRANSACTION_ON_CLOSED_DB:"WARNING",EXPLICIT_ABORT:"IGNORED",IDB_NOT_SUPPORTED:"ERROR",MISSING_INDEX:"WARNING",MISSING_OBJECT_STORES:"ERROR",
DB_DELETED_BY_MISSING_OBJECT_STORES:"WARNING",DB_REOPENED_BY_MISSING_OBJECT_STORES:"WARNING",QUOTA_EXCEEDED:"WARNING",QUOTA_MAYBE_EXCEEDED:"WARNING",UNKNOWN_ABORT:"WARNING",INCOMPATIBLE_DB_VERSION:"WARNING"},br={AUTH_INVALID:!1,EXECUTE_TRANSACTION_ON_CLOSED_DB:!1,EXPLICIT_ABORT:!1,IDB_NOT_SUPPORTED:!1,MISSING_INDEX:!1,MISSING_OBJECT_STORES:!1,DB_DELETED_BY_MISSING_OBJECT_STORES:!1,DB_REOPENED_BY_MISSING_OBJECT_STORES:!1,QUOTA_EXCEEDED:!1,QUOTA_MAYBE_EXCEEDED:!0,UNKNOWN_ABORT:!0,INCOMPATIBLE_DB_VERSION:!1};
var U=class extends T{constructor(a,b={},c=$q[a],d=ar[a],e=br[a]){super(c,{name:"YtIdbKnownError",isSw:self.document===void 0,isIframe:self!==self.top,type:a,...b});this.type=a;this.message=c;this.level=d;this.h=e;Object.setPrototypeOf(this,U.prototype)}},cr=class extends U{constructor(a,b){super("MISSING_OBJECT_STORES",{expectedObjectStores:b,foundObjectStores:a},$q.MISSING_OBJECT_STORES);Object.setPrototypeOf(this,cr.prototype)}},dr=class extends Error{constructor(a,b){super();this.index=a;this.objectStore=
b;Object.setPrototypeOf(this,dr.prototype)}};const er=["The database connection is closing","Can't start a transaction on a closed database","A mutation operation was attempted on a database that did not allow mutations"];
function fr(a,b,c,d){b=Xq(b);let e;e=a instanceof Error?a:Error(`Unexpected error: ${a}`);if(e instanceof U)return e;a={objectStoreNames:c,dbName:b,dbVersion:d};if(e.name==="QuotaExceededError")return new U("QUOTA_EXCEEDED",a);if(Sc&&e.name==="UnknownError")return new U("QUOTA_MAYBE_EXCEEDED",a);if(e instanceof dr)return new U("MISSING_INDEX",{...a,objectStore:e.objectStore,index:e.index});if(e.name==="InvalidStateError"&&er.some(f=>e.message.includes(f)))return new U("EXECUTE_TRANSACTION_ON_CLOSED_DB",
a);
if(e.name==="AbortError")return new U("UNKNOWN_ABORT",a,e.message);e.args=[{...a,name:"IdbError",Bd:e.name}];e.level="WARNING";return e}
function gr(a,b,c){const d=Mq();return new U("IDB_NOT_SUPPORTED",{context:{caller:a,publicName:b,version:c,hasSucceededOnce:d?.hasSucceededOnce}})}
;function hr(a){if(!a)throw Error();throw a;}
function ir(a){return a}
var jr=class{constructor(a){this.h=a}};function kr(a,b,c,d,e){try{if(a.state.status!=="FULFILLED")throw Error("calling handleResolve before the promise is fulfilled.");const f=c(a.state.value);f instanceof lr?mr(a,b,f,d,e):d(f)}catch(f){e(f)}}
function nr(a,b,c,d,e){try{if(a.state.status!=="REJECTED")throw Error("calling handleReject before the promise is rejected.");const f=c(a.state.reason);f instanceof lr?mr(a,b,f,d,e):d(f)}catch(f){e(f)}}
function mr(a,b,c,d,e){b===c?e(new TypeError("Circular promise chain detected.")):c.then(f=>{f instanceof lr?mr(a,b,f,d,e):d(f)},f=>{e(f)})}
var lr=class{constructor(a){this.state={status:"PENDING"};this.h=[];this.i=[];a=a.h;const b=d=>{if(this.state.status==="PENDING"){this.state={status:"FULFILLED",value:d};for(const e of this.h)e()}},c=d=>{if(this.state.status==="PENDING"){this.state={status:"REJECTED",
reason:d};for(const e of this.i)e()}};
try{a(b,c)}catch(d){c(d)}}static all(a){return new lr(new jr((b,c)=>{const d=[];let e=a.length;e===0&&b(d);for(let f=0;f<a.length;++f)lr.resolve(a[f]).then(g=>{d[f]=g;e--;e===0&&b(d)}).catch(g=>{c(g)})}))}static resolve(a){return new lr(new jr((b,c)=>{a instanceof lr?a.then(b,c):b(a)}))}static reject(a){return new lr(new jr((b,c)=>{c(a)}))}then(a,b){const c=a??ir,d=b??hr;
return new lr(new jr((e,f)=>{this.state.status==="PENDING"?(this.h.push(()=>{kr(this,this,c,e,f)}),this.i.push(()=>{nr(this,this,d,e,f)})):this.state.status==="FULFILLED"?kr(this,this,c,e,f):this.state.status==="REJECTED"&&nr(this,this,d,e,f)}))}catch(a){return this.then(void 0,a)}};function or(a,b,c){const d=()=>{try{a.removeEventListener("success",e),a.removeEventListener("error",f)}catch{}},e=()=>{b(a.result);
d()},f=()=>{c(a.error);
d()};
a.addEventListener("success",e);a.addEventListener("error",f)}
function pr(a){return new Promise((b,c)=>{or(a,b,c)})}
function qr(a){return new lr(new jr((b,c)=>{or(a,b,c)}))}
;function rr(a,b){return new lr(new jr((c,d)=>{const e=()=>{const f=a?b(a):null;f?f.then(g=>{a=g;e()},d):c()};
e()}))}
;const sr=window;var V=sr.ytcsi&&sr.ytcsi.now?sr.ytcsi.now:sr.performance&&sr.performance.timing&&sr.performance.now&&sr.performance.timing.navigationStart?()=>sr.performance.timing.navigationStart+sr.performance.now():()=>(new Date).getTime();function tr(){return S("idb_immediate_commit")}
async function ur(a,b,c,d){const e={mode:"readonly",na:!1,tag:"IDB_TRANSACTION_TAG_UNKNOWN"};typeof c==="string"?e.mode=c:Object.assign(e,c);a.transactionCount++;c=e.na?3:1;let f=0,g;for(;!g;){f++;const n=Math.round(V());try{var h=a.h.transaction(b,e.mode),k=d,l=!!e.commit;const m=new vr(h),u=await wr(m,k,l),p=Math.round(V());xr(a,n,p,f,void 0,b.join(),e);return u}catch(m){k=Math.round(V());const u=fr(m,a.h.name,b.join(),a.h.version);if(u instanceof U&&!u.h||f>=c)xr(a,n,k,f,u,b.join(),e),g=u}}return Promise.reject(g)}
function yr(a,b,c){a=a.h.createObjectStore(b,c);return new zr(a)}
function Ar(a,b,c){return ur(a,[b],{mode:"readwrite",na:!0,commit:tr()},d=>{d=d.objectStore(b);return qr(d.h.put(c,void 0))})}
function xr(a,b,c,d,e,f,g){b=c-b;e?(e instanceof U&&(e.type==="QUOTA_EXCEEDED"||e.type==="QUOTA_MAYBE_EXCEEDED")&&Vq("QUOTA_EXCEEDED",{dbName:Xq(a.h.name),objectStoreNames:f,transactionCount:a.transactionCount,transactionMode:g.mode}),e instanceof U&&e.type==="UNKNOWN_ABORT"&&(c-=a.j,c<0&&c>=2147483648&&(c=0),Vq("TRANSACTION_UNEXPECTEDLY_ABORTED",{objectStoreNames:f,transactionDuration:b,transactionCount:a.transactionCount,dbDuration:c}),a.i=!0),Br(a,!1,d,f,b,g.tag),Uq(e)):Br(a,!0,d,f,b,g.tag)}
function Br(a,b,c,d,e,f="IDB_TRANSACTION_TAG_UNKNOWN"){Vq("TRANSACTION_ENDED",{objectStoreNames:d,connectionHasUnknownAbortedTransaction:a.i,duration:e,isSuccessful:b,tryCount:c,tag:f})}
var Cr=class{constructor(a,b){this.h=a;this.options=b;this.transactionCount=0;this.j=Math.round(V());this.i=!1}add(a,b,c){return ur(this,[a],{mode:"readwrite",na:!0,commit:tr()},d=>d.objectStore(a).add(b,c))}clear(a){return ur(this,[a],{mode:"readwrite",
na:!0},b=>b.objectStore(a).clear())}close(){this.h.close();
this.options?.closed&&this.options.closed()}count(a,b){return ur(this,[a],{mode:"readonly",na:!0,commit:tr()},c=>c.objectStore(a).count(b))}delete(a,b){return ur(this,[a],{mode:"readwrite",
na:!0,commit:tr()&&!(b instanceof IDBKeyRange)},c=>c.objectStore(a).delete(b))}get(a,b){return ur(this,[a],{mode:"readonly",
na:!0,commit:tr()},c=>c.objectStore(a).get(b))}objectStoreNames(){return Array.from(this.h.objectStoreNames)}getName(){return this.h.name}};
function Dr(a,b,c){a.h.createIndex(b,c,{unique:!1})}
function Er(a,b,c){a=a.h.openCursor(b.query,b.direction);return Fr(a).then(d=>rr(d,c))}
function Gr(a,b){return Er(a,{query:b},c=>c.delete().then(()=>Hr(c))).then(()=>{})}
var zr=class{constructor(a){this.h=a}add(a,b){return qr(this.h.add(a,b))}autoIncrement(){return this.h.autoIncrement}clear(){return qr(this.h.clear()).then(()=>{})}count(a){return qr(this.h.count(a))}delete(a){return a instanceof IDBKeyRange?Gr(this,a):qr(this.h.delete(a))}get(a){return qr(this.h.get(a))}index(a){try{return new Ir(this.h.index(a))}catch(b){if(b instanceof Error&&b.name==="NotFoundError")throw new dr(a,this.h.name);
throw b;}}getName(){return this.h.name}keyPath(){return this.h.keyPath}};function wr(a,b,c){const d=new Promise((e,f)=>{try{const g=b(a);c&&a.commit();g.then(h=>{e(h)}).catch(f)}catch(g){f(g),a.abort()}});
return Promise.all([d,a.done]).then(([e])=>e)}
var vr=class{constructor(a){this.h=a;this.i=new Map;this.aborted=!1;this.done=new Promise((b,c)=>{this.h.addEventListener("complete",()=>{b()});
this.h.addEventListener("error",d=>{d.currentTarget===d.target&&c(this.h.error)});
this.h.addEventListener("abort",()=>{var d=this.h.error;if(d)c(d);else if(!this.aborted){d=U;var e=this.h.objectStoreNames;const f=[];for(let g=0;g<e.length;g++){const h=e.item(g);if(h===null)throw Error("Invariant: item in DOMStringList is null");f.push(h)}d=new d("UNKNOWN_ABORT",{objectStoreNames:f.join(),dbName:this.h.db.name,mode:this.h.mode});c(d)}})})}abort(){this.h.abort();
this.aborted=!0;throw new U("EXPLICIT_ABORT");}commit(){this.aborted||this.h.commit?.()}objectStore(a){a=this.h.objectStore(a);let b=this.i.get(a);b||(b=new zr(a),this.i.set(a,b));return b}};function Jr(a,b,c){const {query:d=null,direction:e="next"}=b;a=a.h.openCursor(d,e);return Fr(a).then(f=>rr(f,c))}
var Ir=class{constructor(a){this.h=a}count(a){return qr(this.h.count(a))}delete(a){return Jr(this,{query:a},b=>b.delete().then(()=>Hr(b)))}get(a){return qr(this.h.get(a))}keyPath(){return this.h.keyPath}unique(){return this.h.unique}};
function Fr(a){return qr(a).then(b=>b?new Kr(a,b):null)}
function Hr(a){a.cursor.continue(void 0);return Fr(a.request)}
var Kr=class{constructor(a,b){this.request=a;this.cursor=b}delete(){return qr(this.cursor.delete()).then(()=>{})}getValue(){return this.cursor.value}update(a){return qr(this.cursor.update(a))}};function Lr(a,b,c){return new Promise((d,e)=>{let f;f=b!==void 0?self.indexedDB.open(a,b):self.indexedDB.open(a);const g=c.le,h=c.blocking,k=c.Ef,l=c.upgrade,n=c.closed;let m;const u=()=>{m||(m=new Cr(f.result,{closed:n}));return m};
f.addEventListener("upgradeneeded",p=>{try{if(p.newVersion===null)throw Error("Invariant: newVersion on IDbVersionChangeEvent is null");if(f.transaction===null)throw Error("Invariant: transaction on IDbOpenDbRequest is null");p.dataLoss&&p.dataLoss!=="none"&&Vq("IDB_DATA_CORRUPTED",{reason:p.dataLossMessage||"unknown reason",dbName:Xq(a)});const z=u(),D=new vr(f.transaction);l&&l(z,B=>p.oldVersion<B&&p.newVersion>=B,D);
D.done.catch(B=>{e(B)})}catch(z){e(z)}});
f.addEventListener("success",()=>{const p=f.result;h&&p.addEventListener("versionchange",()=>{h(u())});
p.addEventListener("close",()=>{Vq("IDB_UNEXPECTEDLY_CLOSED",{dbName:Xq(a),dbVersion:p.version});k&&k()});
d(u())});
f.addEventListener("error",()=>{e(f.error)});
g&&f.addEventListener("blocked",()=>{g()})})}
function Mr(a,b,c={}){return Lr(a,b,c)}
async function Nr(a,b={}){try{const c=self.indexedDB.deleteDatabase(a),d=b.le;d&&c.addEventListener("blocked",()=>{d()});
await pr(c)}catch(c){throw fr(c,a,"",-1);}}
;function Or(a,b){return new U("INCOMPATIBLE_DB_VERSION",{dbName:a.name,oldVersion:a.options.version,newVersion:b})}
function Pr(a,b){if(!b)throw gr("openWithToken",Xq(a.name));return a.open()}
var Qr=class{constructor(a,b){this.name=a;this.options=b;this.j=!0;this.u=this.o=0}i(a,b,c={}){return Mr(a,b,c)}delete(a={}){return Nr(this.name,a)}open(){if(!this.j)throw Or(this);if(this.h)return this.h;let a;const b=()=>{this.h===a&&(this.h=void 0)},c={blocking:e=>{e.close()},
closed:b,Ef:b,upgrade:this.options.upgrade},d=async()=>{var e=Error().stack??"";try{const h=await this.i(this.name,this.options.version,c);var f=h,g=this.options;const k=[];for(const l of Object.keys(g.Ib)){const {Pb:n,Bi:m=Number.MAX_VALUE}=g.Ib[l];!(f.h.version>=n)||f.h.version>=m||f.h.objectStoreNames.contains(l)||k.push(l)}if(k.length!==0){const l=Object.keys(this.options.Ib),n=h.objectStoreNames();if(this.u<I("ytidb_reopen_db_retries",0))return this.u++,h.close(),Uq(new U("DB_REOPENED_BY_MISSING_OBJECT_STORES",
{dbName:this.name,expectedObjectStores:l,foundObjectStores:n})),d();if(this.o<I("ytidb_remake_db_retries",1))return this.o++,await this.delete(),Uq(new U("DB_DELETED_BY_MISSING_OBJECT_STORES",{dbName:this.name,expectedObjectStores:l,foundObjectStores:n})),d();throw new cr(n,l);}return h}catch(h){if(h instanceof DOMException?h.name==="VersionError":"DOMError"in self&&h instanceof DOMError?h.name==="VersionError":h instanceof Object&&"message"in h&&h.message==="An attempt was made to open a database using a lower version than the existing version."){e=
await this.i(this.name,void 0,{...c,upgrade:void 0});f=e.h.version;if(this.options.version!==void 0&&f>this.options.version+1)throw e.close(),this.j=!1,Or(this,f);return e}b();h instanceof Error&&!S("ytidb_async_stack_killswitch")&&(h.stack=`${h.stack}\n${e.substring(e.indexOf("\n")+1)}`);throw fr(h,this.name,"",this.options.version??-1);}};
return this.h=a=d()}};const Rr=new Qr("YtIdbMeta",{Ib:{databases:{Pb:1}},upgrade(a,b){b(1)&&yr(a,"databases",{keyPath:"actualName"})}});async function Sr(a,b){return ur(await Pr(Rr,b),["databases"],{na:!0,mode:"readwrite"},c=>{const d=c.objectStore("databases");return d.get(a.actualName).then(e=>{if(e?a.actualName!==e.actualName||a.publicName!==e.publicName||a.userIdentifier!==e.userIdentifier:1)return qr(d.h.put(a,void 0)).then(()=>{})})})}
async function Tr(a,b){return a?(await Pr(Rr,b)).delete("databases",a):void 0}
async function Ur(a,b){const c=[];b=await Pr(Rr,b);await ur(b,["databases"],{na:!0,mode:"readonly"},d=>{c.length=0;return Er(d.objectStore("databases"),{},e=>{a(e.getValue())&&c.push(e.getValue());return Hr(e)})});
return c}
function Vr(a){return Ur(b=>b.publicName==="LogsDatabaseV2"&&b.userIdentifier!==void 0,a)}
function Wr(a,b,c){return Ur(d=>c?d.userIdentifier!==void 0&&!a.includes(d.userIdentifier)&&c.includes(d.publicName):d.userIdentifier!==void 0&&!a.includes(d.userIdentifier),b)}
async function Xr(a){const b=cq("YtIdbMeta hasAnyMeta other");return(await Ur(c=>c.userIdentifier!==void 0&&c.userIdentifier!==b,a)).length>0}
;let Yr;const Zr=new class{constructor(){}}(new class{constructor(){}});
async function $r(){if(Mq()?.hasSucceededOnce)return!0;var a;if(a=Yq)a=/WebKit\/([0-9]+)/.exec(zc()),a=!!(a&&parseInt(a[1],10)>=600);a&&(a=/WebKit\/([0-9]+)/.exec(zc()),a=!(a&&parseInt(a[1],10)>=602));if(!(a=a||Mc)){try{a=self;var b=!!(a.indexedDB&&a.IDBIndex&&a.IDBKeyRange&&a.IDBObjectStore)}catch(c){b=!1}a=!b}if(a||!("IDBTransaction"in self&&"objectStoreNames"in IDBTransaction.prototype))return!1;try{return await Sr({actualName:"yt-idb-test-do-not-use",publicName:"yt-idb-test-do-not-use",userIdentifier:void 0},
Zr),await Tr("yt-idb-test-do-not-use",Zr),!0}catch(c){return!1}}
function as(){if(Yr!==void 0)return Yr;Pq=!0;return Yr=$r().then(a=>{Pq=!1;if(Lq()?.i()){var b={hasSucceededOnce:Mq()?.hasSucceededOnce||a};Lq()?.set("LAST_RESULT_ENTRY_KEY",b,2592E3,!0)}return a})}
function bs(){return w("ytglobal.idbToken_")||void 0}
function cs(){const a=bs();return a?Promise.resolve(a):as().then(b=>{b?(v("ytglobal.idbToken_",Zr),b=Zr):b=void 0;return b})}
;let ds=0;function es(a,b){ds||(ds=Kl.va(async()=>{const c=await cs();if(c){var d=!0;try{const e=await Wr(a,c,b);if(e.length){const f=e[0];await Nr(f.actualName);await Tr(f.actualName,c)}else d=!1}catch(e){Uq(e),d=!1}Kl.wa(ds);ds=0;d&&es(a,b)}}))}
async function gs(){const a=await cs();return a?Xr(a):!1}
new lk;function hs(a){if(!bq())throw a=new U("AUTH_INVALID",{dbName:a}),Uq(a),a;const b=cq();return{actualName:`${a}:${b}`,publicName:a,userIdentifier:b}}
async function is(a,b,c,d){var e=Error().stack??"";const f=await cs();if(!f)throw b=gr("openDbImpl",a,b),S("ytidb_async_stack_killswitch")||(b.stack=`${b.stack}\n${e.substring(e.indexOf("\n")+1)}`),Uq(b),b;Wq(a);e=c?{actualName:a,publicName:a,userIdentifier:void 0}:hs(a);try{return await Sr(e,f),await Mr(e.actualName,b,d)}catch(g){try{await Tr(e.actualName,f)}catch{}throw g;}}
function js(a,b,c={}){return is(a,b,!1,c)}
function ks(a,b,c={}){return is(a,b,!0,c)}
async function ls(a,b={}){const c=await cs();c&&(Wq(a),a=hs(a),await Nr(a.actualName,b),await Tr(a.actualName,c))}
function ms(a,b,c){a=a.map(async d=>{await Nr(d.actualName,b);await Tr(d.actualName,c)});
return Promise.all(a).then(()=>{})}
async function ns(){var a={};const b=await cs();if(b){Wq("LogsDatabaseV2");var c=await Vr(b);await ms(c,a,b)}}
async function ps(a,b={}){const c=await cs();c&&(Wq(a),await Nr(a,b),await Tr(a,c))}
;function qs(a,b){let c;return()=>{c||(c=new rs(a,b));return c}}
var rs=class extends Qr{constructor(a,b){super(a,b);this.options=b;Wq(a)}i(a,b,c={}){return(this.options.shared?ks:js)(a,b,{...c})}delete(a={}){return(this.options.shared?ps:ls)(this.name,a)}};function ss(a,b){return qs(a,b)}
;var ts=ss("ytGcfConfig",{Ib:{coldConfigStore:{Pb:1},hotConfigStore:{Pb:1}},shared:!1,upgrade(a,b){b(1)&&(Dr(yr(a,"hotConfigStore",{keyPath:"key",autoIncrement:!0}),"hotTimestampIndex","timestamp"),Dr(yr(a,"coldConfigStore",{keyPath:"key",autoIncrement:!0}),"coldTimestampIndex","timestamp"))},version:1});function us(a){return Pr(ts(),a)}
async function vs(a,b,c){a={config:a,hashData:b,timestamp:V()};c=await us(c);await c.clear("hotConfigStore");return await Ar(c,"hotConfigStore",a)}
async function ws(a,b,c,d){a={config:a,hashData:b,configData:c,timestamp:V()};d=await us(d);await d.clear("coldConfigStore");return await Ar(d,"coldConfigStore",a)}
async function xs(a){a=await us(a);let b=void 0;await ur(a,["coldConfigStore"],{mode:"readwrite",na:!0},c=>Jr(c.objectStore("coldConfigStore").index("coldTimestampIndex"),{direction:"prev"},d=>{b=d.getValue()}));
return b}
async function ys(a){a=await us(a);let b=void 0;await ur(a,["hotConfigStore"],{mode:"readwrite",na:!0},c=>Jr(c.objectStore("hotConfigStore").index("hotTimestampIndex"),{direction:"prev"},d=>{b=d.getValue()}));
return b}
;var zs=class extends y{constructor(){super();this.i=[];this.h=[];const a=w("yt.gcf.config.hotUpdateCallbacks");a?(this.i=[...a],this.h=a):(this.h=[],v("yt.gcf.config.hotUpdateCallbacks",this.h))}ba(){for(const b of this.i){var a=this.h;const c=a.indexOf(b);c>=0&&a.splice(c,1)}this.i.length=0;super.ba()}};async function As(a,b,c){if(S("start_client_gcf")){c&&(a.j=c,v("yt.gcf.config.hotConfigGroup",a.j||null));a.o(b);const d=bs();d&&(c||(c=(await ys(d))?.config),await vs(c,b,d));if(c){a=a.i;for(const e of a.h)e(c)}}}
async function Bs(a,b,c){S("start_client_gcf")&&(a.coldHashData=b,v("yt.gcf.config.coldHashData",a.coldHashData||null),a=bs())&&(c||(c=(await xs(a))?.config),c&&await ws(c,b,c.configData,a))}
function Cs(){if(!Ds.instance){var a=new Ds;Ds.instance=a}a=Ds.instance;var b=V()-a.h;if(!(a.h!==0&&b<I("send_config_hash_timer"))){b=w("yt.gcf.config.coldConfigData");var c=w("yt.gcf.config.hotHashData"),d=w("yt.gcf.config.coldHashData");b&&c&&d&&(a.h=V());return{coldConfigData:b,hotHashData:c,coldHashData:d}}}
var Ds=class{constructor(){this.h=0;this.i=new zs}xc(){return w("yt.gcf.config.hotConfigGroup")??P("RAW_HOT_CONFIG_GROUP")}o(a){this.hotHashData=a;v("yt.gcf.config.hotHashData",this.hotHashData||null)}};function Es(){return"INNERTUBE_API_KEY"in zo&&"INNERTUBE_API_VERSION"in zo}
function Fs(){return{innertubeApiKey:P("INNERTUBE_API_KEY"),innertubeApiVersion:P("INNERTUBE_API_VERSION"),Te:P("INNERTUBE_CONTEXT_CLIENT_CONFIG_INFO"),wd:P("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),hi:P("INNERTUBE_CONTEXT_CLIENT_NAME",1),innertubeContextClientVersion:P("INNERTUBE_CONTEXT_CLIENT_VERSION"),Ve:P("INNERTUBE_CONTEXT_HL"),Ue:P("INNERTUBE_CONTEXT_GL"),We:P("INNERTUBE_HOST_OVERRIDE")||"",Xe:!!P("INNERTUBE_USE_THIRD_PARTY_AUTH",!1),ii:!!P("INNERTUBE_OMIT_API_KEY_WHEN_AUTH_HEADER_IS_PRESENT",
!1),appInstallData:P("SERIALIZED_CLIENT_CONFIG_DATA")}}
function Gs(a){const b={client:{hl:a.Ve,gl:a.Ue,clientName:a.wd,clientVersion:a.innertubeContextClientVersion,configInfo:a.Te}};navigator.userAgent&&(b.client.userAgent=String(navigator.userAgent));var c=t.devicePixelRatio;c&&c!=1&&(b.client.screenDensityFloat=String(c));c=P("EXPERIMENTS_TOKEN","");c!==""&&(b.client.experimentsToken=c);c=bp();c.length>0&&(b.request={internalExperimentFlags:c});c=a.wd;c!=="WEB"&&c!=="MWEB"&&c!==1&&c!==2||!b||(b.client.mainAppWebInfo=b.client.mainAppWebInfo??{},b.client.mainAppWebInfo.webDisplayMode=
Gp());(c=w("yt.embedded_player.embed_url"))&&b&&(b.thirdParty={embedUrl:c});S("web_log_memory_total_kbytes")&&t.navigator?.deviceMemory&&(c=t.navigator?.deviceMemory,b&&(b.client.memoryTotalKbytes=`${c*1E6}`));a.appInstallData&&b&&(b.client.configInfo=b.client.configInfo||{},b.client.configInfo.appInstallData=a.appInstallData);(a=$p())&&b&&(b.client.connectionType=a);S("web_log_effective_connection_type")&&(a=aq())&&b&&(b.client.effectiveConnectionType=a);if(S("start_client_gcf")){var d=Cs();d&&(a=
d.coldConfigData,c=d.coldHashData,d=d.hotHashData,b&&(b.client.configInfo=b.client.configInfo||{},a&&(b.client.configInfo.coldConfigData=a),c&&(b.client.configInfo.coldHashData=c),d&&(b.client.configInfo.hotHashData=d)))}P("DELEGATED_SESSION_ID")&&!S("pageid_as_header_web")&&(b.user={onBehalfOfUser:P("DELEGATED_SESSION_ID")});!S("fill_delegate_context_in_gel_killswitch")&&(a=P("INNERTUBE_CONTEXT_SERIALIZED_DELEGATION_CONTEXT"))&&(b.user={...b.user,serializedDelegationContext:a});a=P("INNERTUBE_CONTEXT");
S("enable_persistent_device_token")&&a?.client?.rolloutToken&&(b.client.rolloutToken=a?.client?.rolloutToken);a=Object;c=a.assign;d=b.client;var e=P("DEVICE","");const f={};for(const [g,h]of Object.entries(Mo(e))){e=g;const k=h;e==="cbrand"?f.deviceMake=k:e==="cmodel"?f.deviceModel=k:e==="cbr"?f.browserName=k:e==="cbrver"?f.browserVersion=k:e==="cos"?f.osName=k:e==="cosver"?f.osVersion=k:e==="cplatform"&&(f.platform=k)}b.client=c.call(a,d,f);return b}
function Hs(a,b,c={}){let d={};P("EOM_VISITOR_DATA")?d={"X-Goog-EOM-Visitor-Id":P("EOM_VISITOR_DATA")}:d={"X-Goog-Visitor-Id":c.visitorData||P("VISITOR_DATA","")};if(b&&b.includes("www.youtube-nocookie.com"))return d;b=c.authorization||P("AUTHORIZATION");b||(a?b=`Bearer ${w("gapi.auth.getToken")().Uh}`:(Jp.instance||(Jp.instance=new Jp),a=Ip(),S("pageid_as_header_web")||delete a["X-Goog-PageId"],d={...d,...a}));b&&(d.Authorization=b);return d}
;const Is=typeof TextEncoder!=="undefined"?new TextEncoder:null,Js=Is?a=>Is.encode(a):a=>{a=vc(a);
const b=new Uint8Array(a.length);for(let c=0;c<b.length;c++)b[c]=a[c];return b};var Ks={next:"wn_s",browse:"br_s",search:"sr_s",reel:"r_wrs",player:"ps_s"},Ls={next:"wn_r",browse:"br_r",search:"sr_r",reel:"r_wrr",player:"ps_r"};function Ms(a){this.version=1;this.args=a}
Ms.prototype.serialize=function(){return{version:this.version,args:this.args}};function Ns(a,b){this.topic=a;this.h=b}
Ns.prototype.toString=function(){return this.topic};const Os=w("ytPubsub2Pubsub2Instance")||new L;L.prototype.subscribe=L.prototype.subscribe;L.prototype.unsubscribeByKey=L.prototype.ec;L.prototype.publish=L.prototype.rb;L.prototype.clear=L.prototype.clear;v("ytPubsub2Pubsub2Instance",Os);const Ps=w("ytPubsub2Pubsub2SubscribedKeys")||{};v("ytPubsub2Pubsub2SubscribedKeys",Ps);const Qs=w("ytPubsub2Pubsub2TopicToKeys")||{};v("ytPubsub2Pubsub2TopicToKeys",Qs);const Rs=w("ytPubsub2Pubsub2IsAsync")||{};v("ytPubsub2Pubsub2IsAsync",Rs);
v("ytPubsub2Pubsub2SkipSubKey",null);function Ss(a,b){const c=Ts();c&&c.publish.call(c,a.toString(),a,b)}
function Us(a){var b=Vs;const c=Ts();if(!c)return 0;const d=c.subscribe(b.toString(),(e,f)=>{var g=w("ytPubsub2Pubsub2SkipSubKey");g&&g==d||(g=()=>{if(Ps[d])try{if(f&&b instanceof Ns&&b!=e)try{{var h=b.h,k=f;if(!k.args||!k.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");let l;try{if(!h.Sd){const n=new h;h.Sd=n.version}l=h.Sd}catch(n){}if(!l||k.version!=l)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");try{f=Reflect.construct(h,
nb(k.args))}catch(n){throw n.message="yt.pubsub2.Data.deserialize(): "+n.message,n;}}}catch(l){throw l.message="yt.pubsub2.pubsub2 cross-binary conversion error for "+b.toString()+": "+l.message,l;}a.call(window,f)}catch(l){Eo(l)}},Rs[b.toString()]?w("yt.scheduler.instance")?Kl.va(g):Xo(g,0):g())});
Ps[d]=!0;Qs[b.toString()]||(Qs[b.toString()]=[]);Qs[b.toString()].push(d);return d}
function Ws(){var a=Xs;const b=Us(function(c){a.apply(void 0,arguments);Ys(b)});
return b}
function Ys(a){const b=Ts();b&&(typeof a==="number"&&(a=[a]),hb(a,c=>{b.unsubscribeByKey(c);delete Ps[c]}))}
function Ts(){return w("ytPubsub2Pubsub2Instance")}
;function Zs(a,b,c={sampleRate:.1}){Math.random()<Math.min(.02,c.sampleRate/100)&&Ss("meta_logging_csi_event",{timerName:a,Ki:b})}
;const $s=I("max_body_size_to_compress",5E5),at=I("min_body_size_to_compress",500);let bt=0;
function ct(a,b,c,d){const e={startTime:V(),ticks:{},infos:{}};try{const g=dt(b);if(g==null||!(g>$s||g<at)){var f=Xn(Js(b));const h=V();e.ticks.gelc=h;bt++;S("gel_compression_csi_killswitch")||!S("log_gel_compression_latency")&&!S("log_gel_compression_latency_lr")||Zs("gel_compression",e,{sampleRate:.1});c.headers||(c.headers={});c.headers["Content-Encoding"]="gzip";c.postBody=f;c.postParams=void 0}d(a,c)}catch(g){Fo(g),d(a,c)}}
function et(a){V();if(!a.body)return a;try{const b=typeof a.body==="string"?a.body:JSON.stringify(a.body);let c=b;if(typeof b==="string"){const d=dt(b);if(d!=null&&(d>$s||d<at))return a;c=Xn(Js(b));V()}a.headers={"Content-Encoding":"gzip",...(a.headers||{})};a.body=c;return a}catch(b){return Fo(b),a}}
function dt(a){try{return(new Blob(a.split(""))).size}catch(b){return Fo(b),null}}
;function ft(a){a=Object.assign({},a);delete a.Authorization;const b=Wg();if(b){const c=new Sl;c.update(P("INNERTUBE_API_KEY"));c.update(b);a.hash=Vc(c.digest(),3)}return a}
;let gt;function ht(){gt||(gt=new Kq("yt.innertube"));return gt}
function jt(a,b,c,d){if(d)return null;d=ht().get("nextId",!0)||1;const e=ht().get("requests",!0)||{};e[d]={method:a,request:b,authState:ft(c),requestTime:Math.round(V())};ht().set("nextId",d+1,86400,!0);ht().set("requests",e,86400,!0);return d}
function kt(a){const b=ht().get("requests",!0)||{};delete b[a];ht().set("requests",b,86400,!0)}
function lt(a){const b=ht().get("requests",!0);if(b){for(const d in b){const e=b[d];if(!(Math.round(V())-e.requestTime<6E4)){var c=e.authState;const f=ft(Hs(!1));kh(c,f)&&(c=e.request,"requestTimeMs"in c&&(c.requestTimeMs=Math.round(V())),mt(a,e.method,c,{}));delete b[d]}}ht().set("requests",b,86400,!0)}}
;function nt(a){return!!a.aa||a.fc}
function ot(a){nt(a)&&!a.Ub&&(a.h=!0,a.oc&&Math.random()<=a.lc&&a.ia.qe(a.aa),pt(a),a.ha.ya()&&a.j(),a.ha.listen(a.cd,a.j.bind(a)),a.ha.listen(a.bd,a.o.bind(a)))}
function pt(a){if(!nt(a))throw Error("IndexedDB is not supported: retryQueuedRequests");a.ia.sd("QUEUED",a.aa).then(b=>{b&&!qt(a,b,a.Dd)?a.Ha.va(async()=>{b.id!==void 0&&await a.ia.dd(b.id,a.aa);pt(a)}):a.ha.ya()&&a.j()})}
async function rt(a,b){if(!nt(a))throw Error("IndexedDB is not supported: immediateSend");b.id!==void 0&&(await a.ia.cf(b.id,a.aa)||a.Ab(Error("The request cannot be found in the database.")));qt(a,b,a.Hd)?(b.skipRetry||(b=st(a,b)),b&&(b.skipRetry&&b.id!==void 0&&await a.ia.xb(b.id,a.aa),a.Va(b.url,b.options,!!b.skipRetry))):(a.Ab(Error("Networkless Logging: Stored logs request expired age limit")),b.id!==void 0&&await a.ia.xb(b.id,a.aa))}
function tt(a,b){a.Xd&&!a.ha.ya()?a.Xd(b):a.handleError(b)}
function qt(a,b,c){b=b.timestamp;return a.now()-b>=c?!1:!0}
function st(a,b){if(!nt(a))throw Error("IndexedDB is not supported: updateRequestHandlers");const c=b.options.onError?b.options.onError:()=>{};
b.options.onError=async(e,f)=>{const g=ut(f),h=vt(f);h&&a.da&&a.da("web_enable_error_204")&&a.handleError(Error("Request failed due to compression"),b.url,f);if(a.da&&a.da("nwl_consider_error_code")&&g||a.da&&!a.da("nwl_consider_error_code")&&a.potentialEsfErrorCounter<=a.Dc)if(a.ha.Hc&&await a.ha.Hc(),!a.ha.ya()){c(e,f);a.da&&a.da("nwl_consider_error_code")&&b?.id!==void 0&&await a.ia.dd(b.id,a.aa,!1);return}a.da&&a.da("nwl_consider_error_code")&&!g&&a.potentialEsfErrorCounter>a.Dc||(a.potentialEsfErrorCounter++,
b?.id!==void 0&&(b.sendCount<a.Jd?(await a.ia.dd(b.id,a.aa,!0,h?!1:void 0),a.Ha.va(()=>{a.ha.ya()&&a.j()},a.Id)):await a.ia.xb(b.id,a.aa)),c(e,f))};
const d=b.options.onSuccess?b.options.onSuccess:()=>{};
b.options.onSuccess=async(e,f)=>{b?.id!==void 0&&await a.ia.xb(b.id,a.aa);a.ha.lb&&a.da&&a.da("vss_network_hint")&&a.ha.lb(!0);d(e,f)};
return b}
var wt=class{constructor(a){this.fc=this.h=!1;this.potentialEsfErrorCounter=this.i=0;this.handleError=()=>{};
this.Ab=()=>{};
this.now=Date.now;this.Ub=!1;this.Nd=a.Nd??100;this.Jd=a.Jd??1;this.Hd=a.Hd??2592E6;this.Dd=a.Dd??12E4;this.Id=a.Id??5E3;this.aa=a.aa??void 0;this.oc=!!a.oc;this.lc=a.lc??.1;this.Dc=a.Dc??10;a.handleError&&(this.handleError=a.handleError);a.Ab&&(this.Ab=a.Ab);a.Ub&&(this.Ub=a.Ub);a.fc&&(this.fc=a.fc);this.da=a.da;this.Ha=a.Ha;this.ia=a.ia;this.ha=a.ha;this.Va=a.Va;this.cd=a.cd;this.bd=a.bd;nt(this)&&(!this.da||this.da("networkless_logging"))&&ot(this)}writeThenSend(a,b={}){if(nt(this)&&this.h){const c=
{url:a,options:b,timestamp:this.now(),status:"NEW",sendCount:0};this.ia.set(c,this.aa).then(d=>{c.id=d;this.ha.ya()&&rt(this,c)}).catch(d=>{rt(this,c);
tt(this,d)})}else this.Va(a,b)}sendThenWrite(a,b={},c){if(nt(this)&&this.h){const d={url:a,
options:b,timestamp:this.now(),status:"NEW",sendCount:0};this.da&&this.da("nwl_skip_retry")&&(d.skipRetry=c);if(this.ha.ya()||this.da&&this.da("nwl_aggressive_send_then_write")&&!d.skipRetry){if(!d.skipRetry){const e=b.onError?b.onError:()=>{};
b.onError=async(f,g)=>{await this.ia.set(d,this.aa).catch(h=>{tt(this,h)});
e(f,g)}}this.Va(a,b,d.skipRetry)}else this.ia.set(d,this.aa).catch(e=>{this.Va(a,b,d.skipRetry);
tt(this,e)})}else this.Va(a,b,this.da&&this.da("nwl_skip_retry")&&c)}sendAndWrite(a,b={}){if(nt(this)&&this.h){const c={url:a,
options:b,timestamp:this.now(),status:"NEW",sendCount:0};let d=!1;const e=b.onSuccess?b.onSuccess:()=>{};
c.options.onSuccess=(f,g)=>{c.id!==void 0?this.ia.xb(c.id,this.aa):d=!0;this.ha.lb&&this.da&&this.da("vss_network_hint")&&this.ha.lb(!0);e(f,g)};
this.Va(c.url,c.options,void 0,!0);this.ia.set(c,this.aa).then(f=>{c.id=f;d&&this.ia.xb(c.id,this.aa)}).catch(f=>{tt(this,f)})}else this.Va(a,b,void 0,!0)}j(){if(!nt(this))throw Error("IndexedDB is not supported: throttleSend");
this.i||(this.i=this.Ha.va(async()=>{const a=await this.ia.sd("NEW",this.aa);a?(await rt(this,a),this.i&&(this.i=0,this.j())):this.o()},this.Nd))}o(){this.Ha.wa(this.i);
this.i=0}};function ut(a){return(a=a?.error?.code)&&a>=400&&a<=599?!1:!0}
function vt(a){a=a?.error?.code;return!(a!==400&&a!==415)}
;let xt;
function zt(){if(xt)return xt();xt=ss("LogsDatabaseV2",{Ib:{LogsRequestsStore:{Pb:2}},shared:!1,upgrade(a,b,c){b(2)&&yr(a,"LogsRequestsStore",{keyPath:"id",autoIncrement:!0});b(3);b(5)&&(c=c.objectStore("LogsRequestsStore"),c.h.indexNames.contains("newRequest")&&c.h.deleteIndex("newRequest"),Dr(c,"newRequestV2",["status","interface","timestamp"]));b(7)&&a.h.objectStoreNames.contains("sapisid")&&a.h.deleteObjectStore("sapisid");b(9)&&a.h.objectStoreNames.contains("SWHealthLog")&&a.h.deleteObjectStore("SWHealthLog")},version:9});
return xt()}
;function At(a){return Pr(zt(),a)}
async function Bt(a,b){const c={startTime:V(),infos:{transactionType:"YT_IDB_TRANSACTION_TYPE_WRITE"},ticks:{}};b=await At(b);a={...a,options:JSON.parse(JSON.stringify(a.options)),interface:P("INNERTUBE_CONTEXT_CLIENT_NAME",0)};a=await Ar(b,"LogsRequestsStore",a);c.ticks.tc=V();Ct(c);return a}
async function Dt(a,b){const c={startTime:V(),infos:{transactionType:"YT_IDB_TRANSACTION_TYPE_READ"},ticks:{}};b=await At(b);var d=P("INNERTUBE_CONTEXT_CLIENT_NAME",0),e=[a,d,0];d=[a,d,V()];const f=IDBKeyRange.bound(e,d);let g="prev";S("use_fifo_for_networkless")&&(g="next");let h=void 0;e=a==="NEW"?"readwrite":"readonly";S("use_readonly_for_get_most_recent_by_status_killswitch")&&(e="readwrite");await ur(b,["LogsRequestsStore"],{mode:e,na:!0},k=>Jr(k.objectStore("LogsRequestsStore").index("newRequestV2"),
{query:f,direction:g},l=>{l.getValue()&&(h=l.getValue(),a==="NEW"&&(h.status="QUEUED",l.update(h)))}));
c.ticks.tc=V();Ct(c);return h}
async function Et(a,b){return ur(await At(b),["LogsRequestsStore"],{mode:"readwrite",na:!0},c=>{const d=c.objectStore("LogsRequestsStore");return d.get(a).then(e=>{if(e)return e.status="QUEUED",qr(d.h.put(e,void 0)).then(()=>e)})})}
async function Ft(a,b,c=!0,d){return ur(await At(b),["LogsRequestsStore"],{mode:"readwrite",na:!0},e=>{const f=e.objectStore("LogsRequestsStore");return f.get(a).then(g=>g?(g.status="NEW",c&&(g.sendCount+=1),d!==void 0&&(g.options.compress=d),qr(f.h.put(g,void 0)).then(()=>g)):lr.resolve(void 0))})}
async function Gt(a,b){return(await At(b)).delete("LogsRequestsStore",a)}
async function Ht(a){a=await At(a);const b=V()-2592E6;await ur(a,["LogsRequestsStore"],{mode:"readwrite",na:!0},c=>Er(c.objectStore("LogsRequestsStore"),{},d=>{if(d.getValue().timestamp<=b)return d.delete().then(()=>Hr(d))}))}
async function It(){await ns()}
function Ct(a){S("nwl_csi_killswitch")||Zs("networkless_performance",a,{sampleRate:1})}
;var Jt={accountStateChangeSignedIn:23,accountStateChangeSignedOut:24,delayedEventMetricCaptured:11,latencyActionBaselined:6,latencyActionInfo:7,latencyActionTicked:5,offlineTransferStatusChanged:2,offlineImageDownload:335,playbackStartStateChanged:9,systemHealthCaptured:3,mangoOnboardingCompleted:10,mangoPushNotificationReceived:230,mangoUnforkDbMigrationError:121,mangoUnforkDbMigrationSummary:122,mangoUnforkDbMigrationPreunforkDbVersionNumber:133,mangoUnforkDbMigrationPhoneMetadata:134,mangoUnforkDbMigrationPhoneStorage:135,
mangoUnforkDbMigrationStep:142,mangoAsyncApiMigrationEvent:223,mangoDownloadVideoResult:224,mangoHomepageVideoCount:279,mangoHomeV3State:295,mangoImageClientCacheHitEvent:273,sdCardStatusChanged:98,framesDropped:12,thumbnailHovered:13,deviceRetentionInfoCaptured:14,thumbnailLoaded:15,backToAppEvent:318,streamingStatsCaptured:17,offlineVideoShared:19,appCrashed:20,youThere:21,offlineStateSnapshot:22,mdxSessionStarted:25,mdxSessionConnected:26,mdxSessionDisconnected:27,bedrockResourceConsumptionSnapshot:28,
nextGenWatchWatchSwiped:29,kidsAccountsSnapshot:30,zeroStepChannelCreated:31,tvhtml5SearchCompleted:32,offlineSharePairing:34,offlineShareUnlock:35,mdxRouteDistributionSnapshot:36,bedrockRepetitiveActionTimed:37,unpluggedDegradationInfo:229,uploadMp4HeaderMoved:38,uploadVideoTranscoded:39,uploadProcessorStarted:46,uploadProcessorEnded:47,uploadProcessorReady:94,uploadProcessorRequirementPending:95,uploadProcessorInterrupted:96,uploadFrontendEvent:241,assetPackDownloadStarted:41,assetPackDownloaded:42,
assetPackApplied:43,assetPackDeleted:44,appInstallAttributionEvent:459,playbackSessionStopped:45,adBlockerMessagingShown:48,distributionChannelCaptured:49,dataPlanCpidRequested:51,detailedNetworkTypeCaptured:52,sendStateUpdated:53,receiveStateUpdated:54,sendDebugStateUpdated:55,receiveDebugStateUpdated:56,kidsErrored:57,mdxMsnSessionStatsFinished:58,appSettingsCaptured:59,mdxWebSocketServerHttpError:60,mdxWebSocketServer:61,startupCrashesDetected:62,coldStartInfo:435,offlinePlaybackStarted:63,liveChatMessageSent:225,
liveChatUserPresent:434,liveChatBeingModerated:457,liveCreationCameraUpdated:64,liveCreationEncodingCaptured:65,liveCreationError:66,liveCreationHealthUpdated:67,liveCreationVideoEffectsCaptured:68,liveCreationStageOccured:75,offlineSystemFailure:546,liveCreationBroadcastScheduled:123,liveCreationArchiveReplacement:149,liveCreationCostreamingConnection:421,liveCreationPlayablesMetrics:533,liveCreationStreamWebrtcStats:288,liveCreationWebrtcError:526,mdxSessionRecoveryStarted:69,mdxSessionRecoveryCompleted:70,
mdxSessionRecoveryStopped:71,visualElementShown:72,visualElementHidden:73,visualElementGestured:78,visualElementStateChanged:208,screenCreated:156,playbackAssociated:202,visualElementAttached:215,playbackContextEvent:214,cloudCastingPlaybackStarted:74,webPlayerApiCalled:76,tvhtml5AccountDialogOpened:79,foregroundHeartbeat:80,foregroundHeartbeatScreenAssociated:111,kidsOfflineSnapshot:81,mdxEncryptionSessionStatsFinished:82,playerRequestCompleted:83,liteSchedulerStatistics:84,mdxSignIn:85,spacecastMetadataLookupRequested:86,
spacecastBatchLookupRequested:87,spacecastSummaryRequested:88,spacecastPlayback:89,spacecastDiscovery:90,tvhtml5LaunchUrlComponentChanged:91,mdxBackgroundPlaybackRequestCompleted:92,mdxBrokenAdditionalDataDeviceDetected:93,tvhtml5LocalStorage:97,tvhtml5DeviceStorageStatus:147,autoCaptionsAvailable:99,playbackScrubbingEvent:339,flexyState:100,interfaceOrientationCaptured:101,mainAppBrowseFragmentCache:102,offlineCacheVerificationFailure:103,offlinePlaybackExceptionDigest:217,vrCopresenceStats:104,
vrCopresenceSyncStats:130,vrCopresenceCommsStats:137,vrCopresencePartyStats:153,vrCopresenceEmojiStats:213,vrCopresenceEvent:141,vrCopresenceFlowTransitEvent:160,vrCowatchPartyEvent:492,vrCowatchUserStartOrJoinEvent:504,vrPlaybackEvent:345,kidsAgeGateTracking:105,offlineDelayAllowedTracking:106,mainAppAutoOfflineState:107,videoAsThumbnailDownload:108,videoAsThumbnailPlayback:109,liteShowMore:110,renderingError:118,kidsProfilePinGateTracking:119,abrTrajectory:124,scrollEvent:125,streamzIncremented:126,
kidsProfileSwitcherTracking:127,kidsProfileCreationTracking:129,buyFlowStarted:136,mbsConnectionInitiated:138,mbsPlaybackInitiated:139,mbsLoadChildren:140,liteProfileFetcher:144,mdxRemoteTransaction:146,reelPlaybackError:148,reachabilityDetectionEvent:150,mobilePlaybackEvent:151,courtsidePlayerStateChanged:152,musicPersistentCacheChecked:154,musicPersistentCacheCleared:155,playbackInterrupted:157,playbackInterruptionResolved:158,fixFopFlow:159,anrDetection:161,backstagePostCreationFlowEnded:162,clientError:163,
gamingAccountLinkStatusChanged:164,liteHousewarming:165,buyFlowEvent:167,kidsParentalGateTracking:168,kidsSignedOutSettingsStatus:437,kidsSignedOutPauseHistoryFixStatus:438,tvhtml5WatchdogViolation:444,ypcUpgradeFlow:169,yongleStudy:170,ypcUpdateFlowStarted:171,ypcUpdateFlowCancelled:172,ypcUpdateFlowSucceeded:173,ypcUpdateFlowFailed:174,liteGrowthkitPromo:175,paymentFlowStarted:341,transactionFlowShowPaymentDialog:405,transactionFlowStarted:176,transactionFlowSecondaryDeviceStarted:222,transactionFlowSecondaryDeviceSignedOutStarted:383,
transactionFlowCancelled:177,transactionFlowPaymentCallBackReceived:387,transactionFlowPaymentSubmitted:460,transactionFlowPaymentSucceeded:329,transactionFlowSucceeded:178,transactionFlowFailed:179,transactionFlowPlayBillingConnectionStartEvent:428,transactionFlowSecondaryDeviceSuccess:458,transactionFlowErrorEvent:411,liteVideoQualityChanged:180,watchBreakEnablementSettingEvent:181,watchBreakFrequencySettingEvent:182,videoEffectsCameraPerformanceMetrics:183,adNotify:184,startupTelemetry:185,playbackOfflineFallbackUsed:186,
outOfMemory:187,ypcPauseFlowStarted:188,ypcPauseFlowCancelled:189,ypcPauseFlowSucceeded:190,ypcPauseFlowFailed:191,uploadFileSelected:192,ypcResumeFlowStarted:193,ypcResumeFlowCancelled:194,ypcResumeFlowSucceeded:195,ypcResumeFlowFailed:196,adsClientStateChange:197,ypcCancelFlowStarted:198,ypcCancelFlowCancelled:199,ypcCancelFlowSucceeded:200,ypcCancelFlowFailed:201,ypcCancelFlowGoToPaymentProcessor:402,ypcDeactivateFlowStarted:320,ypcRedeemFlowStarted:203,ypcRedeemFlowCancelled:204,ypcRedeemFlowSucceeded:205,
ypcRedeemFlowFailed:206,ypcFamilyCreateFlowStarted:258,ypcFamilyCreateFlowCancelled:259,ypcFamilyCreateFlowSucceeded:260,ypcFamilyCreateFlowFailed:261,ypcFamilyManageFlowStarted:262,ypcFamilyManageFlowCancelled:263,ypcFamilyManageFlowSucceeded:264,ypcFamilyManageFlowFailed:265,restoreContextEvent:207,embedsAdEvent:327,autoplayTriggered:209,clientDataErrorEvent:210,experimentalVssValidation:211,tvhtml5TriggeredEvent:212,tvhtml5FrameworksFieldTrialResult:216,tvhtml5FrameworksFieldTrialStart:220,musicOfflinePreferences:218,
watchTimeSegment:219,appWidthLayoutError:221,accountRegistryChange:226,userMentionAutoCompleteBoxEvent:227,downloadRecommendationEnablementSettingEvent:228,musicPlaybackContentModeChangeEvent:231,offlineDbOpenCompleted:232,kidsFlowEvent:233,kidsFlowCorpusSelectedEvent:234,videoEffectsEvent:235,unpluggedOpsEogAnalyticsEvent:236,playbackAudioRouteEvent:237,interactionLoggingDebugModeError:238,offlineYtbRefreshed:239,kidsFlowError:240,musicAutoplayOnLaunchAttempted:242,deviceContextActivityEvent:243,
deviceContextEvent:244,templateResolutionException:245,musicSideloadedPlaylistServiceCalled:246,embedsStorageAccessNotChecked:247,embedsHasStorageAccessResult:248,embedsItpPlayedOnReload:249,embedsRequestStorageAccessResult:250,embedsShouldRequestStorageAccessResult:251,embedsRequestStorageAccessState:256,embedsRequestStorageAccessFailedState:257,embedsItpWatchLaterResult:266,searchSuggestDecodingPayloadFailure:252,siriShortcutActivated:253,tvhtml5KeyboardPerformance:254,latencyActionSpan:255,elementsLog:267,
ytbFileOpened:268,tfliteModelError:269,apiTest:270,yongleUsbSetup:271,touStrikeInterstitialEvent:272,liteStreamToSave:274,appBundleClientEvent:275,ytbFileCreationFailed:276,adNotifyFailure:278,ytbTransferFailed:280,blockingRequestFailed:281,liteAccountSelector:282,liteAccountUiCallbacks:283,dummyPayload:284,browseResponseValidationEvent:285,entitiesError:286,musicIosBackgroundFetch:287,mdxNotificationEvent:289,layersValidationError:290,musicPwaInstalled:291,liteAccountCleanup:292,html5PlayerHealthEvent:293,
watchRestoreAttempt:294,liteAccountSignIn:296,notaireEvent:298,kidsVoiceSearchEvent:299,adNotifyFilled:300,delayedEventDropped:301,analyticsSearchEvent:302,systemDarkThemeOptOutEvent:303,flowEvent:304,networkConnectivityBaselineEvent:305,ytbFileImported:306,downloadStreamUrlExpired:307,directSignInEvent:308,lyricImpressionEvent:309,accessibilityStateEvent:310,tokenRefreshEvent:311,genericAttestationExecution:312,tvhtml5VideoSeek:313,unpluggedAutoPause:314,scrubbingEvent:315,bedtimeReminderEvent:317,
tvhtml5UnexpectedRestart:319,tvhtml5DeviceStorageStats:535,tvhtml5StabilityTraceEvent:478,tvhtml5OperationHealth:467,tvhtml5WatchKeyEvent:321,voiceLanguageChanged:322,tvhtml5LiveChatStatus:323,parentToolsCorpusSelectedEvent:324,offerAdsEnrollmentInitiated:325,networkQualityIntervalEvent:326,deviceStartupMetrics:328,heartbeatActionPlayerTransitioned:330,tvhtml5Lifecycle:331,heartbeatActionPlayerHalted:332,adaptiveInlineMutedSettingEvent:333,mainAppLibraryLoadingState:334,thirdPartyLogMonitoringEvent:336,
appShellAssetLoadReport:337,tvhtml5AndroidAttestation:338,tvhtml5StartupSoundEvent:340,iosBackgroundRefreshTask:342,iosBackgroundProcessingTask:343,sliEventBatch:344,postImpressionEvent:346,musicSideloadedPlaylistExport:347,idbUnexpectedlyClosed:348,voiceSearchEvent:349,mdxSessionCastEvent:350,idbQuotaExceeded:351,idbTransactionEnded:352,idbTransactionAborted:353,tvhtml5KeyboardLogging:354,idbIsSupportedCompleted:355,creatorStudioMobileEvent:356,idbDataCorrupted:357,parentToolsAppChosenEvent:358,
webViewBottomSheetResized:359,activeStateControllerScrollPerformanceSummary:360,navigatorValidation:361,mdxSessionHeartbeat:362,clientHintsPolyfillDiagnostics:363,clientHintsPolyfillEvent:364,proofOfOriginTokenError:365,kidsAddedAccountSummary:366,musicWearableDevice:367,ypcRefundFlowEvent:368,tvhtml5PlaybackMeasurementEvent:369,tvhtml5WatermarkMeasurementEvent:370,clientExpGcfPropagationEvent:371,mainAppReferrerIntent:372,leaderLockEnded:373,leaderLockAcquired:374,googleHatsEvent:375,persistentLensLaunchEvent:376,
parentToolsChildWelcomeChosenEvent:378,browseThumbnailPreloadEvent:379,finalPayload:380,mdxDialAdditionalDataUpdateEvent:381,webOrchestrationTaskLifecycleRecord:382,startupSignalEvent:384,accountError:385,gmsDeviceCheckEvent:386,accountSelectorEvent:388,accountUiCallbacks:389,mdxDialAdditionalDataProbeEvent:390,downloadsSearchIcingApiStats:391,downloadsSearchIndexUpdatedEvent:397,downloadsSearchIndexSnapshot:398,dataPushClientEvent:392,kidsCategorySelectedEvent:393,mdxDeviceManagementSnapshotEvent:394,
prefetchRequested:395,prefetchableCommandExecuted:396,gelDebuggingEvent:399,webLinkTtsPlayEnd:400,clipViewInvalid:401,persistentStorageStateChecked:403,cacheWipeoutEvent:404,playerEvent:410,sfvEffectPipelineStartedEvent:412,sfvEffectPipelinePausedEvent:429,sfvEffectPipelineEndedEvent:413,sfvEffectChosenEvent:414,sfvEffectLoadedEvent:415,sfvEffectUserInteractionEvent:465,sfvEffectFirstFrameProcessedLatencyEvent:416,sfvEffectAggregatedFramesProcessedLatencyEvent:417,sfvEffectAggregatedFramesDroppedEvent:418,
sfvEffectPipelineErrorEvent:430,sfvEffectGraphFrozenEvent:419,sfvEffectGlThreadBlockedEvent:420,mdeQosEvent:510,mdeVideoChangedEvent:442,mdePlayerPerformanceMetrics:472,mdeExporterEvent:497,genericClientExperimentEvent:423,homePreloadTaskScheduled:424,homePreloadTaskExecuted:425,homePreloadCacheHit:426,polymerPropertyChangedInObserver:427,applicationStarted:431,networkCronetRttBatch:432,networkCronetRttSummary:433,repeatChapterLoopEvent:436,seekCancellationEvent:462,lockModeTimeoutEvent:483,externalVideoShareToYoutubeAttempt:501,
parentCodeEvent:502,offlineTransferStarted:4,musicOfflineMixtapePreferencesChanged:16,mangoDailyNewVideosNotificationAttempt:40,mangoDailyNewVideosNotificationError:77,dtwsPlaybackStarted:112,dtwsTileFetchStarted:113,dtwsTileFetchCompleted:114,dtwsTileFetchStatusChanged:145,dtwsKeyframeDecoderBufferSent:115,dtwsTileUnderflowedOnNonkeyframe:116,dtwsBackfillFetchStatusChanged:143,dtwsBackfillUnderflowed:117,dtwsAdaptiveLevelChanged:128,blockingVisitorIdTimeout:277,liteSocial:18,mobileJsInvocation:297,
biscottiBasedDetection:439,coWatchStateChange:440,embedsVideoDataDidChange:441,shortsFirst:443,cruiseControlEvent:445,qoeClientLoggingContext:446,atvRecommendationJobExecuted:447,tvhtml5UserFeedback:448,producerProjectCreated:449,producerProjectOpened:450,producerProjectDeleted:451,producerProjectElementAdded:453,producerProjectElementRemoved:454,producerAppStateChange:509,producerProjectDiskInsufficientExportFailure:516,producerMediaServicesResetDetails:522,tvhtml5ShowClockEvent:455,deviceCapabilityCheckMetrics:456,
youtubeClearcutEvent:461,offlineBrowseFallbackEvent:463,getCtvTokenEvent:464,startupDroppedFramesSummary:466,screenshotEvent:468,miniAppPlayEvent:469,elementsDebugCounters:470,fontLoadEvent:471,webKillswitchReceived:473,webKillswitchExecuted:474,cameraOpenEvent:475,manualSmoothnessMeasurement:476,tvhtml5AppQualityEvent:477,polymerPropertyAccessEvent:479,miniAppSdkUsage:480,cobaltTelemetryEvent:481,crossDevicePlayback:482,channelCreatedWithObakeImage:484,channelEditedWithObakeImage:485,offlineDeleteEvent:486,
crossDeviceNotificationTransfer:487,androidIntentEvent:488,unpluggedAmbientInterludesCounterfactualEvent:489,keyPlaysPlayback:490,shortsCreationFallbackEvent:493,vssData:491,castMatch:494,miniAppPerformanceMetrics:495,userFeedbackEvent:496,kidsGuestSessionMismatch:498,musicSideloadedPlaylistMigrationEvent:499,sleepTimerSessionFinishEvent:500,watchEpPromoConflict:503,innertubeResponseCacheMetrics:505,miniAppAdEvent:506,dataPlanUpsellEvent:507,producerProjectRenamed:508,producerMediaSelectionEvent:511,
embedsAutoplayStatusChanged:512,remoteConnectEvent:513,connectedSessionMisattributionEvent:514,producerProjectElementModified:515,adsSeenClientLogging:517,producerEvent:518,tvhtml5CleanStart:519,deviceAccountMetricsEvent:520,derpLogEvent:521,playablesPortalEvent:523,ipValidationStarted:524,ipValidationReceived:525,reelsSequenceMutationEvent:527,watchZoomStateChange:528,metadataEditorEvent:529,kidsPrismaDeeplinksEvent:530,creationOrchestrationEvent:531,coordinatedSamplingTriggered:532,dnaRecapScreenshotEvent:534,
mdxLocalNetworkPermissionRequestEvent:536,mdxLocalNetworkPermissionResponseEvent:537,sessionReplayEvent:538,sessionReplayStatusEvent:539,loggingReliabilityProbe:540,keyValueStoreStatsEvent:541,deviceLocationPermissionEvent:542,remoteControlStarted:543,remoteControlCompleted:544,reelsAdsEvents:545,ytlrLoaderTestHarnessEvent:547};var Kt=ss("ServiceWorkerLogsDatabase",{Ib:{SWHealthLog:{Pb:1}},shared:!0,upgrade:(a,b)=>{b(1)&&Dr(yr(a,"SWHealthLog",{keyPath:"id",autoIncrement:!0}),"swHealthNewRequest",["interface","timestamp"])},
version:1});function Lt(a){return Pr(Kt(),a)}
async function Mt(a){a=await Lt(a);const b=V()-2592E6;await ur(a,["SWHealthLog"],{mode:"readwrite",na:!0},c=>Er(c.objectStore("SWHealthLog"),{},d=>{if(d.getValue().timestamp<=b)return d.delete().then(()=>Hr(d))}))}
async function Nt(a){await (await Lt(a)).clear("SWHealthLog")}
;const Ot={};let Pt=0;function Qt(a){const b=new Image,c=""+Pt++;Ot[c]=b;b.onload=b.onerror=()=>{delete Ot[c]};
({}).Fi&&(b.referrerPolicy="no-referrer");b.src=a}
;let Rt;function St(){Rt||(Rt=new Kq("yt.offline"));return Rt}
function Tt(a){if(S("offline_error_handling")){var b=St().get("errors",!0)||{};b[a.message]={name:a.name,stack:a.stack};a.level&&(b[a.message].level=a.level);St().set("errors",b,2592E3,!0)}}
;function Ut(){if(!Vt.instance){const a=w("yt.networkRequestMonitor.instance")||new Vt;v("yt.networkRequestMonitor.instance",a);Vt.instance=a}return Vt.instance}
var Vt=class{constructor(){this.h=new Map;this.i=!1}requestComplete(a,b){b&&(this.i=!0);a=this.removeParams(a);this.h.get(a)||this.h.set(a,b)}isEndpointCFR(a){a=this.removeParams(a);return(a=this.h.get(a))?!1:a===!1&&this.i?!0:null}removeParams(a){return a.split("?")[0]}};Vt.prototype.removeParams=Vt.prototype.removeParams;Vt.prototype.isEndpointCFR=Vt.prototype.isEndpointCFR;Vt.prototype.requestComplete=Vt.prototype.requestComplete;Vt.getInstance=Ut;function Wt(){if(!Xt.instance){const a=w("yt.networkStatusManager.instance")||new Xt;v("yt.networkStatusManager.instance",a);Xt.instance=a}return Xt.instance}
var Xt=class extends Oi{constructor(){super();this.j=!1;this.h=Jl();this.h.listen("networkstatus-online",()=>{if(this.j&&S("offline_error_handling")){var a=St().get("errors",!0);if(a){for(const b in a)if(a[b]){const c=new T(b,"sent via offline_errors");c.name=a[b].name;c.stack=a[b].stack;c.level=a[b].level;Eo(c)}St().set("errors",{},2592E3,!0)}}})}ya(){return this.h.ya()}lb(a){this.h.h=a}Qe(){const a=window.navigator.onLine;
return a===void 0?!0:a}Ae(){this.j=!0}listen(a,b){return this.h.listen(a,b)}Hc(a){return Ml(this.h,a)}};Xt.prototype.sendNetworkCheckRequest=Xt.prototype.Hc;Xt.prototype.listen=Xt.prototype.listen;Xt.prototype.enableErrorFlushing=Xt.prototype.Ae;Xt.prototype.getWindowStatus=Xt.prototype.Qe;Xt.prototype.networkStatusHint=Xt.prototype.lb;Xt.prototype.isNetworkAvailable=Xt.prototype.ya;Xt.getInstance=Wt;function Yt(a,b){a.rateLimit?a.h?(Kl.wa(a.u),a.u=Kl.va(()=>{a.o!==b&&(Pi(a,b),a.o=b,a.h=V())},a.rateLimit-(V()-a.h))):(Pi(a,b),a.o=b,a.h=V()):Pi(a,b)}
var Zt=class extends Oi{constructor(a={}){super();this.h=this.u=0;this.j=Wt();const b=w("yt.networkStatusManager.instance.listen").bind(this.j);b&&(a.rateLimit?(this.rateLimit=a.rateLimit,b("networkstatus-online",()=>{Yt(this,"publicytnetworkstatus-online")}),b("networkstatus-offline",()=>{Yt(this,"publicytnetworkstatus-offline")})):(b("networkstatus-online",()=>{Pi(this,"publicytnetworkstatus-online")}),b("networkstatus-offline",()=>{Pi(this,"publicytnetworkstatus-offline")})))}ya(){const a=w("yt.networkStatusManager.instance.isNetworkAvailable");
return a?a.bind(this.j)():!0}lb(a){const b=w("yt.networkStatusManager.instance.networkStatusHint").bind(this.j);b&&b(a)}async Hc(a){const b=w("yt.networkStatusManager.instance.sendNetworkCheckRequest").bind(this.j);return S("skip_network_check_if_cfr")&&Ut().isEndpointCFR("generate_204")?new Promise(c=>{this.lb(window.navigator?.onLine||!0);c(this.ya())}):b?b(a):!0}};let $t;function au(){let a=w("yt.networklessRequestController.instance");a||(a=new bu,v("yt.networklessRequestController.instance",a),S("networkless_logging")&&cs().then(b=>{a.aa=b;ot(a);a.u.resolve();a.oc&&Math.random()<=a.lc&&a.aa&&Mt(a.aa);S("networkless_immediately_drop_sw_health_store")&&cu(a)}));
return a}
async function cu(a){if(!a.aa)throw gr("clearSWHealthLogsDb");Nt(a.aa).catch(b=>{a.handleError(b)})}
var bu=class extends wt{constructor(){$t||($t=new Zt({mi:!0,bi:!0}));super({ia:{qe:Ht,xb:Gt,sd:Dt,cf:Et,dd:Ft,set:Bt},ha:$t,handleError:(a,b,c)=>{const d=c?.error?.code;d===400||d===415?(a=new T(a.message,b,c?.error?.code),Fo(a,void 0,void 0,void 0,!0)):Eo(a)},
Ab:Fo,Va:du,now:V,Xd:Tt,Ha:Iq(),cd:"publicytnetworkstatus-online",bd:"publicytnetworkstatus-offline",oc:!0,lc:.1,Dc:I("potential_esf_error_limit",10),da:S,Ub:!(bq()&&eu())});this.u=new lk;S("networkless_immediately_drop_all_requests")&&It();ps("LogsDatabaseV2")}writeThenSend(a,b){b||(b={});b=fu(a,b);bq()||(this.h=!1);super.writeThenSend(a,b)}sendThenWrite(a,b,c){b||(b={});b=fu(a,b);bq()||(this.h=!1);super.sendThenWrite(a,b,c)}sendAndWrite(a,b){b||(b={});b=fu(a,b);bq()||(this.h=!1);super.sendAndWrite(a,
b)}awaitInitialization(){return this.u.promise}};
function du(a,b,c){b=S("web_fp_via_jspb")?Object.assign({},b):b;S("use_request_time_ms_header")?b.headers&&Qo(a)&&(b.headers["X-Goog-Request-Time"]=JSON.stringify(Math.round(V()))):b.postParams?.requestTimeMs&&(b.postParams.requestTimeMs=Math.round(V()));if(c&&Object.keys(b).length===0){if(a)if(P("USE_NET_AJAX_FOR_PING_TRANSPORT",!1))fp(a,void 0,"GET","",void 0,void 0,!1,!1);else{b:{try{c:{var d=new za({url:a});if(d.h.dsh==="1")var e=null;else{var f=d.h.ae;if(f==="1"){const m=d.h.adurl;if(m)try{e=
{version:3,ye:decodeURIComponent(m),he:wa(d.i,"act=1","ri=1",ya(d))};break c}catch(u){}}e=f==="2"?{version:4,ye:wa(d.i,"dct=1","suid="+d.j,"ri=1"),he:wa(d.i,"act=1","ri=1","suid="+d.j)}:null}}if(e){const m=Ab(a);var g;if(!(g=!m||!m.endsWith("/aclk"))){{const u=a.search(Ib);let p=Hb(a,0,"ri",u);if(p<0)var h=null;else{var k=a.indexOf("&",p);if(k<0||k>u)k=u;h=vb(a.slice(p+3,k!==-1?k:0))}}g=h!=="1"}var l=!g;break b}}catch(m){}l=!1}if(l){b:{try{if(window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,
"")){var n=!0;break b}}catch(m){}n=!1}c=n?!0:!1}else c=!1;c||Qt(a)}}else b.compress?b.postBody?(typeof b.postBody!=="string"&&(b.postBody=JSON.stringify(b.postBody)),ct(a,b.postBody,b,jp)):ct(a,JSON.stringify(b.postParams),b,ip):jp(a,b)}
function fu(a,b){S("use_event_time_ms_header")&&Qo(a)&&(b.headers||(b.headers={}),b.headers["X-Goog-Event-Time"]=JSON.stringify(Math.round(V())));return b}
function eu(){return zb(document.location.toString())!=="www.youtube-nocookie.com"}
;let gu=!1;const hu=t.ytNetworklessLoggingInitializationOptions||{isNwlInitialized:gu};v("ytNetworklessLoggingInitializationOptions",hu);async function iu(){await cs()&&(bq()||S("nwl_init_require_datasync_id_killswitch"))&&eu()&&(gu=!0,hu.isNwlInitialized=gu,await au().awaitInitialization())}
;function mt(a,b,c,d){!P("VISITOR_DATA")&&b!=="visitor_id"&&Math.random()<.01&&Fo(new T("Missing VISITOR_DATA when sending innertube request.",b,c,d));if(!a.isReady()){var e=new T("innertube xhrclient not ready",b,c,d);Eo(e);throw e;}const f={headers:d.headers||{},method:"POST",postParams:c,postBody:d.postBody,postBodyFormat:d.postBodyFormat||"JSON",onTimeout:()=>{d.onTimeout()},
onFetchTimeout:d.onTimeout,onSuccess:(m,u)=>{if(d.onSuccess)d.onSuccess(u)},
onFetchSuccess:m=>{if(d.onSuccess)d.onSuccess(m)},
onProgress:m=>{if(d.onProgress)d.onProgress(m)},
onError:(m,u)=>{if(d.onError)d.onError(u)},
onFetchError:m=>{if(d.onError)d.onError(m)},
timeout:d.timeout,withCredentials:!0,compress:d.compress};f.headers["Content-Type"]||(f.headers["Content-Type"]="application/json");let g="";(e=a.config_.We)&&(g=e);const h=a.config_.Xe||!1,k=Hs(h,g,d);Object.assign(f.headers,k);f.headers.Authorization&&!g&&h&&(f.headers["x-origin"]=window.location.origin);const l=Oo(`${g}${`/${"youtubei"}/${a.config_.innertubeApiVersion}/${b}`}`,{alt:"json"}),n=(m=!1)=>{let u;if(d.retry&&g!="www.youtube-nocookie.com"&&(m||S("skip_ls_gel_retry")||f.headers["Content-Type"]!==
"application/json"||(u=jt(b,c,k,h)),u)){const p=f.onSuccess,z=f.onFetchSuccess;f.onSuccess=(D,B)=>{kt(u);p(D,B)};
c.onFetchSuccess=(D,B)=>{kt(u);z(D,B)}}try{if(m&&d.retry&&!d.networklessOptions.bypassNetworkless)f.method="POST",d.networklessOptions.writeThenSend?au().writeThenSend(l,f):au().sendAndWrite(l,f);
else if(d.compress)if(f.postBody){let p=f.postBody;typeof p!=="string"&&(p=JSON.stringify(f.postBody));ct(l,p,f,jp)}else ct(l,JSON.stringify(f.postParams),f,ip);else ip(l,f)}catch(p){if(p.name==="InvalidAccessError")u&&(kt(u),u=0),Fo(Error("An extension is blocking network request."));else throw p;}u&&dq(()=>{lt(a)},5E3)};
(w("ytNetworklessLoggingInitializationOptions")?hu.isNwlInitialized:gu)?as().then(m=>{n(m)}):n(!1)}
var ju=class{constructor(a){this.config_=null;a?this.config_=a:Es()&&(this.config_=Fs());dq(()=>{lt(this)},5E3)}isReady(){!this.config_&&Es()&&(this.config_=Fs());
return!!this.config_}};let ku=0;const lu=Oc?"webkit":Nc?"moz":Lc?"ms":Kc?"o":"";v("ytDomDomGetNextId",w("ytDomDomGetNextId")||(()=>++ku));const mu={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};function nu(a){if(document.body&&document.documentElement){const b=document.body.scrollTop+document.documentElement.scrollTop;a.h=a.clientX+(document.body.scrollLeft+document.documentElement.scrollLeft);a.i=a.clientY+b}}
class ou{constructor(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.metaKey=this.shiftKey=this.ctrlKey=this.altKey=!1;this.rotation=this.clientY=this.clientX=0;this.scale=1;this.changedTouches=this.touches=null;try{if(a=a||window.event){this.event=a;for(let d in a)d in mu||(this[d]=a[d]);this.scale=a.scale;this.rotation=a.rotation;var b=a.target||a.srcElement;b&&b.nodeType==3&&(b=b.parentNode);this.target=b;
var c=a.relatedTarget;if(c)try{c=c.nodeName?c:null}catch(d){c=null}else this.type=="mouseover"?c=a.fromElement:this.type=="mouseout"&&(c=a.toElement);this.relatedTarget=c;this.clientX=a.clientX!=void 0?a.clientX:a.pageX;this.clientY=a.clientY!=void 0?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||(this.type=="keypress"?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey;this.metaKey=a.metaKey;this.h=a.pageX;this.i=a.pageY}}catch(d){}}preventDefault(){this.event&&
(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())}stopPropagation(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())}stopImmediatePropagation(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())}};const gh=t.ytEventsEventsListeners||{};v("ytEventsEventsListeners",gh);const pu=t.ytEventsEventsCounter||{count:0};v("ytEventsEventsCounter",pu);
function qu(a,b,c,d={}){a.addEventListener&&(b!="mouseenter"||"onmouseenter"in document?b!="mouseleave"||"onmouseenter"in document?b=="mousewheel"&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return fh(e=>{const f=typeof e[4]==="boolean"&&e[4]==!!d,g=ma(e[4])&&ma(d)&&kh(e[4],d);return!!e.length&&e[0]==a&&e[1]==b&&e[2]==c&&(f||g)})}
function ru(a,b,c,d={}){if(!a||!a.addEventListener&&!a.attachEvent)return"";let e=qu(a,b,c,d);if(e)return e;e=++pu.count+"";const f=!(b!="mouseenter"&&b!="mouseleave"||!a.addEventListener||"onmouseenter"in document);let g;g=f?h=>{h=new ou(h);if(!vh(h.relatedTarget,k=>k==a))return h.currentTarget=a,h.type=b,c.call(a,h)}:h=>{h=new ou(h);
h.currentTarget=a;return c.call(a,h)};
g=R(g);a.addEventListener?(b=="mouseenter"&&f?b="mouseover":b=="mouseleave"&&f?b="mouseout":b=="mousewheel"&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),su()||typeof d==="boolean"?a.addEventListener(b,g,d):a.addEventListener(b,g,!!d.capture)):a.attachEvent(`on${b}`,g);gh[e]=[a,b,c,g,d];return e}
function tu(a){a&&(typeof a=="string"&&(a=[a]),hb(a,b=>{if(b in gh){var c=gh[b];const d=c[0],e=c[1],f=c[3];c=c[4];d.removeEventListener?su()||typeof c==="boolean"?d.removeEventListener(e,f,c):d.removeEventListener(e,f,!!c.capture):d.detachEvent&&d.detachEvent(`on${e}`,f);delete gh[b]}}))}
const su=dj(function(){let a=!1;try{const b=Object.defineProperty({},"capture",{get:function(){a=!0}});
window.addEventListener("test",null,b)}catch(b){}return a});function uu(a){this.F=a;this.h=null;this.o=0;this.A=null;this.u=0;this.i=[];for(a=0;a<4;a++)this.i.push(0);this.j=0;this.P=ru(window,"mousemove",ra(this.Y,this));a=ra(this.G,this);typeof a==="function"&&(a=R(a));this.Z=window.setInterval(a,25)}
va(uu,y);uu.prototype.Y=function(a){a.h===void 0&&nu(a);var b=a.h;a.i===void 0&&nu(a);this.h=new bh(b,a.i)};
uu.prototype.G=function(){if(this.h){var a=V();if(this.o!=0){var b=this.A,c=this.h,d=b.x-c.x;b=b.y-c.y;d=Math.sqrt(d*d+b*b)/(a-this.o);this.i[this.j]=Math.abs((d-this.u)/this.u)>.5?1:0;b=0;for(c=0;c<4;c++)b+=this.i[c]||0;b>=3&&this.F();this.u=d}this.o=a;this.A=this.h;this.j=(this.j+1)%4}};
uu.prototype.ba=function(){window.clearInterval(this.Z);tu(this.P)};const vu={};function wu({wi:a=!1,ci:b=!0}={}){if(w("_lact",window)==null){var c=parseInt(P("LACT"),10);c=isFinite(c)?Date.now()-Math.max(c,0):-1;v("_lact",c,window);v("_fact",c,window);c==-1&&xu();yu(a,b);new uu(()=>{zu("mouse",100)})}}
function yu(a=!1,b=!0){var c=window;ru(c.document,"keydown",xu);ru(c.document,"keyup",xu);ru(c.document,"mousedown",xu);ru(c.document,"mouseup",xu);a?ru(c,"touchmove",()=>{zu("touchmove",200)},{passive:!0}):(ru(c,"resize",()=>{zu("resize",200)}),b&&ru(c,"scroll",()=>{zu("scroll",200)}));
ru(c.document,"touchstart",xu,{passive:!0});ru(c.document,"touchend",xu,{passive:!0})}
function zu(a,b){vu[a]||(vu[a]=!0,Kl.va(()=>{xu();vu[a]=!1},b))}
function xu(){w("_lact",window)==null&&wu();var a=Date.now();v("_lact",a,window);w("_fact",window)==-1&&v("_fact",a,window);(a=w("ytglobal.ytUtilActivityCallback_"))&&a()}
function Au(){const a=w("_lact",window);return a==null?-1:Math.max(Date.now()-a,0)}
;const Bu=t.ytPubsubPubsubInstance||new L,Cu=t.ytPubsubPubsubSubscribedKeys||{},Du=t.ytPubsubPubsubTopicToKeys||{},Eu=t.ytPubsubPubsubIsSynchronous||{};function Fu(a,b){const c=Gu();if(c&&b){const d=c.subscribe(a,function(){const e=arguments,f=()=>{Cu[d]&&b.apply&&typeof b.apply=="function"&&b.apply(window,e)};
try{Eu[a]?f():Xo(f,0)}catch(g){Eo(g)}},void 0);
Cu[d]=!0;Du[a]||(Du[a]=[]);Du[a].push(d);return d}return 0}
function Hu(a){const b=Gu();b&&(typeof a==="number"?a=[a]:typeof a==="string"&&(a=[parseInt(a,10)]),hb(a,c=>{b.unsubscribeByKey(c);delete Cu[c]}))}
function Iu(a,b){const c=Gu();c&&c.publish.apply(c,arguments)}
function Ju(a){const b=Gu();if(b)if(b.clear(a),a)Ku(a);else for(let c in Du)Ku(c)}
function Gu(){return t.ytPubsubPubsubInstance}
function Ku(a){Du[a]&&(a=Du[a],hb(a,b=>{Cu[b]&&delete Cu[b]}),a.length=0)}
L.prototype.subscribe=L.prototype.subscribe;L.prototype.unsubscribeByKey=L.prototype.ec;L.prototype.publish=L.prototype.rb;L.prototype.clear=L.prototype.clear;v("ytPubsubPubsubInstance",Bu);v("ytPubsubPubsubTopicToKeys",Du);v("ytPubsubPubsubIsSynchronous",Eu);v("ytPubsubPubsubSubscribedKeys",Cu);var Lu=Symbol("injectionDeps"),Mu=class{constructor(a){this.name=a}toString(){return`InjectionToken(${this.name})`}},Nu=class{constructor(a){this.key=a}};function Ou(a,b){a.i.set(b.Zb,b);const c=a.j.get(b.Zb);if(c)try{c.Gc(a.resolve(b.Zb))}catch(d){c.Ai(d)}}
function Pu(a,b,c,d=!1){if(c.indexOf(b)>-1)throw Error(`Deps cycle for: ${b}`);if(a.h.has(b))return a.h.get(b);if(!a.i.has(b)){if(d)return;throw Error(`No provider for: ${b}`);}d=a.i.get(b);c.push(b);if(d.Qd!==void 0)var e=d.Qd;else if(d.Kf)e=d[Lu]?Qu(a,d[Lu],c):[],e=d.Kf(...e);else if(d.jd){e=d.jd;const f=e[Lu]?Qu(a,e[Lu],c):[];e=new e(...f)}else throw Error(`Could not resolve providers for: ${b}`);c.pop();d.Ii||a.h.set(b,e);return e}
function Qu(a,b,c){return b?b.map(d=>d instanceof Nu?Pu(a,d.key,c,!0):Pu(a,d,c)):[]}
var Ru=class{constructor(){this.i=new Map;this.j=new Map;this.h=new Map}resolve(a){return a instanceof Nu?Pu(this,a.key,[],!0):Pu(this,a,[])}};let Su;function Tu(){Su||(Su=new Ru);return Su}
;let Uu=window;function Vu(){return"h5vcc"in Uu&&Uu.h5vcc.traceEvent?.traceBegin&&Uu.h5vcc.traceEvent?.traceEnd?1:"performance"in Uu&&Uu.performance.mark&&Uu.performance.measure?2:0}
function Wu(a){const b=Vu();switch(b){case 1:Uu.h5vcc.traceEvent.traceBegin("YTLR",a);break;case 2:Uu.performance.mark(`${a}-start`);break;case 0:break;default:Ua(b,"unknown trace type")}}
function Xu(a){var b=Vu();switch(b){case 1:Uu.h5vcc.traceEvent.traceEnd("YTLR",a);break;case 2:b=`${a}-start`;const c=`${a}-end`;Uu.performance.mark(c);Uu.performance.measure(a,b,c);break;case 0:break;default:Ua(b,"unknown trace type")}}
;var Yu=S("web_enable_lifecycle_monitoring")&&Vu()!==0,Zu=S("web_enable_lifecycle_monitoring");function $u(a){var b=Array.from(a.h.keys()).sort((c,d)=>a.getPriority(a.h[d])-a.getPriority(a.h[c]));
for(const c of b)b=a.h[c],b.jobId===void 0||b.Ec||(a.scheduler.wa(b.jobId),a.scheduler.Xa(b.Tc,10))}
var av=class{constructor(a){this.scheduler=Iq();this.i=new lk;this.h=a;for(let c=0;c<this.h.length;c++){const d=this.h[c];a=()=>{d.Tc();this.h[c].Ec=!0;this.h.every(e=>e.Ec===!0)&&this.i.resolve()};
var b=this.getPriority(d);b=this.scheduler.Xa(a,b);this.h[c]={...d,Tc:a,jobId:b}}}cancel(){for(const a of this.h)a.jobId===void 0||a.Ec||this.scheduler.wa(a.jobId),a.Ec=!0;this.i.resolve()}getPriority(a){return a.priority??0}};function bv(a,b,c){Zu&&console.groupCollapsed&&console.groupEnd&&(console.groupCollapsed(`[${a.constructor.name}] '${a.state}' to '${b}'`),console.log("with message: ",c),console.groupEnd())}
function cv(a,b){const c=b.filter(e=>(a.i??e.priority??0)===10),d=b.filter(e=>(a.i??e.priority??0)!==10);
return a.A.Hi?async(...e)=>{await dv(c,...e);ev(a,d,...e)}:(...e)=>{fv(c,...e);
ev(a,d,...e)}}
async function dv(a,...b){const c=Iq();for(const d of a){let e;c.G(()=>{gv(d.name);const f=hv(()=>d.callback(...b));
Jd(f)?e=S("web_lifecycle_error_handling_killswitch")?f.then(()=>{iv(d.name)}):f.then(()=>{iv(d.name)},g=>{window.onerror?.(g.message,"",0,0,g);
iv(d.name)}):iv(d.name)});
e&&await e}}
function ev(a,b,...c){b=b.map(d=>({Tc:()=>{gv(d.name);hv(()=>d.callback(...c));
iv(d.name)},
priority:a.i??d.priority??0}));
b.length&&(a.o=new av(b))}
function fv(a,...b){const c=Iq();for(const d of a)c.G(()=>{gv(d.name);hv(()=>d.callback(...b));
iv(d.name)})}
function gv(a){Yu&&a&&Wu(a)}
function iv(a){Yu&&a&&Xu(a)}
var jv=class{constructor(a){this.state=a;this.plugins=[];this.i=void 0;this.A={};Yu&&Wu(this.state)}get currentState(){return this.state}install(a){this.plugins.push(a);return this}uninstall(...a){a.forEach(b=>{b=this.plugins.indexOf(b);b>-1&&this.plugins.splice(b,1)})}transition(a,b){Yu&&Xu(this.state);
var c=this.transitions.find(d=>Array.isArray(d.from)?d.from.find(e=>e===this.state&&d.to===a):d.from===this.state&&d.to===a);
if(c){this.o&&($u(this.o),this.o=void 0);bv(this,a,b);this.state=a;Yu&&Wu(this.state);c=c.action.bind(this);const d=this.plugins.filter(e=>e[a]).map(e=>e[a]);
c(cv(this,d),b)}else throw Error(`no transition specified from ${this.state} to ${a}`);}};function hv(a){if(S("web_lifecycle_error_handling_killswitch"))return a();try{return a()}catch(b){window.onerror?.(b.message,"",0,0,b)}}
;function kv(){lv||(lv=new mv);return lv}
var mv=class extends jv{constructor(){super("none");this.h=null;this.i=10;this.transitions=[{from:"none",to:"application_navigating",action:this.j},{from:"application_navigating",to:"none",action:this.u},{from:"application_navigating",to:"application_navigating",action:()=>{}},
{from:"none",to:"none",action:()=>{}}]}j(a,b){this.h=dq(()=>{this.currentState==="application_navigating"&&this.transition("none")},5E3);
a(b?.event)}u(a,b){this.h&&(Kl.wa(this.h),this.h=null);a(b?.event)}},lv;let nv=[];v("yt.logging.transport.getScrapedGelPayloads",function(){return nv});function ov(a,b){const c=pv(b);if(a.h[c])return a.h[c];const d=Object.keys(a.store)||[];if(d.length<=1&&pv(b)===d[0])return d;const e=[];for(let g=0;g<d.length;g++){const h=d[g].split("/");if(qv(b.auth,h[0])){var f=b.isJspb;qv(f===void 0?"undefined":f?"true":"false",h[1])&&qv(b.cttAuthInfo,h[2])&&(f=b.tier,f=f===void 0?"undefined":JSON.stringify(f),qv(f,h[3])&&e.push(d[g]))}}return a.h[c]=e}
function qv(a,b){return a===void 0||a==="undefined"?!0:a===b}
var rv=class{constructor(){this.store={};this.h={}}storePayload(a,b){a=pv(a);this.store[a]?this.store[a].push(b):(this.h={},this.store[a]=[b]);S("more_accurate_gel_parser")&&(b=new CustomEvent("TRANSPORTING_NEW_EVENT"),window.dispatchEvent(b));return a}smartExtractMatchingEntries(a){if(!a.keys.length)return[];const b=ov(this,a.keys.splice(0,1)[0]),c=[];for(let d=0;d<b.length;d++)this.store[b[d]]&&a.sizeLimit&&(this.store[b[d]].length<=a.sizeLimit?(c.push(...this.store[b[d]]),delete this.store[b[d]]):
c.push(...this.store[b[d]].splice(0,a.sizeLimit)));a?.sizeLimit&&c.length<a?.sizeLimit&&(a.sizeLimit-=c.length,c.push(...this.smartExtractMatchingEntries(a)));return c}extractMatchingEntries(a){a=ov(this,a);const b=[];for(let c=0;c<a.length;c++)this.store[a[c]]&&(b.push(...this.store[a[c]]),delete this.store[a[c]]);return b}getSequenceCount(a){a=ov(this,a);let b=0;for(let c=0;c<a.length;c++)b+=this.store[a[c]]?.length||0;return b}};rv.prototype.getSequenceCount=rv.prototype.getSequenceCount;
rv.prototype.extractMatchingEntries=rv.prototype.extractMatchingEntries;rv.prototype.smartExtractMatchingEntries=rv.prototype.smartExtractMatchingEntries;rv.prototype.storePayload=rv.prototype.storePayload;function pv(a){return[a.auth===void 0?"undefined":a.auth,a.isJspb===void 0?"undefined":a.isJspb,a.cttAuthInfo===void 0?"undefined":a.cttAuthInfo,a.tier===void 0?"undefined":a.tier].join("/")}
;function sv(a,b){if(a)return a[b.name]}
;var tv=new Mu("FinchConfigManagerService");const uv=I("initial_gel_batch_timeout",2E3),vv=I("gel_queue_timeout_max_ms",6E4),wv=I("gel_min_batch_size",5);let xv=void 0;class yv{constructor(){this.o=this.h=this.i=0;this.j=!1}}const zv=new yv,Av=new yv,Bv=new yv,Cv=new yv;let Dv,Ev=!0;const Fv=t.ytLoggingTransportTokensToCttTargetIds_||{};v("ytLoggingTransportTokensToCttTargetIds_",Fv);let Gv={};function Hv(){let a=w("yt.logging.ims");a||(a=new rv,v("yt.logging.ims",a));return a}
function Iv(a,b){if(a.endpoint==="log_event"){Jv(a);var c=Kv(a),d=Lv(a.payload)||"";a:{if(S("enable_web_tiered_gel")){var e=Jt[d||""];var f=Tu().resolve(new Nu(Ds))?.xc()?.loggingHotConfig?.eventLoggingConfig?.payloadPolicies;if(f)for(let g=0;g<f.length;g++)if(f[g].payloadNumber===e){e=f[g];break a}}e=void 0}f=200;if(e){if(e.enabled===!1&&!S("web_payload_policy_disabled_killswitch"))return;f=Mv(e.tier);if(f===400){Nv(a,b);return}}Gv[c]=!0;c={cttAuthInfo:c,isJspb:!1,tier:f};Hv().storePayload(c,a.payload);
Ov(b,c,d==="gelDebuggingEvent")}}
function Ov(a,b,c=!1){a&&(xv=new a);a=I("tvhtml5_logging_max_batch_ads_fork")||I("tvhtml5_logging_max_batch")||I("web_logging_max_batch")||100;const d=V(),e=Pv(!1,b.tier),f=e.o;c&&(e.j=!0);c=0;b&&(c=Hv().getSequenceCount(b));const g=()=>{Qv({writeThenSend:!0},void 0,!1,b.tier)};
c>=1E3?g():c>=a?Dv||(Dv=Rv(()=>{g();Dv=void 0},0)):d-f>=10&&(Sv(!1,b.tier),e.o=d)}
function Nv(a,b){if(a.endpoint==="log_event"){S("more_accurate_gel_parser")&&Hv().storePayload({isJspb:!1},a.payload);Jv(a);var c=Kv(a),d=new Map;d.set(c,[a.payload]);var e=Lv(a.payload)||"";b&&(xv=new b);return new ej((f,g)=>{xv&&xv.isReady()?Tv(d,xv,f,g,{bypassNetworkless:!0},!0,e==="gelDebuggingEvent"):f()})}}
function Kv(a){var b="";if(a.dangerousLogToVisitorSession)b="visitorOnlyApprovedKey";else if(a.cttAuthInfo){b=a.cttAuthInfo;const c={};b.videoId?c.videoId=b.videoId:b.playlistId&&(c.playlistId=b.playlistId);Fv[a.cttAuthInfo.token]=c;b=a.cttAuthInfo.token}return b}
function Qv(a={},b,c=!1,d){new ej((e,f)=>{const g=Pv(c,d),h=g.j;g.j=!1;Uv(g.i);Uv(g.h);g.h=0;xv&&xv.isReady()?d===void 0&&S("enable_web_tiered_gel")?Vv(e,f,a,b,c,300,h):Vv(e,f,a,b,c,d,h):(Sv(c,d),e())})}
function Vv(a,b,c={},d,e=!1,f=200,g=!1){var h=xv;const k=new Map,l={isJspb:e,cttAuthInfo:d,tier:f};e={isJspb:e,cttAuthInfo:d};if(d!==void 0)f=S("enable_web_tiered_gel")?Hv().smartExtractMatchingEntries({keys:[l,e],sizeLimit:1E3}):Hv().extractMatchingEntries(e),k.set(d,f);else for(const n of Object.keys(Gv))d=S("enable_web_tiered_gel")?Hv().smartExtractMatchingEntries({keys:[{isJspb:!1,cttAuthInfo:n,tier:f},{isJspb:!1,cttAuthInfo:n}],sizeLimit:1E3}):Hv().extractMatchingEntries({isJspb:!1,cttAuthInfo:n}),
d.length>0&&k.set(n,d),(S("web_fp_via_jspb_and_json")&&c.writeThenSend||!S("web_fp_via_jspb_and_json"))&&delete Gv[n];Tv(k,h,a,b,c,!1,g)}
function Sv(a=!1,b=200){const c=()=>{Qv({writeThenSend:!0},void 0,a,b)},d=Pv(a,b);
var e=d===Cv||d===Bv?5E3:vv;S("web_gel_timeout_cap")&&!d.h&&(e=Rv(()=>{c()},e),d.h=e);
Uv(d.i);e=P("LOGGING_BATCH_TIMEOUT",I("web_gel_debounce_ms",1E4));S("shorten_initial_gel_batch_timeout")&&Ev&&(e=uv);e=Rv(()=>{I("gel_min_batch_size")>0?Hv().getSequenceCount({cttAuthInfo:void 0,isJspb:a,tier:b})>=wv&&c():c()},e);
d.i=e}
function Tv(a,b,c,d,e={},f,g){const h=Math.round(V());let k=a.size;const l=Wv(g);for(const [n,m]of a){a=n;g=m;const u=mh({context:Gs(b.config_||Fs())});if(!la(g)&&!S("throw_err_when_logevent_malformed_killswitch")){d();break}u.events=g;(g=Fv[a])&&Xv(u,a,g);delete Fv[a];const p=a==="visitorOnlyApprovedKey";Yv(u,h,p);S("always_send_and_write")&&(e.writeThenSend=!1);const z=M=>{S("start_client_gcf")&&Kl.va(async()=>{await Zv(M)});
k--;k||c()};
let D=0;const B=()=>{D++;if(e.bypassNetworkless&&D===1)try{mt(b,l,u,$v({writeThenSend:!0},p,z,B,f)),Ev=!1}catch(M){Eo(M),d()}k--;k||c()};
try{mt(b,l,u,$v(e,p,z,B,f)),Ev=!1}catch(M){Eo(M),d()}}}
function $v(a,b,c,d,e){a={retry:!0,onSuccess:c,onError:d,networklessOptions:a,dangerousLogToVisitorSession:b,Wh:!!e,headers:{},postBodyFormat:"",postBody:"",compress:S("compress_gel")||S("compress_gel_lr")};aw()&&(a.headers["X-Goog-Request-Time"]=JSON.stringify(Math.round(V())));return a}
function Yv(a,b,c){aw()||(a.requestTimeMs=String(b));S("unsplit_gel_payloads_in_logs")&&(a.unsplitGelPayloadsInLogs=!0);!c&&(b=P("EVENT_ID"))&&((c=P("BATCH_CLIENT_COUNTER")||0)||(c=Math.floor(Math.random()*65535/2)),c++,c>65535&&(c=1),Ao("BATCH_CLIENT_COUNTER",c),a.serializedClientEventId={serializedEventId:b,clientCounter:String(c)})}
function Xv(a,b,c){let d;if(c.videoId)d="VIDEO";else if(c.playlistId)d="PLAYLIST";else return;a.credentialTransferTokenTargetId=c;a.context=a.context||{};a.context.user=a.context.user||{};a.context.user.credentialTransferTokens=[{token:b,scope:d}]}
function Jv(a){var b=ap("il_payload_scraping")==="enable_il_payload_scraping";if(!w("yt.logging.transport.enableScrapingForTest"))if(b)nv=[],v("yt.logging.transport.enableScrapingForTest",!0),v("yt.logging.transport.scrapedPayloadsForTesting",nv),v("yt.logging.transport.payloadToScrape","visualElementShown visualElementHidden visualElementAttached screenCreated visualElementGestured visualElementStateChanged".split(" ")),v("yt.logging.transport.getScrapedPayloadFromClientEventsFunction"),v("yt.logging.transport.scrapeClientEvent",
!0);else return;b=w("yt.logging.transport.scrapedPayloadsForTesting");const c=w("yt.logging.transport.payloadToScrape"),d=w("yt.logging.transport.scrapeClientEvent");if(c&&c.length>=1)for(let e=0;e<c.length;e++)a&&a.payload[c[e]]&&(d?b.push(a.payload):b.push((a?.payload)[c[e]]));v("yt.logging.transport.scrapedPayloadsForTesting",b)}
function aw(){return S("use_request_time_ms_header")||S("lr_use_request_time_ms_header")}
function Rv(a,b){return S("transport_use_scheduler")===!1?Xo(a,b):S("logging_avoid_blocking_during_navigation")||S("lr_logging_avoid_blocking_during_navigation")?dq(()=>{kv().currentState==="none"?a():kv().install({none:{callback:a}})},b):dq(a,b)}
function Uv(a){S("transport_use_scheduler")?Kl.wa(a):window.clearTimeout(a)}
async function Zv(a){a=a?.responseContext?.globalConfigGroup;var b=sv(a,co),c=a?.hotHashData;const d=sv(a,bo),e=a?.coldHashData,f=Tu().resolve(new Nu(Ds));f&&(c&&(b?await As(f,c,b):await As(f,c)),e&&(d?await Bs(f,e,d):await Bs(f,e)));b=a?.rawFinchStaticConfigGroup;(a=a?.finchStaticHashData)?(c=Tu().resolve(new Nu(tv)))?await c.xi({config:b||{},Xh:a||""}):(b||a)&&Fo(new T("FinchConfigManagerService is not present, but Finch config data is present.")):b&&Fo(new T("Finch config data is present, but hash is missing."))}
function Pv(a,b=200){return a?b===300?Cv:Av:b===300?Bv:zv}
function Lv(a){a=Object.keys(a);for(const b of a)if(Jt[b])return b}
function Mv(a){switch(a){case "DELAYED_EVENT_TIER_UNSPECIFIED":return 0;case "DELAYED_EVENT_TIER_DEFAULT":return 100;case "DELAYED_EVENT_TIER_DISPATCH_TO_EMPTY":return 200;case "DELAYED_EVENT_TIER_FAST":return 300;case "DELAYED_EVENT_TIER_IMMEDIATE":return 400;default:return 200}}
function Wv(a=!1){return a&&S("vss_through_gel_video_stats")?"video_stats":"log_event"}
;const bw=t.ytLoggingGelSequenceIdObj_||{};v("ytLoggingGelSequenceIdObj_",bw);
function cw(a,b,c,d={}){const e={},f=Math.round(d.timestamp||V());e.eventTimeMs=f<Number.MAX_SAFE_INTEGER?f:0;e[a]=b;a=Au();e.context={lastActivityMs:String(d.timestamp||!isFinite(a)?-1:a)};d.sequenceGroup&&!S("web_gel_sequence_info_killswitch")&&(a=e.context,b=d.sequenceGroup,bw[b]=b in bw?bw[b]+1:0,a.sequence={index:bw[b],groupKey:b},d.endOfSequence&&delete bw[d.sequenceGroup]);S("web_tag_automated_log_events")&&(e.context.automatedLogEventSource=d.automatedLogEventSource);(d.sendIsolatedPayload?
Nv:Iv)({endpoint:"log_event",payload:e,cttAuthInfo:d.cttAuthInfo,dangerousLogToVisitorSession:d.dangerousLogToVisitorSession},c)}
;function Sq(a,b,c={}){let d=ju;P("ytLoggingEventsDefaultDisabled",!1)&&ju===ju&&(d=null);cw(a,b,d,c)}
;var dw=new Set,ew=0,fw=0,gw=0,hw=[];const iw=[],jw=["PhantomJS","Googlebot","TO STOP THIS SECURITY SCAN go/scan"];function Rq(a){kw(a)}
function W(a){kw(a,"WARNING")}
function lw(a){a instanceof Error?kw(a):(a=ma(a)?JSON.stringify(a):String(a),a=new T(a),a.name="RejectedPromiseError",W(a))}
function kw(a,b="ERROR",c,d,e,f={},g=!1,h){f.name=c||P("INNERTUBE_CONTEXT_CLIENT_NAME",1);f.version=d||P("INNERTUBE_CONTEXT_CLIENT_VERSION");mw(a,f,b,g,h)}
function mw(a,b,c="ERROR",d=!1,e){if(a){a.hasOwnProperty("level")&&a.level&&(c=a.level);if(S("console_log_js_exceptions")||["test","dev","autopush","staging"].includes(P("SERVER_VERSION"))){var f=[];f.push(`Name: ${a.name}`);f.push(`Message: ${a.message}`);a.hasOwnProperty("params")&&f.push(`Error Params: ${JSON.stringify(a.params)}`);a.hasOwnProperty("args")&&f.push(`Error args: ${JSON.stringify(a.args)}`);f.push(`File name: ${a.fileName}`);f.push(`Stacktrace: ${a.stack}`);f=f.join("\n");window.console.log(f,
a)}if(!(ew>=5)){f=[];for(g of iw)try{g()&&f.push(g())}catch(B){}var g=f;g=[...hw,...g];var h=rb(a);f=h.message||"Unknown Error";const z=h.name||"UnknownError";var k=h.stack||a.i||"Not available";if(k.startsWith(`${z}: ${f}`)){var l=k.split("\n");l.shift();k=l.join("\n")}l=h.lineNumber||"Not available";h=h.fileName||"Not available";let D=0;if(a.hasOwnProperty("args")&&a.args&&a.args.length)for(var n=0;n<a.args.length&&!(D=Dp(a.args[n],`params.${n}`,b,D),D>=500);n++);else if(a.hasOwnProperty("params")&&
a.params){const B=a.params;if(typeof a.params==="object")for(n in B){if(!B[n])continue;const M=`params.${n}`,K=Fp(B[n]);b[M]=K;D+=M.length+K.length;if(D>500)break}else b.params=Fp(B)}if(g.length)for(n=0;n<g.length&&!(D=Dp(g[n],`params.context.${n}`,b,D),D>=500);n++);navigator.vendor&&!b.hasOwnProperty("vendor")&&(b["device.vendor"]=navigator.vendor);b={message:f,name:z,lineNumber:l,fileName:h,stack:k,params:b,sampleWeight:1};n=Number(a.columnNumber);isNaN(n)||(b.lineNumber=`${b.lineNumber}:${n}`);
if(a.level==="IGNORED")var m=0;else a:{a=wp();for(m of a.cb)if(b.message&&b.message.match(m.oi)){m=m.weight;break a}for(var u of a.Za)if(u.callback(b)){m=u.weight;break a}m=1}b.sampleWeight=m;m=b;for(var p of sp){if(!p.Cc[m.name])continue;u=p.Cc[m.name];for(const B of u){u=m.message.match(B.regexp);if(!u)continue;m.params["params.error.original"]=u[0];a=B.groups;b={};for(n=0;n<a.length;n++)b[a[n]]=u[n+1],m.params[`params.error.${a[n]}`]=u[n+1];m.message=p.Xc(b);break}}m.params||(m.params={});p=wp();
m.params["params.errorServiceSignature"]=`msg=${p.cb.length}&cb=${p.Za.length}`;m.params["params.serviceWorker"]="false";t.document&&t.document.querySelectorAll&&(m.params["params.fscripts"]=String(document.querySelectorAll("script:not([nonce])").length));(new qh(ph,"sample")).constructor!==qh&&(m.params["params.fconst"]="true");window.yterr&&typeof window.yterr==="function"&&window.yterr(m);m.sampleWeight===0||dw.has(m.message)||(d?nw(m,c):ow(m,c,e))}}}
function nw(a,b="ERROR"){pw(b,a);qw(a)}
function ow(a,b="ERROR",c){if(b==="ERROR"){Ap.rb("handleError",a);if(S("record_app_crashed_web")&&gw===0&&a.sampleWeight===1){gw++;const d={appCrashType:"APP_CRASH_TYPE_BREAKPAD"};S("report_client_error_with_app_crash_ks")||(d.systemHealth={crashData:{clientError:{logMessage:{message:a.message}}}});Sq("appCrashed",d)}fw++}else b==="WARNING"&&Ap.rb("handleWarning",a);S("kevlar_gel_error_routing")&&(c=rw(b,a,c))&&(Sq("clientError",c),(b==="ERROR"||S("errors_flush_gel_always_killswitch"))&&Qv(void 0,
void 0,!1));S("suppress_error_204_logging")||pw(b,a);qw(a)}
function qw(a){try{dw.add(a.message)}catch(b){}ew++}
function rw(a,b,c={}){a:{for(d of jw)if(Zq(d.toLowerCase())){var d=!0;break a}d=!1}if(!d){var e={stackTrace:b.stack};b.fileName&&(e.filename=b.fileName);d=b.lineNumber&&b.lineNumber.split?b.lineNumber.split(":"):[];d.length!==0&&(d.length!==1||isNaN(Number(d[0]))?d.length!==2||isNaN(Number(d[0]))||isNaN(Number(d[1]))||(e.lineNumber=Number(d[0]),e.columnNumber=Number(d[1])):e.lineNumber=Number(d[0]));d={level:"ERROR_LEVEL_UNKNOWN",message:b.message,errorClassName:b.name,sampleWeight:b.sampleWeight};
a==="ERROR"?d.level="ERROR_LEVEL_ERROR":a==="WARNING"&&(d.level="ERROR_LEVEL_WARNNING");a={isObfuscated:!0,browserStackInfo:e};c.pageUrl=window.location.href;c.kvPairs=[];P("FEXP_EXPERIMENTS")&&(c.experimentIds=P("FEXP_EXPERIMENTS"));e=P("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS");if(!Bo("web_disable_gel_stp_ecatcher_killswitch")&&e)for(const g of Object.keys(e))c.kvPairs.push({key:g,value:String(e[g])});if(b=b.params)for(var f of Object.keys(b))c.kvPairs.push({key:`client.${f}`,value:String(b[f])});
f=P("SERVER_NAME");b=P("SERVER_VERSION");f&&b&&(c.kvPairs.push({key:"server.name",value:f}),c.kvPairs.push({key:"server.version",value:b}));(f=P("PLAYER_CLIENT_VERSION"))&&c.kvPairs.push({key:"client.player.version",value:f});return{errorMetadata:c,stackTrace:a,logMessage:d}}}
function pw(a,b){const c=b.params||{};a={urlParams:{a:"logerror",t:"jserror",type:b.name,msg:b.message.substr(0,250),line:b.lineNumber,level:a,"client.name":c.name},postParams:{url:P("PAGE_NAME",window.location.href),file:b.fileName},method:"POST"};c.version&&(a["client.version"]=c.version);if(a.postParams){b.stack&&(a.postParams.stack=b.stack);for(const e of Object.keys(c))a.postParams[`client.${e}`]=c[e];if(b=P("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS"))for(var d of Object.keys(b))a.postParams[d]=
b[d];(d=P("LAVA_VERSION"))&&(a.postParams["lava.version"]=d);d=P("SERVER_NAME");b=P("SERVER_VERSION");d&&b&&(a.postParams["server.name"]=d,a.postParams["server.version"]=b);(d=P("PLAYER_CLIENT_VERSION"))&&(a.postParams["client.player.version"]=d)}jp(`${P("ECATCHER_REPORT_HOST","")}/error_204`,a)}
function sw(a,...b){a.args||(a.args=[]);Array.isArray(a.args)&&a.args.push(...b)}
;function tw(a){for(const b of a.register.values())b.Ed("ABORTED")}
class uw{constructor(){this.register=new Map}clear(){tw(this);this.register.clear()}}var vw=new uw;let ww=Date.now().toString();
function xw(){a:{if(window.crypto&&window.crypto.getRandomValues)try{var a=Array(16),b=new Uint8Array(16);window.crypto.getRandomValues(b);for(var c=0;c<a.length;c++)a[c]=b[c];var d=a;break a}catch(e){}d=Array(16);for(a=0;a<16;a++){b=Date.now();for(c=0;c<b%23;c++)d[a]=Math.random();d[a]=Math.floor(Math.random()*256)}if(ww)for(a=1,b=0;b<ww.length;b++)d[a%16]^=d[(a-1)%16]/4^ww.charCodeAt(b),a++}a=[];for(b=0;b<d.length;b++)a.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_".charAt(d[b]&63));
return a.join("")}
;var yw;let zw=t.ytLoggingDocDocumentNonce_;zw||(zw=xw(),v("ytLoggingDocDocumentNonce_",zw));yw=zw;var Aw=class{constructor(a){this.h=a}getAsJson(){const a={};this.h.trackingParams!==void 0?a.trackingParams=this.h.trackingParams:(a.veType=this.h.veType,this.h.veCounter!==void 0&&(a.veCounter=this.h.veCounter),this.h.elementIndex!==void 0&&(a.elementIndex=this.h.elementIndex));this.h.dataElement!==void 0&&(a.dataElement=this.h.dataElement.getAsJson());this.h.youtubeData!==void 0&&(a.youtubeData=this.h.youtubeData);this.h.isCounterfactual&&(a.isCounterfactual=!0);return a}getAsJspb(){const a=new fo;
this.h.trackingParams!==void 0?a.setTrackingParams(this.h.trackingParams):(this.h.veType!==void 0&&F(a,2,he(this.h.veType)),this.h.veCounter!==void 0&&F(a,6,he(this.h.veCounter)),this.h.elementIndex!==void 0&&F(a,3,he(this.h.elementIndex)),this.h.isCounterfactual&&F(a,5,de(!0)));if(this.h.dataElement!==void 0){var b=this.h.dataElement.getAsJspb();pf(a,fo,7,b)}this.h.youtubeData!==void 0&&pf(a,eo,8,this.h.jspbYoutubeData);return a}toString(){return JSON.stringify(this.getAsJson())}isClientVe(){return!this.h.trackingParams&&
!!this.h.veType}getLoggingDirectives(){return this.h.loggingDirectives}};function Bw(a=0){return P("client-screen-nonce-store",{})[a]}
function Cw(a,b=0){let c=P("client-screen-nonce-store");c||(c={},Ao("client-screen-nonce-store",c));c[b]=a}
function Dw(a=0){return a===0?"ROOT_VE_TYPE":`${"ROOT_VE_TYPE"}.${a}`}
function Ew(a=0){return P(Dw(a))}
v("yt_logging_screen.getRootVeType",Ew);function Fw(a=0){a=Ew(a);var b;a?b=new Aw({veType:a,youtubeData:void 0,jspbYoutubeData:void 0}):b=null;return b}
function Gw(){let a=P("csn-to-ctt-auth-info");a||(a={},Ao("csn-to-ctt-auth-info",a));return a}
function Hw(){return Object.values(P("client-screen-nonce-store",{})).filter(a=>a!==void 0)}
function Iw(a=0){a=Bw(a);if(!a&&!P("USE_CSN_FALLBACK",!0))return null;a||(a="UNDEFINED_CSN");return a?a:null}
v("yt_logging_screen.getCurrentCsn",Iw);function Jw(a,b,c){const d=Gw();(c=Iw(c))&&delete d[c];b&&(d[a]=b)}
function Kw(a){return Gw()[a]}
v("yt_logging_screen.getCttAuthInfo",Kw);v("yt_logging_screen.setCurrentScreen",function(a,b,c=0,d){if(a!==Bw(c)||b!==P(Dw(c)))if(Jw(a,d,c),Cw(a,c),Ao(Dw(c),b),b=()=>{setTimeout(()=>{a&&Sq("foregroundHeartbeatScreenAssociated",{clientDocumentNonce:yw,clientScreenNonce:a})},0)},"requestAnimationFrame"in window)try{window.requestAnimationFrame(b)}catch(e){b()}else b()});function Lw(){const a=lh(Mw);let b;return(new ej((c,d)=>{a.onSuccess=e=>{Vo(e)?c(new Nw(e)):d(new Ow(`Request failed, status=${Wo(e)}`,"net.badstatus",e))};
a.onError=e=>{d(new Ow("Unknown request error","net.unknown",e))};
a.onTimeout=e=>{d(new Ow("Request timed out","net.timeout",e))};
b=jp("//googleads.g.doubleclick.net/pagead/id",a)})).Jc(c=>{c instanceof nj&&b?.abort();
return jj(c)})}
var Ow=class extends Ca{constructor(a,b,c){super(`${a}, errorCode=${b}`);this.errorCode=b;this.xhr=c;this.name="PromiseAjaxError"}},Nw=class{constructor(a){this.xhr=a}};function Pw(a,b=null){a.B=2;a.h=b}
function Qw(a,b=null){a.B=1;a.h=b}
class Rw{constructor(){this.B=0;this.h=null}then(a,b,c){return this.B===1&&a?(a=a.call(c,this.h))&&typeof a.then==="function"?a:Sw(a):this.B===2&&b?(a=b.call(c,this.h))&&typeof a.then==="function"?a:Tw(a):this}getValue(){return this.h}isRejected(){return this.B==2}}Rw.prototype.$goog_Thenable=!0;function Tw(a=null){const b=new Rw;Pw(b,a);return b}
function Sw(a=null){const b=new Rw;Qw(b,a);return b}
;function Uw(a){const b=P("INNERTUBE_HOST_OVERRIDE");b&&(a=String(b)+String(Bb(a)));return a}
function Vw(a){const b={};S("json_condensed_response")&&(b.prettyPrint="false");return a=Po(a,b||{},!1)}
function Ww(a,b="POST"){a={method:b,mode:Qo(a)?"same-origin":"cors",credentials:Qo(a)?"same-origin":"include"};b={};const c={};for(const d of Object.keys(b))b[d]&&(c[d]=b[d]);Object.keys(c).length>0&&(a.headers=c);return a}
;function Xw(){return Ug()||(Qc||Rc)&&Zq("applewebkit")&&!Zq("version")&&(!Zq("safari")||Zq("gsa/"))||Pc&&Zq("version/")?!0:P("EOM_VISITOR_DATA")?!1:!0}
;function Yw(a){var b=a.docid||a.video_id||a.videoId||a.id;if(b)return b;b=a.raw_player_response;b||(a=a.player_response)&&(b=JSON.parse(a));return b&&b.videoDetails&&b.videoDetails.videoId||null}
;function Zw(a){var b="EMBEDDED_PLAYER_MODE_UNKNOWN";window.location.hostname.includes("youtubeeducation.com")&&(b="EMBEDDED_PLAYER_MODE_PFL");let c=a.raw_embedded_player_response;if(!c&&(a=a.embedded_player_response))try{c=JSON.parse(a)}catch(d){return b}if(c)a:for(const d in jo)if(jo[d]==c.embeddedPlayerMode){b=jo[d];break a}return b}
;class $w extends Ca{constructor(a){super(a.message||a.description||a.name);this.isMissing=a instanceof ax;this.isTimeout=a instanceof Ow&&a.errorCode=="net.timeout";this.isCanceled=a instanceof nj}}$w.prototype.name="BiscottiError";class ax extends Ca{constructor(){super("Biscotti ID is missing from server")}}ax.prototype.name="BiscottiMissingError";const Mw={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0};let bx=null;
function cx(){if(S("disable_biscotti_fetch_entirely_for_all_web_clients"))return Error("Biscotti id fetching has been disabled entirely.");if(!Xw())return Error("User has not consented - not fetching biscotti id.");const a=P("PLAYER_VARS",{});if(jh(a)=="1")return Error("Biscotti ID is not available in private embed mode");if(Zw(a)==="EMBEDDED_PLAYER_MODE_PFL")return Error("Biscotti id fetching has been disabled for pfl.")}
function vo(){const a=cx();if(a!==void 0)return jj(a);bx||(bx=Lw().then(dx).Jc(b=>ex(2,b)));
return bx}
function dx(a){a=a.xhr.responseText;if(a.lastIndexOf(")]}'",0)!=0)throw new ax;a=JSON.parse(a.substr(4));if((a.type||1)>1)throw new ax;a=a.id;wo(a);bx=Sw(a);fx(18E5,2);return a}
function ex(a,b){b=new $w(b);wo("");bx=Tw(b);a>0&&fx(12E4,a-1);throw b;}
function fx(a,b){Xo(function(){Lw().then(dx,c=>ex(b,c)).Jc(cj)},a)}
function gx(){try{const a=w("yt.ads.biscotti.getId_");return a?a():vo()}catch(a){return jj(a)}}
;function hx(a){a&&(a.dataset?a.dataset[ix()]="true":cb(a))}
function jx(a){return a?a.dataset?a.dataset[ix()]:a.getAttribute("data-loaded"):null}
const kx={};function ix(){return kx.loaded||(kx.loaded="loaded".replace(/\-([a-z])/g,(a,b)=>b.toUpperCase()))}
;class lx{constructor(a){a=a||{};const b={},c={};this.url=a.url||"";this.args=a.args||lh(b);this.assets=a.assets||{};this.attrs=a.attrs||lh(c);this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}clone(){const a=new lx;for(const b in this)if(this.hasOwnProperty(b)){const c=this[b];ka(c)=="object"?a[b]=lh(c):a[b]=c}return a}};var mx=["att/get"],nx=["share/get_share_panel"],ox=["share/get_web_player_share_panel"],px=["feedback"],qx=["notification/modify_channel_preference"],rx=["browse/edit_playlist"],sx=["subscription/subscribe"],tx=["subscription/unsubscribe"];const ux=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};v("yt.msgs_",ux);function vx(a){xo(ux,arguments)}
;function wx(a,b,c=null){xx(a,b,c)}
function yx(a){a=zx(a);const b=document.getElementById(a);b&&(Ju(a),b.parentNode.removeChild(b))}
function Ax(a,b){a&&b&&(a=`${na(b)}`,(a=Bx[a])&&Hu(a))}
function xx(a,b,c=null){const d=zx(typeof a==="string"?a:a.toString());let e=document.getElementById(d);var f=e&&jx(e);const g=e&&!f;f?b&&b():(b&&(f=Fu(d,b),b=`${na(b)}`,Bx[b]=f),g||(e=Cx(a,d,()=>{jx(e)||(hx(e),Iu(d),Xo(()=>{Ju(d)},0))},c)))}
function Cx(a,b,c,d=null){const e=sh("SCRIPT");e.id=b;e.onload=()=>{c&&setTimeout(c,0)};
e.onreadystatechange=()=>{switch(e.readyState){case "loaded":case "complete":e.onload()}};
d&&e.setAttribute("nonce",d);ab(e,typeof a==="string"?$n(a):a);a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(e,a.firstChild);return e}
function zx(a){const b=document.createElement("a");Ta(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return`js-${wb(a)}`}
const Bx={};function Dx(a){const b=Ex(a);let c=document.getElementById(b);const d=c&&jx(c);d||c&&!d||(c=Fx(a,b,()=>{if(!jx(c)){hx(c);Iu(b);const e=sa(Ju,b);Xo(e,0)}}))}
function Fx(a,b,c){const d=document.createElement("link");d.id=b;d.onload=()=>{c&&setTimeout(c,0)};
a=$n(a);fb(d,a);(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function Ex(a){const b=sh("A");Ta(b,new La(a));a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return`css-${wb(a)}`}
;function Gx(a,...b){if(!Hx(a)||b.some(c=>!Hx(c)))throw Error("Only objects may be merged.");
for(const c of b)Ix(a,c)}
function Ix(a,b){for(const c in b)if(Hx(b[c])){if(c in a&&!Hx(a[c]))throw Error("Cannot merge an object into a non-object.");c in a||(a[c]={});Ix(a[c],b[c])}else if(Jx(b[c])){if(c in a&&!Jx(a[c]))throw Error("Cannot merge an array into a non-array.");c in a||(a[c]=[]);Kx(a[c],b[c])}else a[c]=b[c];return a}
function Kx(a,b){for(const c of b)Hx(c)?a.push(Ix({},c)):Jx(c)?a.push(Kx([],c)):a.push(c);return a}
function Hx(a){return typeof a==="object"&&!Array.isArray(a)}
function Jx(a){return typeof a==="object"&&Array.isArray(a)}
;const Lx="absolute_experiments app conditional_experiments debugcss debugjs expflag forced_experiments pbj pbjreload sbb spf spfreload sr_bns_address sttick".split(" ");
function Mx(a,b){var c=P("VALID_SESSION_TEMPDATA_DOMAINS",[]),d=zb(window.location.href);d&&c.push(d);d=zb(a);if(gb(c,d)>=0||!d&&a.lastIndexOf("/",0)==0)if(c=document.createElement("a"),Ta(c,a),a=c.href)if(a=Bb(a),a=Cb(a))if(!b.csn&&(b.itct||b.ved)&&(b=Object.assign({csn:Iw()},b)),e){var e=parseInt(e,10);isFinite(e)&&e>0&&Nx(a,b,e)}else Nx(a,b)}
function Nx(a,b,c){a=Ox(a);b=b?Fb(b):"";c=c||5;Xw()&&Lp(a,b,c)}
function Ox(a){for(let b of Lx)a=Kb(a,b);return"ST-"+wb(a).toString(36)}
;Date.now();function Px(a){let b=0;for(let c=0;c<a.length;c++)b=b*31+a.charCodeAt(c),c<a.length-1&&(b%=0x800000000000);return b%1E5}
;class Qx extends Ms{constructor(a){super(arguments);this.csn=a}}const Vs=new Ns("screen-created",Qx),Rx=[];let Sx=0;const Tx=new Map,Ux=new Map,Vx=new Map;
function Wx(a,b,c,d,e=!1,f={}){Object.assign(f,Xx({cttAuthInfo:Kw(b)||void 0},b));for(const h of d){var g=h.getAsJson();(hh(g)||!g.trackingParams&&!g.veType)&&W(Error("Child VE logged with no data"));if(S("no_client_ve_attach_unless_shown")){const k=Yx(h,b);if(g.veType&&!Ux.has(k)&&!Vx.has(k)&&!e){if(!S("il_attach_cache_limit")||Tx.size<1E3){Tx.set(k,[a,b,c,h]);return}S("il_attach_cache_limit")&&Tx.size>1E3&&W(new T("IL Attach cache exceeded limit"))}g=Yx(c,b);Tx.has(g)?Zx(c,b):Vx.set(g,!0)}}d=d.filter(h=>
{h.csn!==b?(h.csn=b,h=!0):h=!1;return h});
c={csn:b,parentVe:c.getAsJson(),childVes:jb(d,h=>h.getAsJson())};
b==="UNDEFINED_CSN"?$x("visualElementAttached",f,c):a?cw("visualElementAttached",c,a,f):Sq("visualElementAttached",c,f)}
function $x(a,b,c){Rx.push({sf:a,payload:c,li:void 0,options:b});Sx||(Sx=Ws())}
function Xs(a){if(Rx){for(const b of Rx)b.payload&&(b.payload.csn=a.csn,Sq(b.sf,b.payload,b.options));Rx.length=0}Sx=0}
function Yx(a,b){return`${a.getAsJson().veType}${a.getAsJson().veCounter}${b}`}
function Zx(a,b){a=Yx(a,b);Tx.has(a)&&(b=Tx.get(a)||[],Wx(b[0],b[1],b[2],[b[3]],!0,{}),Tx.delete(a))}
function Xx(a,b){S("log_sequence_info_on_gel_web")&&(a.sequenceGroup=b);return a}
;class ay{flush(a=[],b=!1){if(S("enable_client_streamz_web"))for(const c of a)a=Ig(c),this.h&&pf(a,Eg,2,this.h),a={serializedIncrementBatch:Vc(a.j())},Sq("streamzIncremented",a,{sendIsolatedPayload:b})}}var yl=class extends ay{constructor(){super()}},by=class extends ay{constructor(a){super();var b=new Eg;var c=new Dg;c=uf(c,1,"botguard");a=uf(c,2,a);a=of(a,Dg);kf(b,1,Fg,a);a&&!yd(a)&&We(b.X);this.h=b}};let xl;const cy=new Map;function dy(){try{return!!self.localStorage}catch{return!1}}
;function ey(a){a=a.match(/(.*)::.*::.*/);if(a!==null)return a[1]}
function fy(a){if(dy()){var b=Object.keys(window.localStorage);for(const c of b)b=ey(c),b===void 0||a.includes(b)||self.localStorage.removeItem(c)}}
function gy(){if(!dy())return!1;const a=cq();var b=Object.keys(window.localStorage);for(const c of b)if(b=ey(c),b!==void 0&&b!==a)return!0;return!1}
;function hy(){let a=!1;try{a=!!window.sessionStorage.getItem("session_logininfo")}catch{a=!0}return(P("INNERTUBE_CLIENT_NAME")==="WEB"||P("INNERTUBE_CLIENT_NAME")==="WEB_CREATOR")&&a}
function iy(){try{window.sessionStorage.removeItem("stickiness_reload");window.sessionStorage.removeItem("session_logininfo");Ao("LOGIN_INFO","");window.sessionStorage.setItem("from_switch_account","1");var a;let c=jy;c||(c=document.querySelector("#persist_identity"));if(a=c){var b=a.src?(new URL(a.src)).origin:"*";a.contentWindow?.postMessage({action:"clear"},b)}}catch{}}
function ky(a){if(a)if(a.startsWith("https://accounts.google.com/AddSession"))iy();else if(a.startsWith("https://accounts.google.com/ServiceLogin"))iy();else{var b;if(b=a.startsWith("https://myaccount.google.com"))b=(a instanceof tm?a.clone():new tm(a)).h.endsWith("/youtubeoptions");b&&iy()}if(P("LOGGED_IN",!0)&&hy()){b=P("VALID_SESSION_TEMPDATA_DOMAINS",[]);var c=zb(window.location.href);c&&b.push(c);c=zb(a);gb(b,c)>=0||!c&&a.lastIndexOf("/",0)==0?(b=Bb(a),(b=Cb(b))?(b=Ox(b),b=(b=Mp(b)||null)?Mo(b):
{}):b=null):b=null;b==null&&(b={});c=b;var d=void 0;hy()?(d||(d=P("LOGIN_INFO")),d?(c.session_logininfo=d,c=!0):c=!1):c=!1;c&&Mx(a,b)}}
let jy=null;function ly(a,b={},c=!1){const d=P("EVENT_ID");d&&(b.ei||(b.ei=d));b&&Mx(a,b);if(c)return!1;ky(a);b=window;a=Gb(a,{});ky(a);a=Qa(a+"",Pa)||Ma;b=b.location;a=Sa(a);a!==void 0&&(b.href=a);return!0}
;function my(a){if(jh(P("PLAYER_VARS",{}))!="1"){a&&uo();try{gx().then(()=>{},()=>{}),Xo(my,18E5)}catch(b){Eo(b)}}}
;var ny=class{constructor(){this.h={}}contains(a){return Object.prototype.hasOwnProperty.call(this.h,a)}get(a){if(this.contains(a))return this.h[a]}set(a,b){this.h[a]=b}Vb(){return Object.keys(this.h)}remove(a){delete this.h[a]}};new class{constructor(){this.mappings=new ny}get(a){a:{var b=this.mappings.get(a.toString());switch(b.type){case "mapping":a=b.value;break a;case "factory":b=b.value();this.mappings.set(a.toString(),{type:"mapping",value:b});a=b;break a;default:a=Ua(b,void 0)}}return a}};const oy=new Map([["dark","USER_INTERFACE_THEME_DARK"],["light","USER_INTERFACE_THEME_LIGHT"]]);function py(){var a=window.location.href;if(S("kevlar_disable_theme_param"))return null;Ab(a);try{const b=No(a).theme;return oy.get(b)||null}catch(b){}return null}
;function qy(a){const b=new hk;if(a.interpreterJavascript){var c=Yn(a.interpreterJavascript);c=Za(c).toString();var d=new fk;uf(d,6,c);pf(b,fk,1,d,Dd)}else a.interpreterUrl&&(c=Zn(a.interpreterUrl),c=Ja(c).toString(),d=new gk,uf(d,4,c),pf(b,gk,2,d,Dd));a.interpreterHash&&jf(b,3,we(a.interpreterHash),Dd);a.program&&jf(b,4,we(a.program),Dd);a.globalName&&jf(b,5,we(a.globalName),Dd);a.clientExperimentsStateBlob&&jf(b,7,we(a.clientExperimentsStateBlob),Dd);return b}
function ry(a){const b={};a=a.split("&");for(const c of a)a=c.split("="),a.length===2&&(b[a[0]]=a[1]);return b}
function sy(a){return Number(a.t)||7200}
;async function ty(){var a=window;await Pb(uy());const b=a.bgevmc;if(!b)throw Error("BGE Controls not exposed");return{pause:()=>{b.p()},
resume:()=>{b.r()},
checkForRefresh:()=>b.cr()}}
function uy(){return S("bg_st_hr")?"havuokmhhs-0":`${"havuokmhhs"}-${Math.floor(globalThis.performance?.timeOrigin||0)}`}
function vy(a){window.bgens=a}
class wy{constructor(a){this.h=a}bindInnertubeChallengeFetcher(a){this.h.bicf(a)}registerChallengeFetchedCallback(a){this.h.bcr(a)}getLatestChallengeResponse(){return this.h.blc()}}function xy(){return new Promise(a=>{const b=window;b.ntpevasrs!==void 0?a(new wy(b.ntpevasrs)):(b.ntpqfbel===void 0&&(b.ntpqfbel=[]),b.ntpqfbel.push(c=>{a(new wy(c))}))})}
;const yy=[];var zy=function(a,...b){if(b.length===0)return Ia(a[0]);let c=a[0];for(let d=0;d<b.length;d++)c+=encodeURIComponent(b[d])+a[d+1];return Ia(c)}`https://static.doubleclick.net/instream/ad_status.js`;
let Ay=!1;function By(){if(Xw()){var a=P("PLAYER_VARS",{});if(jh(a)!="1"&&Zw(a)!=="EMBEDDED_PLAYER_MODE_PFL"){var b=()=>{Ay=!0;"google_ad_status"in window?Ao("DCLKSTAT",1):Ao("DCLKSTAT",2)};
try{const c=Wa(document);wx(zy,b,c)}catch(c){}yy.push(Kl.va(()=>{if(!(Ay||"google_ad_status"in window)){try{Ax(zy.toString(),b)}catch(c){}Ay=!0;Ao("DCLKSTAT",3)}},5E3))}}}
function Cy(){const a=Number(P("DCLKSTAT",0));return isNaN(a)?0:a}
;var X=class{constructor(a){this.h=a}};[new X("b.f_"),new X("j.s_"),new X("r.s_"),new X("e.h_"),new X("i.s_"),new X("s.t_"),new X("p.h_"),new X("s.i_"),new X("f.i_"),new X("a.b_"),new X("a.o_"),new X("g.o_"),new X("p.i_"),new X("p.m_"),new X("n.k_"),new X("i.f_"),new X("a.s_"),new X("m.c_"),new X("n.h_"),new X("o.p_"),new X("m.p_"),new X("o.a_"),new X("d.p_"),new X("e.i_")].reduce((a,b)=>{a[b.h]=b;return a},{});function Dy(a){return w("ytcsi."+(a||"")+"data_")||Ey(a)}
function Fy(){const a=Dy();a.info||(a.info={});return a.info}
function Gy(a){a=Dy(a);a.metadata||(a.metadata={});return a.metadata}
function Hy(a){a=Dy(a);a.tick||(a.tick={});return a.tick}
function Iy(a){a=Dy(a);if(a.gel){const b=a.gel;b.gelInfos||(b.gelInfos={});b.gelTicks||(b.gelTicks={})}else a.gel={gelTicks:{},gelInfos:{}};return a.gel}
function Jy(a){a=Iy(a);a.gelInfos||(a.gelInfos={});return a.gelInfos}
function Ky(){const a=Iy();a.preLoggedGelInfos||(a.preLoggedGelInfos=[]);return a.preLoggedGelInfos}
function Ly(a){let b=Dy(a).nonce;b||(b=xw(),Dy(a).nonce=b);return b}
function Ey(a){const b={tick:{},info:{}};v("ytcsi."+(a||"")+"data_",b);return b}
;const My=I("ytcsi_debug_max_size",100);function Ny(){let a=w("ytcsi.debug");a||(a=[],v("ytcsi.debug",a),v("ytcsi.reference",{}));return a}
function Oy(a){const b=Ny();b.push(a);S("limit_ytcsi_debug_array_size")&&b.length>My&&b.splice(0,b.length-My)}
function Py(a){a=a||"";const b=Qy();if(b[a])return b[a];const c={timerName:a,info:{},tick:{},span:{},jspbInfo:[]};Oy(c);return b[a]=c}
function Qy(){const a=w("ytcsi.reference");if(a)return a;Ny();return w("ytcsi.reference")}
;var Ry={auto_search:"LATENCY_ACTION_AUTO_SEARCH",ad_to_ad:"LATENCY_ACTION_AD_TO_AD",ad_to_video:"LATENCY_ACTION_AD_TO_VIDEO",app_startup:"LATENCY_ACTION_APP_STARTUP",browse:"LATENCY_ACTION_BROWSE",cast_splash:"LATENCY_ACTION_CAST_SPLASH",call_to_cast:"LATENCY_ACTION_CALL_TO_CAST",channel_activity:"LATENCY_ACTION_FAMILY_CENTER_CHANNEL_ACTIVITY",channels:"LATENCY_ACTION_CHANNELS",chips:"LATENCY_ACTION_CHIPS",commerce_transaction:"LATENCY_ACTION_COMMERCE_TRANSACTION",direct_playback:"LATENCY_ACTION_DIRECT_PLAYBACK",
editor:"LATENCY_ACTION_EDITOR",embed:"LATENCY_ACTION_EMBED",embed_no_video:"LATENCY_ACTION_EMBED_NO_VIDEO",entity_key_serialization_perf:"LATENCY_ACTION_ENTITY_KEY_SERIALIZATION_PERF",entity_key_deserialization_perf:"LATENCY_ACTION_ENTITY_KEY_DESERIALIZATION_PERF",explore:"LATENCY_ACTION_EXPLORE",favorites:"LATENCY_ACTION_FAVORITES",home:"LATENCY_ACTION_HOME",inboarding:"LATENCY_ACTION_INBOARDING",landing:"LATENCY_ACTION_LANDING",learning:"LATENCY_ACTION_LEARNING",learning_journey_browse:"LATENCY_ACTION_LEARNING_JOURNEY_BROWSE",
learning_journey_watch:"LATENCY_ACTION_LEARNING_JOURNEY_WATCH",library:"LATENCY_ACTION_LIBRARY",live:"LATENCY_ACTION_LIVE",live_pagination:"LATENCY_ACTION_LIVE_PAGINATION",management:"LATENCY_ACTION_MANAGEMENT",mini_app:"LATENCY_ACTION_MINI_APP_PLAY",notification_settings:"LATENCY_ACTION_FAMILY_CENTER_NOTIFICATION_SETTINGS",onboarding:"LATENCY_ACTION_ONBOARDING",parent_profile_settings:"LATENCY_ACTION_KIDS_PARENT_PROFILE_SETTINGS",parent_tools_collection:"LATENCY_ACTION_PARENT_TOOLS_COLLECTION",parent_tools_dashboard:"LATENCY_ACTION_PARENT_TOOLS_DASHBOARD",
player_att:"LATENCY_ACTION_PLAYER_ATTESTATION",prebuffer:"LATENCY_ACTION_PREBUFFER",prefetch:"LATENCY_ACTION_PREFETCH",profile_settings:"LATENCY_ACTION_KIDS_PROFILE_SETTINGS",profile_switcher:"LATENCY_ACTION_LOGIN",projects:"LATENCY_ACTION_PROJECTS",reel_watch:"LATENCY_ACTION_REEL_WATCH",results:"LATENCY_ACTION_RESULTS",red:"LATENCY_ACTION_PREMIUM_PAGE_GET_BROWSE",premium:"LATENCY_ACTION_PREMIUM_PAGE_GET_BROWSE",premium_lite_upsell:"LATENCY_ACTION_PREMIUM_LITE_UPSELL",privacy_policy:"LATENCY_ACTION_FAMILY_CENTER_PRIVACY_POLICY",
review:"LATENCY_ACTION_REVIEW",search_overview_answer:"LATENCY_ACTION_SEARCH_OVERVIEW_ANSWER",search_ui:"LATENCY_ACTION_SEARCH_UI",search_suggest:"LATENCY_ACTION_SUGGEST",search_zero_state:"LATENCY_ACTION_SEARCH_ZERO_STATE",secret_code:"LATENCY_ACTION_KIDS_SECRET_CODE",switchplan:"LATENCY_ACTION_UNPLUGGED_SWITCH_PLAN",seek:"LATENCY_ACTION_PLAYER_SEEK",settings:"LATENCY_ACTION_SETTINGS",store:"LATENCY_ACTION_STORE",supervision_dashboard:"LATENCY_ACTION_FAMILY_CENTER_SUPERVISION_DASHBOARD",bedtime_reminder_settings:"LATENCY_ACTION_FAMILY_CENTER_BEDTIME_REMINDER_SETTINGS",
break_reminder_settings:"LATENCY_ACTION_FAMILY_CENTER_BREAK_REMINDER_SETTINGS",supervision_settings_dashboard:"LATENCY_ACTION_FAMILY_CENTER_SUPERVISION_SETTINGS_DASHBOARD",time_management:"LATENCY_ACTION_FAMILY_CENTER_TIME_MANAGEMENT",update_profile:"LATENCY_ACTION_FAMILY_CENTER_UPDATE_PROFILE",viewing_permissions:"LATENCY_ACTION_FAMILY_CENTER_VIEWING_PERMISSIONS",shorts_settings:"LATENCY_ACTION_FAMILY_CENTER_SHORTS_SETTINGS",privacy_settings:"LATENCY_ACTION_FAMILY_CENTER_PRIVACY_SETTINGS",tenx:"LATENCY_ACTION_TENX",
video_preview:"LATENCY_ACTION_VIDEO_PREVIEW",video_to_ad:"LATENCY_ACTION_VIDEO_TO_AD",watch:"LATENCY_ACTION_WATCH",watch_it_again:"LATENCY_ACTION_KIDS_WATCH_IT_AGAIN","watch,watch7":"LATENCY_ACTION_WATCH","watch,watch7_html5":"LATENCY_ACTION_WATCH","watch,watch7ad":"LATENCY_ACTION_WATCH","watch,watch7ad_html5":"LATENCY_ACTION_WATCH",wn_comments:"LATENCY_ACTION_LOAD_COMMENTS",ww_rqs:"LATENCY_ACTION_WHO_IS_WATCHING",voice_assistant:"LATENCY_ACTION_VOICE_ASSISTANT",cast_load_by_entity_to_watch:"LATENCY_ACTION_CAST_LOAD_BY_ENTITY_TO_WATCH",
networkless_performance:"LATENCY_ACTION_NETWORKLESS_PERFORMANCE",gel_compression:"LATENCY_ACTION_GEL_COMPRESSION",gel_jspb_serialize:"LATENCY_ACTION_GEL_JSPB_SERIALIZE",attestation_challenge_fetch:"LATENCY_ACTION_ATTESTATION_CHALLENGE_FETCH"};function Sy(a){return Ry[a]||"LATENCY_ACTION_UNKNOWN"}
;var Ty=class extends Ms{constructor(a,b){super(arguments);this.timer=b}},Uy=new Ns("aft-recorded",Ty);v("ytLoggingGelSequenceIdObj_",t.ytLoggingGelSequenceIdObj_||{});const Vy=t.ytLoggingLatencyUsageStats_||{};v("ytLoggingLatencyUsageStats_",Vy);function Wy(){Xy.instance||(Xy.instance=new Xy);return Xy.instance}
function Yy(a,b){Vy[b]=Vy[b]||{count:0};var c=Vy[b];c.count++;c.time=V();a.h||(a.h=dq(()=>{const d=V();for(const e in Vy)Vy[e]&&d-Vy[e].time>6E4&&delete Vy[e];a&&(a.h=0)},5E3));
return c.count>5?(c.count===6&&Math.random()*1E5<1&&(c=new T("CSI data exceeded logging limit with key",b.split("_")),b.indexOf("plev")>=0||W(c)),!0):!1}
var Xy=class{constructor(){this.h=0}tick(a,b,c,d){Yy(this,`tick_${a}_${b}`)||Sq("latencyActionTicked",{tickName:a,clientActionNonce:b},{timestamp:c,cttAuthInfo:d})}info(a,b,c){const d=Object.keys(a).join("");Yy(this,`info_${d}_${b}`)||(a=Object.assign({},a),a.clientActionNonce=b,Sq("latencyActionInfo",a,{cttAuthInfo:c}))}jspbInfo(){}span(a,b,c){const d=Object.keys(a).join("");Yy(this,`span_${d}_${b}`)||(a.clientActionNonce=b,Sq("latencyActionSpan",a,{cttAuthInfo:c}))}};const Zy=window;class $y{constructor(){this.timing={};this.clearResourceTimings=()=>{};
this.webkitClearResourceTimings=()=>{};
this.mozClearResourceTimings=()=>{};
this.msClearResourceTimings=()=>{};
this.oClearResourceTimings=()=>{}}}
function az(){var a;S("csi_use_performance_navigation_timing")?(a=Y?.getEntriesByType?.("navigation")?.[0]?.toJSON?.())?(a.requestStart=bz(a.requestStart),a.responseEnd=bz(a.responseEnd),a.redirectStart=bz(a.redirectStart),a.redirectEnd=bz(a.redirectEnd),a.domainLookupEnd=bz(a.domainLookupEnd),a.connectStart=bz(a.connectStart),a.connectEnd=bz(a.connectEnd),a.responseStart=bz(a.responseStart),a.secureConnectionStart=bz(a.secureConnectionStart),a.domainLookupStart=bz(a.domainLookupStart),a.isPerformanceNavigationTiming=
!0):a=Y.timing:a=S("csi_performance_timing_to_object")?JSON.parse(JSON.stringify(Y.timing)):Y.timing;return a}
function bz(a){return Math.round(cz()+a)}
function cz(){return(S("csi_use_time_origin")||S("csi_use_time_origin_tvhtml5"))&&Y.timeOrigin?Math.floor(Y.timeOrigin):Y.timing.navigationStart}
var Y=Zy.performance||Zy.mozPerformance||Zy.msPerformance||Zy.webkitPerformance||new $y;let dz=!1,ez=!1;
var fz={'script[name="scheduler/scheduler"]':"sj",'script[name="player/base"]':"pj",'link[rel="preload"][name="player/embed"]':"pej",'link[rel="stylesheet"][name="www-player"]':"pc",'link[rel="stylesheet"][name="player/www-player"]':"pc",'script[name="desktop_polymer/desktop_polymer"]':"dpj",'link[rel="import"][name="desktop_polymer"]':"dph",'script[name="mobile-c3"]':"mcj",'link[rel="stylesheet"][name="mobile-c3"]':"mcc",'script[name="player-plasma-ias-phone/base"]':"mcppj",'script[name="player-plasma-ias-tablet/base"]':"mcptj",'link[rel="stylesheet"][name="mobile-polymer-player-ias"]':"mcpc",
'link[rel="stylesheet"][name="mobile-polymer-player-svg-ias"]':"mcpsc",'script[name="mobile_blazer_core_mod"]':"mbcj",'link[rel="stylesheet"][name="mobile_blazer_css"]':"mbc",'script[name="mobile_blazer_logged_in_users_mod"]':"mbliuj",'script[name="mobile_blazer_logged_out_users_mod"]':"mblouj",'script[name="mobile_blazer_noncore_mod"]':"mbnj","#player_css":"mbpc",'script[name="mobile_blazer_desktopplayer_mod"]':"mbpj",'link[rel="stylesheet"][name="mobile_blazer_tablet_css"]':"mbtc",'script[name="mobile_blazer_watch_mod"]':"mbwj",
'script[name="embed_client"]':"ecj",'link[rel="stylesheet"][name="embed-ui"]':"ecc"},gz=ra(Y.clearResourceTimings||Y.webkitClearResourceTimings||Y.mozClearResourceTimings||Y.msClearResourceTimings||Y.oClearResourceTimings||cj,Y);
function hz(){const a=Ky(),b=Jy();var c=void 0;for(var d=0;d<a.length;d++){const h=a[d];if(h.loadType){c=h.loadType;break}}if(Gy().loadType==="cold"&&(b.loadType==="cold"||c==="cold")){c=Hy();d=Iy();d=d.gelTicks?d.gelTicks:d.gelTicks={};for(var e in c)e in d||typeof c[e]==="number"&&Z(e,iz(e));var f={},g=!1;e=h=>{Gx(b,h);Gx(f,h);g=!0};
for(const h of a)e(h);g&&jz(f)}}
function kz(a,b){Z("_start",a,b)}
function jz(a,b){if(!S("web_csi_action_sampling_enabled")||!Dy(b).actionDisabled){var c=Py(b||"");Gx(c.info,a);a.loadType&&(c=a.loadType,Gy(b).loadType=c);Gx(Jy(b),a);c=Ly(b);b=Dy(b).cttAuthInfo;Wy().info(a,c,b)}}
function lz(){return(Tu().resolve(new Nu(Ds))?.xc()?.loggingHotConfig?.csiConfig?.debugTicks??[]).map(a=>Object.values(a)[0])}
function Z(a,b,c){if(!S("web_csi_action_sampling_enabled")||!Dy(c).actionDisabled){var d=Ly(c),e;if(e=S("web_csi_debug_sample_enabled")&&d){Tu().resolve(new Nu(Ds))?.xc()&&!ez&&(ez=!0,Z("gcfl",V(),c));e=Tu().resolve(new Nu(Ds))?.xc()?.loggingHotConfig?.csiConfig?.debugSampleWeight||0;var f;if(f=e!==0)b:{f=lz();if(f.length>0)for(let h=0;h<f.length;h++)if(a===f[h]){f=!0;break b}f=!1}f?(e=Px(d)%e!==0,Dy(c).debugTicksExcludedLogged||(f={},f.debugTicksExcluded=e,jz(f,c)),Dy(c).debugTicksExcludedLogged=
!0):e=!1}if(!e){if(a[0]!=="_"&&(e=a,f=b,Y.mark))if(e.startsWith("mark_")||(e="mark_"+e),c&&(e+=` (${c})`),f===void 0||S("web_csi_disable_alt_time_performance_mark"))Y.mark(e);else{f=S("csi_use_performance_navigation_timing")?f-Y.timeOrigin:f-(Y.timeOrigin||Y.timing.navigationStart);try{Y.mark(e,{startTime:f})}catch(h){}}e=Py(c||"");e.tick[a]=b||V();if(e.callback&&e.callback[a])for(var g of e.callback[a])g();g=Iy(c);g.gelTicks&&(g.gelTicks[a]=!0);e=Hy(c);g=b||V();e[a]=g;e=Dy(c).cttAuthInfo;a==="_start"?
(a=Wy(),Yy(a,`baseline_${d}`)||Sq("latencyActionBaselined",{clientActionNonce:d},{timestamp:b,cttAuthInfo:e})):Wy().tick(a,d,b,e);mz(c);return g}}}
function nz(){const a=Y.getEntriesByType?.("mark");a&&a.forEach(b=>{b.name.startsWith("mark_")&&Y.clearMarks?.(b.name)})}
function oz(){var a=document;if("visibilityState"in a)a=a.visibilityState;else{var b=lu+"VisibilityState";a=b in a?a[b]:void 0}switch(a){case "hidden":return 0;case "visible":return 1;case "prerender":return 2;case "unloaded":return 3;default:return-1}}
function pz(){var a=P("TIMING_INFO",{});const b={},c=(d,e,f)=>{e=e.match("_rid")?e.split("_rid")[0]:e;typeof f==="number"&&(f=JSON.stringify(f));d.requestIds?d.requestIds.push({endpoint:e,id:f}):d.requestIds=[{endpoint:e,id:f}]};
for(const [d,e]of Object.entries(a)){a=d;const f=e;switch(a){case "GetBrowse_rid":c(b,a,f);break;case "GetGuide_rid":c(b,a,f);break;case "GetHome_rid":c(b,a,f);break;case "GetPlayer_rid":c(b,a,f);break;case "GetSearch_rid":c(b,a,f);break;case "GetSettings_rid":c(b,a,f);break;case "GetTrending_rid":c(b,a,f);break;case "GetWatchNext_rid":c(b,a,f);break;case "yt_red":b.isRedSubscriber=!!f;break;case "yt_ad":b.isMonetized=!!f}}return b}
function qz(a,b){a=document.querySelector(a);if(!a)return!1;var c="";const d=a.nodeName;d==="SCRIPT"?(c=a.src,c||(c=a.getAttribute("data-timing-href"))&&(c=window.location.protocol+c)):d==="LINK"&&(c=a.href);Wa(document)&&a.setAttribute("nonce",Wa(document));return c?(a=Y.getEntriesByName(c))&&a[0]&&(a=a[0],c=cz(),Z("rsf_"+b,c+Math.round(a.fetchStart)),Z("rse_"+b,c+Math.round(a.responseEnd)),a.transferSize!==void 0&&a.transferSize===0)?!0:!1:!1}
function rz(){const a=window.location.protocol;var b=Y.getEntriesByType("resource");b=ib(b,c=>c.name.indexOf(`${a}//fonts.gstatic.com/s/`)===0);
(b=kb(b,(c,d)=>d.duration>c.duration?d:c))&&b.startTime>0&&b.responseEnd>0&&(Z("wffs",bz(b.startTime)),Z("wffe",bz(b.responseEnd)))}
function sz(a){var b=iz("aft",a);if(b)return b;b=P((a||"")+"TIMING_AFT_KEYS",["ol"]);const c=b.length;for(let d=0;d<c;d++){const e=iz(b[d],a);if(e)return e}return NaN}
function tz(a){v("ytglobal.timing"+(a||"")+"ready_",!0)}
function iz(a,b){if(a=Hy(b)[a])return typeof a==="number"?a:a[a.length-1]}
function mz(a){const b=iz("_start",a),c=sz(a),d=!dz;b&&c&&d&&(Ss(Uy,new Ty(Math.round(c-b),a)),dz=!0)}
function uz(){if(Y.getEntriesByType){var a=Y.getEntriesByType("paint");if(a=lb(a,c=>c.name==="first-paint"))return bz(a.startTime)}let b;
S("csi_use_performance_navigation_timing")?b=Y.getEntriesByType("first-paint")[0].startTime:b=Y.timing.ri;return b?Math.max(0,b):0}
;function vz(a,b){R(()=>{Py("").info.actionType=a;b&&Ao("TIMING_AFT_KEYS",b);Ao("TIMING_ACTION",a);var c=pz();Object.keys(c).length>0&&jz(c);c={isNavigation:!0,actionType:Sy(P("TIMING_ACTION"))};var d=P("PREVIOUS_ACTION");d&&(c.previousAction=Sy(d));if(d=P("CLIENT_PROTOCOL"))c.httpProtocol=d;if(d=P("CLIENT_TRANSPORT"))c.transportProtocol=d;(d=Iw())&&d!=="UNDEFINED_CSN"&&(c.clientScreenNonce=d);d=oz();if(d===1||d===-1)c.isVisible=!0;Gy();Fy();c.loadType="cold";d=Fy();var e=az();let f=cz();const g=P("CSI_START_TIMESTAMP_MILLIS",
0);g>0&&!S("embeds_web_enable_csi_start_override_killswitch")&&(f=g);f&&(Z("srt",e.responseStart),d.prerender!==1&&kz(f));d=uz();d>0&&Z("fpt",d);d=az();d.isPerformanceNavigationTiming&&jz({performanceNavigationTiming:!0},void 0);Z("nreqs",d.requestStart,void 0);Z("nress",d.responseStart,void 0);Z("nrese",d.responseEnd,void 0);d.redirectEnd-d.redirectStart>0&&(Z("nrs",d.redirectStart,void 0),Z("nre",d.redirectEnd,void 0));d.domainLookupEnd-d.domainLookupStart>0&&(Z("ndnss",d.domainLookupStart,void 0),
Z("ndnse",d.domainLookupEnd,void 0));d.connectEnd-d.connectStart>0&&(Z("ntcps",d.connectStart,void 0),Z("ntcpe",d.connectEnd,void 0));d.secureConnectionStart>=cz()&&d.connectEnd-d.secureConnectionStart>0&&(Z("nstcps",d.secureConnectionStart,void 0),Z("ntcpe",d.connectEnd,void 0));Y&&"getEntriesByType"in Y&&rz();d=[];if(document.querySelector&&Y&&Y.getEntriesByName)for(var h in fz)fz.hasOwnProperty(h)&&(e=fz[h],qz(h,e)&&d.push(e));if(d.length>0){c.resourceInfo=[];for(const k of d)c.resourceInfo.push({resourceCache:k})}jz(c);
hz();tz();h=P("TIMING_ACTION");w("ytglobal.timingready_")&&h&&wz()&&sz()&&mz()})()}
function xz(){var a={};R(()=>{yz();var b=a.sampleRate;if(!S("web_csi_action_sampling_enabled")||b===void 0||b<=1)b=!1;else{var c=Ly("attestation_challenge_fetch");b=Px(c)%b!==0}b&&(Dy("attestation_challenge_fetch").actionDisabled=!0);Py("attestation_challenge_fetch").info.actionType="attestation_challenge_fetch";a.cttAuthInfo&&(Dy("attestation_challenge_fetch").cttAuthInfo=a.cttAuthInfo);Ao("attestation_challenge_fetchTIMING_ACTION","attestation_challenge_fetch");R(kz)(a.startTime,"attestation_challenge_fetch");
b={actionType:Sy("attestation_challenge_fetch")};a.ni&&(b.previousAction=Sy(P("TIMING_ACTION")));(c=Iw())&&c!=="UNDEFINED_CSN"&&(b.clientScreenNonce=c);zz(b,"attestation_challenge_fetch");tz("attestation_challenge_fetch")})()}
function yz(){R(()=>{wz("attestation_challenge_fetch")&&Az("aa",void 0,"attestation_challenge_fetch");const a=Qy();a.attestation_challenge_fetch&&delete a.attestation_challenge_fetch;const b={timerName:"attestation_challenge_fetch",info:{},tick:{},span:{},jspbInfo:[]};Oy(b);a.attestation_challenge_fetch=b;Ey("attestation_challenge_fetch");gz();nz()})()}
function wz(a){return R(()=>Bz("_start",a))()}
function zz(a,b,c=!1){R(jz)(a,b,c)}
function Az(a,b,c){return R(Z)(a,b,c)}
function Bz(a,b){return R(()=>{const c=Hy(b);return a in c})()}
function Cz(a){if(!S("universal_csi_network_ticks"))return"";a=Ab(a)||"";const b=Object.keys(Ks);for(let c=0;c<b.length;c++){const d=b[c];if(a.includes(d))return d}return""}
function Dz(a){if(!S("universal_csi_network_ticks"))return()=>{};
const b=Ks[a];return b?(Ez(b),()=>{var c=S("universal_csi_network_ticks")?(c=Ls[a])?Ez(c):!1:!1;return c}):()=>{}}
function Ez(a){return R(()=>{if(Bz(a))return!1;Az(a,void 0,void 0);return!0})()}
function Fz(a){R(()=>{if(!wz("attestation_challenge_fetch")||Bz(a,"attestation_challenge_fetch"))return!1;Az(a,void 0,"attestation_challenge_fetch");return!0})()}
function Gz(){R(()=>{const a=Ly();requestAnimationFrame(()=>{setTimeout(()=>{a===Ly()&&Az("ol",void 0,void 0)},0)})})()}
const Hz=window;Hz.ytcsi&&(Hz.ytcsi.infoGel=zz,Hz.ytcsi.tick=Az);function Iz(a,b){a.h=b}
async function Jz(a){let b;if(t.ytAtP&&!S("ytatp_ks")){var c=await t.ytAtP;delete t.ytAtP;let e=c?.R;b=c?.T;e?a.i.h(1,a.j++):(a.i.h(2,a.j++),c=await a.yb(Kz(b,null)),e=JSON.stringify(c));t.ytAtRC?t.ytAtRC(e):W(Error("ytAtRC not defined for ytAtP."))}else t.ytAtRC?Kl.Xa(async()=>{b=t.ytAtT;delete t.ytAtT;if(t.ytAtRC){a.i.h(2,a.j++);var e=await a.yb(Kz(b,null));t.ytAtRC&&t.ytAtRC(JSON.stringify(e))}else a.i.h(6,a.j++)},2,I("att_init_delay",0)):(b=t.ytAtT,delete t.ytAtT,a.i.h(1,a.j++));
c=await xy();c.bindInnertubeChallengeFetcher(e=>{a.i.h(3,a.j++);return a.yb(Kz(b,e))});
c.registerChallengeFetchedCallback(e=>{e=e.challenge;if(!e)throw Error("BGE_MACR");e={challenge:e,wb:ry(e),vm:d,bgChallenge:new hk};e=Promise.resolve(e);a.h=e});
const d=await Pb(uy());c=c.getLatestChallengeResponse().challenge;if(!c)throw Error("BGE_MACIL");return{challenge:c,wb:ry(c),vm:d,bgChallenge:new hk}}
async function Lz(a){var b=Kz(void 0,pk().h);let c;try{c=await Mz(a,b)}catch(f){return W(Error("Failed to fetch attestation challenge after 5 attempts; not retrying for 24h.")),Nz(a,864E5),{challenge:"",wb:{},vm:void 0,bgChallenge:void 0}}b=c.pf;const d=c.qf;Nz(a,sy(d)*1E3);a=void 0;let e;if("c1a"in d&&c.bgChallenge){e=qy(c.bgChallenge);try{await tk(pk(),e)}catch(f){return W(f),{challenge:b,wb:d,vm:a,bgChallenge:e}}try{a=new nk({challenge:e,Gb:{ka:"aGIf"}}),await a.Kb}catch(f){W(f),a=void 0}}return{challenge:b,
wb:d,vm:a,bgChallenge:e}}
async function Mz(a,b){let c=void 0,d=0;for(;d<5;){if(d>0){const e=1E3*Math.pow(2,d-1)+Math.random()*1E3;await new Promise(f=>{dq(()=>{f(void 0)},e)})}try{a.i.h(4,a.j++);
const e=await a.yb(b);return Oz(e)}catch(e){c=e,e instanceof Error&&W(e)}d++}throw c;}
function Nz(a,b){const c=Date.now()+b,d=async()=>{const e=c-Date.now();e<1E3?await Pz(a):dq(d,Math.min(e,6E4))};
d()}
async function Qz(a,b){vy(2);try{const c=await a.network.yb(b);c?c.challenge&&!c.bgChallenge?vy(1):vy(4):vy(3);return c}catch(c){vy(3)}}
function Oz(a){if(!a)throw Error("Fetching Attestation challenge returned falsy");if(!a.challenge)throw Error("Missing Attestation challenge");const b=a.challenge,c=ry(b);if("c1a"in c&&(!a.bgChallenge||!a.bgChallenge.program))throw Error("Expected bg challenge but missing.");return{...a,pf:b,qf:c}}
async function Pz(a){const b=await Promise.race([a.h,null]);var c=Lz(a);a.h=c;b?.vm?.dispose()}
var Sz=class{constructor(a,b,c){this.network=a;this.options=b;this.H=c;this.j=0;this.h=null;this.i=new zl;b.Pd?Iz(this,Jz(this)):b.preload&&Iz(this,new Promise(d=>{dq(()=>{d(Lz(this))},0)}))}async u(){return!!await Promise.race([this.h,
null])}async o(a,b,c){this.h===null&&Iz(this,Lz(this));let d=!1;const e={};return Promise.race([(async()=>{this.options.di&&this.options.Pd&&await (await ty())?.checkForRefresh();var f=await this.h;e.challenge=f.challenge;if(f.vm){var g={c:f.challenge,e:a,...b};try{d=!0;let h;(h=await f.vm.snapshot({Ka:g}))?e.webResponse=h:e.error="ATTESTATION_ERROR_VM_NO_RESPONSE"}catch{e.error="ATTESTATION_ERROR_VM_INTERNAL_ERROR"}}else"c1a"in f.wb&&(e.error="ATTESTATION_ERROR_VM_NOT_INITIALIZED");a==="ENGAGEMENT_TYPE_PLAYBACK"&&
(f=f.wb,g={},f.c6a&&(g.reportingStatus=String(Number(f.c)^Cy())),f.c6b&&(g.broadSpectrumDetectionResult=String(Number(f.c)^Number(P("CATSTAT",0)))),e.adblockReporting=g);return e})(),
Rz(c,()=>{const f=Object.assign({},e);d&&(f.error="ATTESTATION_ERROR_VM_TIMEOUT");return f})])}async yb(a){const b=this.H;
if(!b||b.ya())return Qz(this,a);Fz("att_pna");return new Promise(c=>{Ki(b,"publicytnetworkstatus-online",()=>{Qz(this,a).then(c)})})}};
function Rz(a,b){return new Promise(c=>{dq(()=>{c(b())},a)})}
function Kz(a,b){const c={engagementType:"ENGAGEMENT_TYPE_UNBOUND"};a&&(c.eacrToken=a);b&&(c.interpreterHash=b);return c}
;const Tz={WEB_UNPLUGGED:"^unplugged/",WEB_UNPLUGGED_ONBOARDING:"^unplugged/",WEB_UNPLUGGED_OPS:"^unplugged/",WEB_UNPLUGGED_PUBLIC:"^unplugged/",WEB_CREATOR:"^creator/",WEB_KIDS:"^kids/",WEB_EXPERIMENTS:"^experiments/",WEB_MUSIC:"^music/",WEB_REMIX:"^music/",WEB_MUSIC_EMBEDDED_PLAYER:"^music/",WEB_MUSIC_EMBEDDED_PLAYER:"^main_app/|^sfv/"};
function Uz(a){if(a.length===1)return a[0];var b=Tz.UNKNOWN_INTERFACE;if(b){b=new RegExp(b);for(var c of a)if(b.exec(c))return c}const d=[];Object.entries(Tz).forEach(([e,f])=>{"UNKNOWN_INTERFACE"!==e&&d.push(f)});
c=new RegExp(d.join("|"));a.sort((e,f)=>e.length-f.length);
for(const e of a)if(!c.exec(e))return e;return a[0]}
;var Xz=class{constructor(){this.h=Vz.instance}yb(a){Fz("att_fsr");return Wz(this.h,a).then(b=>{Fz("att_frr");return b})}};var Yz=new Mu("INNERTUBE_TRANSPORT_TOKEN");async function Zz(){var a=Tu().resolve(Yz);if(a){if(a=await $z(a)){if(a.errorMetadata){W(Error(`Datasync IDs fetch responded with ${a.errorMetadata.status}: ${a.error}`));return}return a.Yh}W(Error("Network request to get Datasync IDs failed."))}else W(Error("InnertubeTransportService unavailable in fetchDatasyncIds"))}
;function aA(a,b){if(b.encryptedTokenJarContents&&(a.h[b.encryptedTokenJarContents]=b,typeof b.expirationSeconds==="string")){const c=Number(b.expirationSeconds);setTimeout(()=>{delete a.h[b.encryptedTokenJarContents]},c*1E3);
a.i&&Lp("CONSISTENCY",b.encryptedTokenJarContents,c,void 0,!0)}}
var bA=class{constructor(){this.h={};if(this.i=Op()){const a=Mp("CONSISTENCY");a&&aA(this,{encryptedTokenJarContents:a})}}handleResponse(a,b){if(!b)throw Error("request needs to be passed into ConsistencyService");b=b.Cb.context?.request?.consistencyTokenJars||[];if(a=a.responseContext?.consistencyTokenJar){for(const c of b)delete this.h[c.encryptedTokenJarContents];aA(this,a)}}};const cA=window.location.hostname.split(".").slice(-2).join(".");function dA(a){return a.localStorage===void 0?new Kq("yt-client-location"):a.localStorage}
function eA(){fA=w("yt.clientLocationService.instance");fA||(fA=new gA,v("yt.clientLocationService.instance",fA));return fA}
var gA=class{constructor(){this.i=-1;let a=P("LOCATION_PLAYABILITY_TOKEN");P("INNERTUBE_CLIENT_NAME")==="TVHTML5"&&(this.localStorage=dA(this))&&(a=this.localStorage.get("yt-location-playability-token"));a&&(this.locationPlayabilityToken=a,this.h=void 0)}setLocationOnInnerTubeContext(a){a.client||(a.client={});if(this.h)a.client.locationInfo||(a.client.locationInfo={}),a.client.locationInfo.latitudeE7=Math.floor(this.h.coords.latitude*1E7),a.client.locationInfo.longitudeE7=Math.floor(this.h.coords.longitude*
1E7),a.client.locationInfo.horizontalAccuracyMeters=Math.round(this.h.coords.accuracy),a.client.locationInfo.forceLocationPlayabilityTokenRefresh=!0;else if(this.j||this.locationPlayabilityToken)a.client.locationPlayabilityToken=this.j||this.locationPlayabilityToken}handleResponse(a){a=a.responseContext?.locationPlayabilityToken;a!==void 0&&(this.locationPlayabilityToken=a,this.h=void 0,P("INNERTUBE_CLIENT_NAME")==="TVHTML5"?(this.localStorage=dA(this))&&this.localStorage.set("yt-location-playability-token",
a,15552E3):Lp("YT_CL",JSON.stringify({loctok:a}),15552E3,cA,!0))}clearLocationPlayabilityToken(a){a==="TVHTML5"?(this.localStorage=dA(this))&&this.localStorage.remove("yt-location-playability-token"):Np("YT_CL");this.j=void 0;this.i!==-1&&(clearTimeout(this.i),this.i=-1)}getCurrentPositionFromGeolocation(){if(!(navigator&&navigator.geolocation&&navigator.geolocation.getCurrentPosition))return Promise.reject(Error("Geolocation unsupported"));let a=!1,b=1E4;P("INNERTUBE_CLIENT_NAME")==="MWEB"&&(a=!0,
b=15E3);return new Promise((c,d)=>{navigator.geolocation.getCurrentPosition(e=>{this.h=e;c(e)},e=>{d(e)},{enableHighAccuracy:a,
maximumAge:0,timeout:b})})}createUnpluggedLocationInfo(a){const b={};
a=a.coords;a?.latitude&&(b.latitudeE7=Math.floor(a.latitude*1E7));a?.longitude&&(b.longitudeE7=Math.floor(a.longitude*1E7));a?.accuracy&&(b.locationRadiusMeters=Math.round(a.accuracy));return b}createLocationInfo(a){const b={};a=a.coords;a?.latitude&&(b.latitudeE7=Math.floor(a.latitude*1E7));a?.longitude&&(b.longitudeE7=Math.floor(a.longitude*1E7));return b}},fA;function hA(a,b=!1,c=!1){var d=P("INNERTUBE_CONTEXT");if(!d)return kw(Error("Error: No InnerTubeContext shell provided in ytconfig.")),{};d=mh(d);S("web_no_tracking_params_in_shell_killswitch")||delete d.clickTracking;d.client||(d.client={});var e=d.client;e.clientName==="MWEB"&&e.clientFormFactor!=="AUTOMOTIVE_FORM_FACTOR"&&(e.clientFormFactor=P("IS_TABLET")?"LARGE_FORM_FACTOR":"SMALL_FORM_FACTOR");e.screenWidthPoints=window.innerWidth;e.screenHeightPoints=window.innerHeight;e.screenPixelDensity=
Math.round(window.devicePixelRatio||1);e.screenDensityFloat=window.devicePixelRatio||1;e.utcOffsetMinutes=-Math.floor((new Date).getTimezoneOffset());Qp();var f="USER_INTERFACE_THEME_LIGHT";Tp(165)?f="USER_INTERFACE_THEME_DARK":Tp(174)?f="USER_INTERFACE_THEME_LIGHT":!S("kevlar_legacy_browsers")&&window.matchMedia&&window.matchMedia("(prefers-color-scheme)").matches&&window.matchMedia("(prefers-color-scheme: dark)").matches&&(f="USER_INTERFACE_THEME_DARK");f=py()||f;e.userInterfaceTheme=f;if(!b){if(f=
$p())e.connectionType=f;S("web_log_effective_connection_type")&&(f=aq())&&(d.client.effectiveConnectionType=f)}S("web_log_memory_total_kbytes")&&t.navigator?.deviceMemory&&(d.client.memoryTotalKbytes=`${t.navigator?.deviceMemory*1E6}`);if(S("web_gcf_hashes_innertube")){var g=Cs();if(g){f=g.coldConfigData;const n=g.coldHashData;g=g.hotHashData;d.client.configInfo=d.client.configInfo||{};f&&(d.client.configInfo.coldConfigData=f);n&&(d.client.configInfo.coldHashData=n);g&&(d.client.configInfo.hotHashData=
g)}}f=No(t.location.href);!S("web_populate_internal_geo_killswitch")&&f.internalcountrycode&&(e.internalGeo=f.internalcountrycode);e.clientName==="MWEB"||e.clientName==="WEB"?(e.mainAppWebInfo||(e.mainAppWebInfo={}),e.mainAppWebInfo.graftUrl=t.location.href,S("kevlar_woffle")&&Hp.instance&&(f=Hp.instance,e.mainAppWebInfo.pwaInstallabilityStatus=!f.h&&f.i?"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED":"PWA_INSTALLABILITY_STATUS_UNKNOWN"),e.mainAppWebInfo.webDisplayMode=Gp(),e.mainAppWebInfo.isWebNativeShareAvailable=
navigator&&navigator.share!==void 0):e.clientName==="TVHTML5"&&(!S("web_lr_app_quality_killswitch")&&(f=P("LIVING_ROOM_APP_QUALITY"))&&(e.tvAppInfo=Object.assign(e.tvAppInfo||{},{appQuality:f})),f=P("LIVING_ROOM_CERTIFICATION_SCOPE"))&&(e.tvAppInfo=Object.assign(e.tvAppInfo||{},{certificationScope:f}));if(!S("web_populate_time_zone_itc_killswitch")){a:{if(typeof Intl!=="undefined")try{var h=(new Intl.DateTimeFormat).resolvedOptions().timeZone;break a}catch{}h=void 0}h&&(e.timeZone=h)}(h=P("EXPERIMENTS_TOKEN",
""))?e.experimentsToken=h:delete e.experimentsToken;e=bp();bA.instance||(bA.instance=new bA);h=eh(bA.instance.h);d.request={...d.request,internalExperimentFlags:e,consistencyTokenJars:h};!S("web_prequest_context_killswitch")&&(e=P("INNERTUBE_CONTEXT_PREQUEST_CONTEXT"))&&(d.request.externalPrequestContext=e);h=Qp();e=Tp(58);h=h.get("gsml","");d.user={...d.user};e&&(d.user.enableSafetyMode=e);h&&(d.user.lockedSafetyMode=!0);S("warm_op_csn_cleanup")?c&&(b=Iw())&&(d.clientScreenNonce=b):!b&&(b=Iw())&&
(d.clientScreenNonce=b);a&&(d.clickTracking={clickTrackingParams:a});if(a=w("yt.mdx.remote.remoteClient_"))d.remoteClient=a;eA().setLocationOnInnerTubeContext(d);try{var k=Ro(),l=k.bid;delete k.bid;d.adSignalsInfo={params:[],bid:l};for(const [n,m]of Object.entries(k))k=n,l=m,d.adSignalsInfo.params?.push({key:k,value:`${l}`});if(d.client?.clientName==="TVHTML5"||d.client?.clientName==="TVHTML5_UNPLUGGED"){const n=P("INNERTUBE_CONTEXT");n.adSignalsInfo&&(d.adSignalsInfo.advertisingId=n.adSignalsInfo.advertisingId,
d.adSignalsInfo.advertisingIdSignalType="DEVICE_ID_TYPE_CONNECTED_TV_IFA",d.adSignalsInfo.limitAdTracking=n.adSignalsInfo.limitAdTracking)}}catch(n){kw(n)}return d}
;function iA(a){const b={"Content-Type":"application/json"};P("EOM_VISITOR_DATA")?b["X-Goog-EOM-Visitor-Id"]=P("EOM_VISITOR_DATA"):P("VISITOR_DATA")&&(b["X-Goog-Visitor-Id"]=P("VISITOR_DATA"));b["X-Youtube-Bootstrap-Logged-In"]=P("LOGGED_IN",!1);P("DEBUG_SETTINGS_METADATA")&&(b["X-Debug-Settings-Metadata"]=P("DEBUG_SETTINGS_METADATA"));a!=="cors"&&((a=P("INNERTUBE_CONTEXT_CLIENT_NAME"))&&(b["X-Youtube-Client-Name"]=a),(a=P("INNERTUBE_CONTEXT_CLIENT_VERSION"))&&(b["X-Youtube-Client-Version"]=a),(a=
P("CHROME_CONNECTED_HEADER"))&&(b["X-Youtube-Chrome-Connected"]=a),(a=P("DOMAIN_ADMIN_STATE"))&&(b["X-Youtube-Domain-Admin-State"]=a));(a=P("SERIALIZED_LAVA_DEVICE_CONTEXT"))&&(b["X-YouTube-Lava-Device-Context"]=a);return b}
;function jA(a){return()=>new a}
;var kA=class{u(a,b={},c=Kp){var d={context:hA(a.clickTrackingParams,!1,this.o)};var e=this.i(a);if(e){this.h(d,e,b);e=`/youtubei/v1/${Uz(this.j())}`;const f=sv(a.commandMetadata,ho)?.apiUrl;f&&(e=f);e=Vw(Uw(e));a={command:a,...(void 0)};d={input:e,Ua:Ww(e),Cb:d,config:a};d.config.Qb?d.config.Qb.identity=c:d.config.Qb={identity:c};b.abortSignal&&(d.Ua.signal=b.abortSignal);return d}b=new T("Error: Failed to create Request from Command.",a);kw(b)}get o(){return!1}},lA=class extends kA{};const mA={GET_DATASYNC_IDS:jA(class extends lA{u(){return{input:"/getDatasyncIdsEndpoint",Ua:Ww("/getDatasyncIdsEndpoint","GET"),Cb:{}}}j(){return[]}i(){}h(){}})};const nA="tokens consistency service_params mss client_location entities adblock_detection response_received_commands store manifest player_preload shorts_prefetch".split(" "),oA=["type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.BrowseResponse","type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.PlayerResponse","type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.PanelResponse"];
function pA(a,b,c){var d=qA;if(Vz.instance!==void 0){if(c=Vz.instance,a=[d!==c.o,a!==c.ha,b!==c.i,!1,!1,!1,!1],a.some(e=>e))throw new T("InnerTubeTransportService is already initialized",a);
}else Vz.instance=new Vz(d,a,b,c)}
function Wz(a,b){var c=`/youtubei/v1/${Uz(mx)}`,d={Qb:{identity:Kp}};let e=()=>{};
e=Dz(Cz(c));b.context||(b.context=hA(void 0,!0));return new ej(async f=>{var g=Uw(c);g=Qo(g)?"same-origin":"cors";g=a.i.Md?rA(d,g):await sA(d,g);var h=Vw(Uw(c));h={input:h,Ua:Ww(h),Cb:b,config:d};f(tA(a,h,g,e))})}
function $z(a){var b={signalServiceEndpoint:{signal:"GET_DATASYNC_IDS"}};const c=uA(a,b);return c?new ej(async(d,e)=>{const f=(await c).u(b,void 0,Kp);f?(ky(f.input),e=f.Ua?.mode==="cors"?"cors":void 0,e=a.i.Md?rA(f.config,e):await sA(f.config,e),d(tA(a,f,e))):e(new T("Error: Failed to build request for command.",b))}):jj(new T("Error: No request builder found for command.",b))}
function uA(a,b){a:{a=a.o;var c=sv(b,io)?.signal;if(c&&a.dc&&(c=a.dc[c])){var d=c();break a}if((c=sv(b,go)?.request)&&a.te&&(c=a.te[c])){d=c();break a}for(d in b)if(a.pd[d]&&(b=a.pd[d])){d=b();break a}d=void 0}if(d!==void 0)return Promise.resolve(d)}
function rA(a,b){a=Ip({sessionIndex:a?.Qb?.sessionIndex});return{...iA(b),...a}}
async function sA(a,b){a=Ip({sessionIndex:a?.Qb?.sessionIndex});if(!(a instanceof ej)){var c=new ej(cj);fj(c,2,a);a=c}a=await a;return Promise.resolve({...iA(b),...a})}
async function tA(a,b,c,d=()=>{}){await vA(b);
const e=b.config?.requestKey;if(e&&a.h.has(e))var f=a.h.get(e);else f=JSON.stringify(b.Cb),b.Ua={...b.Ua,headers:{...(b.Ua?.headers??{}),...c}},c={...b.Ua},b.Ua.method==="POST"&&(c={...c,body:f}),b.config?.uf&&Az(b.config.uf),f=a.ha.fetch(b.input,c,b.config),e&&a.h.set(e,f);(f=await f)&&S("web_streaming_player")&&Array.isArray(f)&&(f=f[0].playerResponse);if(f&&"error"in f&&f?.error?.details){c=f.error.details;for(const g of c)(c=g["@type"])&&oA.indexOf(c)>-1&&(delete g["@type"],f=g)}e&&a.h.has(e)&&
a.h.delete(e);b.config?.wf&&Az(b.config.wf);wA(a,f,b);b.config?.tf&&Az(b.config.tf);d();return f||void 0}
async function vA(a){if(a?.Cb?.context){a=a.Cb.context;for(const b of[])await b.yi(a)}}
function wA(a,b,c){if(b&&!b?.sequenceMetaData?.skipProcessing&&a.j)for(const d of nA)a.j[d]&&a.j[d].handleResponse(b,c)}
var Vz=class{constructor(a,b,c,d){this.o=a;this.ha=b;this.i=c;this.j=d;this.h=new Map;a.dc||(a.dc={});a.dc={...mA,...a.dc}}};var xA=class extends lA{j(){return sx}get o(){return!0}i(a){return sv(a,to)||void 0}h(a,b,c={}){b.channelIds&&(a.channelIds=b.channelIds);b.siloName&&(a.siloName=b.siloName);b.params&&(a.params=b.params);c.botguardResponse&&(a.botguardResponse=c.botguardResponse);c.feature&&(a.clientFeature=c.feature)}};var yA=class extends lA{j(){return tx}get o(){return!0}i(a){return sv(a,so)||void 0}h(a,b){b.channelIds&&(a.channelIds=b.channelIds);b.siloName&&(a.siloName=b.siloName);b.params&&(a.params=b.params)}};var zA=class extends lA{constructor(a){super();this.H=a}j(){return nx}i(a){return sv(a,mo)||sv(a,no)||sv(a,lo)}h(a,b){b.serializedShareEntity&&(a.serializedSharedEntity=b.serializedShareEntity);b.clientParamIdentifier&&this.H?.h(b.clientParamIdentifier)&&(a.clientParams=this.H.i(b.clientParamIdentifier))}};zA[Lu]=[new Mu("SHARE_CLIENT_PARAMS_PROVIDER_TOKEN")];var AA=class extends lA{j(){return px}get o(){return!0}i(a){return sv(a,ko)||void 0}h(a,b,c){a.feedbackTokens=[];b.feedbackToken&&a.feedbackTokens.push(b.feedbackToken);if(b=b.cpn||c.cpn)a.feedbackContext={cpn:b};a.isFeedbackTokenUnencrypted=!!c.is_feedback_token_unencrypted;a.shouldMerge=!1;c.extra_feedback_tokens&&(a.shouldMerge=!0,a.feedbackTokens=a.feedbackTokens.concat(c.extra_feedback_tokens))}};var BA=class extends lA{j(){return px}i(a){return sv(a,ro)}get o(){return!0}h(a,b){b.undoToken&&(a.feedbackTokens=[b.undoToken]);b.isUndoTokenUnencrypted&&(a.isFeedbackTokenUnencrypted=b.isUndoTokenUnencrypted)}};var CA=class extends lA{j(){return qx}i(a){return sv(a,qo)||void 0}h(a,b){b.params&&(a.params=b.params);b.secondaryParams&&(a.secondaryParams=b.secondaryParams)}};var DA=class extends lA{j(){return rx}i(a){return sv(a,po)||void 0}h(a,b){b.actions&&(a.actions=b.actions);b.params&&(a.params=b.params);b.playlistId&&(a.playlistId=b.playlistId)}};var EA=class extends lA{j(){return ox}i(a){return sv(a,oo)}h(a,b,c={}){b.serializedShareEntity&&(a.serializedSharedEntity=b.serializedShareEntity);c.includeListId&&(a.includeListId=!0)}};let FA=t.caches,GA;function HA(a){const b=a.indexOf(":");return b===-1?{Bd:a}:{Bd:a.substring(0,b),datasyncId:a.substring(b+1)}}
async function IA(){return GA!==void 0?GA:GA=new Promise(async a=>{try{await FA.open("test-only"),await FA.delete("test-only")}catch(b){if(b instanceof Error&&b.name==="SecurityError"){a(!1);return}}a("caches"in window)})}
async function JA(a){if(await IA()){var b=[],c=await FA.keys();for(const d of c)({datasyncId:c}=HA(d)),!c||a.includes(c)||b.push(FA.delete(d));Promise.all(b).then(d=>d.some(e=>e))}}
async function KA(){if(!await IA())return!1;const a=cq("cache contains other");var b=await FA.keys();for(const c of b)if({datasyncId:b}=HA(c),b&&b!==a)return!0;return!1}
;function LA(){try{return!!self.sessionStorage}catch{return!1}}
;function MA(a){a=a.match(/(.*)::.*::.*/);if(a!==null)return a[1]}
function NA(a){if(LA()){var b=Object.keys(window.sessionStorage);for(const c of b)b=MA(c),b===void 0||a.includes(b)||self.sessionStorage.removeItem(c)}}
function OA(){if(!LA())return!1;const a=cq();var b=Object.keys(window.sessionStorage);for(const c of b)if(b=MA(c),b!==void 0&&b!==a)return!0;return!1}
;function PA(){Zz().then(a=>{a&&(es(a),JA(a),fy(a),NA(a))})}
function QA(){var a=new Zt;Kl.va(async()=>{if(!S("ytidb_clear_optimizations_killswitch")){var b=cq("clear");if(b.startsWith("V")&&b.endsWith("||")){b=[b];es(b);JA(b);fy(b);NA(b);return}b=gy();const c=OA(),d=await KA(),e=await gs();if(!(b||c||d||e))return}a.ya()?PA():Ki(a,"publicytnetworkstatus-online",PA)})}
;function RA(a){return new Promise(b=>{window.setTimeout(b,a)})}
async function Dk(a,b,c){xz();Az("att_fs",void 0,"attestation_challenge_fetch");if(!a.h)throw new Dj(9,"Missing fetcher");const d=await a.h(b,c);b=d?.bgChallenge;if(!b)throw new Dj(15,"Missing field");a.i=d;a.j.forEach(e=>{e(d)});
a=qy(b);Az("att_fc",void 0,"attestation_challenge_fetch");yz();return a}
async function ll(a,b){const c=new Rh(100,3E5,.25,2);let d=void 0;for(;c.i<10;)try{return c.i>0&&await RA(c.getValue()),await SA(a,b)}catch(e){d=e instanceof Dj?e:new Dj(9,e instanceof Error?e.message:"Unknown"),Sh(c)}if(d)throw d;throw new Dj(9,"Unknown error");}
function SA(a,b){b=wk(xk(new yk,b),a.requestKey);const c=new lk,d=a.u();d.open("POST",a.o);d.setRequestHeader("X-Goog-Api-Key","AIzaSyDyT5W0Jh49F30Pqqtyfdf7pDLFKLJoAnw");d.setRequestHeader("Content-Type","application/json+protobuf");d.onload=()=>{if(Vo(d)){const e=Il(d.responseText);c.resolve(e)}else c.reject(new Dj(Bj(Wo(d)),d.statusText))};
d.onerror=()=>{c.reject(new Dj(Bj(Wo(d)),d.statusText))};
d.send(b.serialize());return c.promise}
var TA=class{constructor(a,b,c){this.requestKey=a;this.o=b;this.i=c;this.u=()=>new XMLHttpRequest;
this.h=void 0;this.j=[]}getLatestChallengeResponse(){return this.i}};function UA(a){const b={bicf:d=>{a.h=d},
blc:()=>a.getLatestChallengeResponse(),
bcr:d=>{a.j.push(d)}},c=window;
c.ntpevasrs=b;if(c.ntpqfbel!==void 0)for(const d of c.ntpqfbel)d(b);c.ntpqfbel=void 0}
;function VA(a){if(a instanceof Error){var b=w("yt.logging.errors.log");b&&b(a,"WARNING")}}
;function WA(a,b){a=new XA(a,b);YA(a);b?.ai||ZA(a)}
function YA(a){if(!a.vm){var b={maxAttempts:5,Fd:a.ttlSeconds*1E3};a.Rb.ytcsi?.tick?.("pot_ist");a.vm=a.Td({Oa:a.Oa,Gb:{disable:S("html5_web_po_disable_remote_logging"),ka:"aGIf",Je:$o(),hf:S("wpo_dis_lfdms")?0:1E3,Mb:d=>{var e=cy.get(d);e||(e=new by(d),e=new Aj(e),cy.set(d,e));return e}},
Nb:b,Se:a.bgChallenge,zc:VA});a.h=Date.now();Ik(a.vm,()=>{a.h=Date.now()});
a.Rb.bgevmc={p:()=>{a.vm?.pause()},
r:()=>{a.vm?.resume()},
cr:()=>a.vm?.checkForRefresh()??Promise.resolve()};
Wb(a.vm,async()=>ZA(a),uy());
var c=a.j.bind(a);a.Zc&&a.ttlSeconds>0&&a.Zc.then(d=>{d.listen("publicytnetworkstatus-online",c)});
a.Gd(c)}}
function ZA(a){if(a.i)return a.i;if(!a.vm)throw Error("VMNI");a.i=new vl({vm:a.vm,Oa:a.Oa,ld:!0,onError:VA,Nb:a.Vd});return a.i}
var XA=class{constructor(a,b){this.h=0;this.Rb=b?.Rb??window;this.Zc=b?.Zc;this.requestKey=b?.requestKey??(ap("par_bir_key")||"O43z0dpjhgX20SCx4KAo");this.Td=b?.Td??(d=>new Lk(d));
const c=b?.gi??((d,e,f)=>new TA(d,e,f));
this.bgChallenge=qy(a.bgChallenge);this.ttlSeconds=sy(ry(a.challenge||""));this.Oa=c(this.requestKey,S("par_at_ep")?["www.youtube.com","m.youtube.com"].includes(t.location.hostname)?"/api/jnn/v1/GenerateIT":"https://jnn-pa.googleapis.com/$rpc/google.internal.waa.v1.Waa/GenerateIT":"https://jnn-pa.googleapis.com/$rpc/google.internal.waa.v1.Waa/GenerateIT",a);this.Vd=b?.Vd;UA(this.Oa);this.Gd=b?.Gd??(d=>{Ci(this.Rb.document,"visibilitychange",()=>{this.Rb.document.visibilityState==="visible"&&d()})})}j(){Date.now()>
this.h+this.ttlSeconds*1E3&&this.vm?.G()}};
function $A(a){try{const b=JSON.parse(a);if(b.bgChallenge)return b}catch(b){}}
function aB(a=window){var b={},c=a.ytAtR;b?.vd?.zi();if(c){if(c=$A(c))b?.vd?.Ed("SUCCESS"),WA(c,b);a.ytAtR=void 0}else a.ytAtRC=d=>{if(d=$A(d))b?.vd?.Ed("SUCCESS"),WA(d,b),a.ytAtRC=void 0}}
;const bB=["www.youtube-nocookie.com","www.youtubeeducation.com","youtube.googleapis.com"];function cB(a,b,c,d,e,f){c?(a.state=2,wx($n(c),()=>{window.trayride?dB(a,d,e):(a.state=3,yx(c),W(new T("BL:ULB",`${c}`)))},f)):b?(f=sh("SCRIPT"),b instanceof Xa?(f.textContent=Za(b),$a(f)):f.textContent=b,f.nonce=Wa(document),document.head.appendChild(f),document.head.removeChild(f),window.trayride?dB(a,d,e):(a.state=4,W(new T("BL:ULBJ")))):W(new T("BL:ULV"))}
function dB(a,b,c){a.state=5;const d=!!a.h&&bB.includes(zb(a.h)||"");try{const e=new nk({program:b,globalName:"trayride",Gb:{disable:!S("att_web_record_metrics")||!S("att_skip_metrics_for_cookieless_domains_ks")&&d,ka:"aGIf"}});e.Kb.then(()=>{a.state=6;c&&c(b)});
a.i(e)}catch(e){a.state=7,e instanceof Error&&W(e)}}
var eB=class{constructor(){this.state=1;this.vm=null;this.h=void 0}initialize(a,b,c,d){this.h=d;if(a.program){var e;d=a.interpreterUrl??null;a.interpreterSafeScript?e=Yn(a.interpreterSafeScript):e=a.interpreterScript??null;a.interpreterSafeUrl&&(d=Zn(a.interpreterSafeUrl).toString());cB(this,e,d,a.program,b,c)}else W(Error("BL:CIP"))}isLoading(){return this.state===2}invoke(a={}){return this.j()?this.o({Ka:a}):null}dispose(){this.i(null);this.state=8}j(){return!!this.vm}o(a){return this.vm.Kd(a)}i(a){Mb(this.vm);
this.vm=a}};function fB(){const a=w("yt.abuse.playerAttLoader");return a&&["bgvma","bgvmb","bgvmc"].every(b=>b in a)?a:null}
;var gB=class extends eB{i(a){fB()?.bgvma();if(a){const b={bgvma:a.dispose.bind(a),bgvmb:a.snapshot.bind(a),bgvmc:a.Kd.bind(a)};v("yt.abuse.playerAttLoader",b);v("yt.abuse.playerAttLoaderRun",c=>a.snapshot(c))}else v("yt.abuse.playerAttLoader",null),v("yt.abuse.playerAttLoaderRun",null)}j(){return!!fB()}o(a){return fB().bgvmc(a)}};var hB=new Mu("AUTH_SERVICE_TOKEN");var iB=class extends jv{constructor(){super("document_active");this.i=10;this.h=new Map;this.transitions=[{from:"document_active",to:"document_disposed_preventable",action:this.F},{from:"document_active",to:"document_disposed",action:this.u},{from:"document_disposed_preventable",to:"document_disposed",action:this.u},{from:"document_disposed_preventable",to:"flush_logs",action:this.H},{from:"document_disposed_preventable",to:"document_active",action:this.j},{from:"document_disposed",to:"flush_logs",
action:this.H},{from:"document_disposed",to:"document_active",action:this.j},{from:"document_disposed",to:"document_disposed",action:()=>{}},
{from:"flush_logs",to:"document_active",action:this.j}];window.addEventListener("pagehide",a=>{this.transition("document_disposed",{event:a});a.persisted===!1&&(this.h=new Map)});
window.addEventListener("beforeunload",a=>{this.transition("document_disposed_preventable",{event:a})})}F(a,b){if(!this.h.get("document_disposed_preventable")&&(a(b?.event),b?.event?.defaultPrevented||b?.event?.returnValue)){b.event.returnValue||(b.event.returnValue=!0);
b.event.defaultPrevented||b.event.preventDefault();this.h=new Map;this.transition("document_active");return}this.h.set("document_disposed_preventable",!0);this.h.get("document_disposed")?this.transition("flush_logs"):this.transition("document_disposed")}u(a,b){this.h.get("document_disposed")?this.transition("document_active"):(a(b?.event),this.h.set("document_disposed",!0),this.transition("flush_logs"))}H(a,b){a(b?.event);this.transition("document_active")}j(){this.h=new Map}};var jB=class extends jv{constructor(){super("document_visibility_unknown");this.transitions=[{from:"document_visibility_unknown",to:"document_visible",action:this.j},{from:"document_visibility_unknown",to:"document_hidden",action:this.h},{from:"document_visibility_unknown",to:"document_foregrounded",action:this.H},{from:"document_visibility_unknown",to:"document_backgrounded",action:this.u},{from:"document_visible",to:"document_hidden",action:this.h},{from:"document_visible",to:"document_foregrounded",
action:this.H},{from:"document_visible",to:"document_visible",action:this.j},{from:"document_foregrounded",to:"document_visible",action:this.j},{from:"document_foregrounded",to:"document_hidden",action:this.h},{from:"document_foregrounded",to:"document_foregrounded",action:this.H},{from:"document_hidden",to:"document_visible",action:this.j},{from:"document_hidden",to:"document_backgrounded",action:this.u},{from:"document_hidden",to:"document_hidden",action:this.h},{from:"document_backgrounded",to:"document_hidden",
action:this.h},{from:"document_backgrounded",to:"document_backgrounded",action:this.u},{from:"document_backgrounded",to:"document_visible",action:this.j}];document.addEventListener("visibilitychange",a=>{document.visibilityState==="visible"?this.transition("document_visible",{event:a}):this.transition("document_hidden",{event:a})});
S("visibility_lifecycles_dynamic_backgrounding")&&(window.addEventListener("blur",a=>{this.transition("document_backgrounded",{event:a})}),window.addEventListener("focus",a=>{this.transition("document_foregrounded",{event:a})}))}j(a,b){a(b?.event);
S("visibility_lifecycles_dynamic_backgrounding")&&this.transition("document_foregrounded")}h(a,b){a(b?.event);S("visibility_lifecycles_dynamic_backgrounding")&&this.transition("document_backgrounded")}u(a,b){a(b?.event)}H(a,b){a(b?.event)}};var kB=class{constructor(){this.o=new iB;this.u=new jB}install(...a){a.forEach(b=>{this.o.install(b)});
a.forEach(b=>{this.u.install(b)})}};function lB(a,b,c,d=0){if(!b)return!1;d=Iw(d);if(!d)return!1;a=a.client;b=new Aw({trackingParams:b});var e=void 0;if(S("no_client_ve_attach_unless_shown")){var f=Yx(b,d);Ux.set(f,!0);Zx(b,d)}e=e||"INTERACTION_LOGGING_GESTURE_TYPE_GENERIC_CLICK";f=Xx({cttAuthInfo:Kw(d)||void 0,automatedLogEventSource:void 0},d);b={csn:d,ve:b.getAsJson(),gestureType:e};c&&(b.clientData=c);d==="UNDEFINED_CSN"?$x("visualElementGestured",f,b):a?cw("visualElementGestured",b,a,f):Sq("visualElementGestured",b,f);return!0}
function mB(a,b,c,d=0){const e=Iw(d);b=b||Fw(d);e&&b&&(a=a.client,d=Xx({cttAuthInfo:Kw(e)||void 0},e),c={csn:e,ve:b.getAsJson(),clientData:c},e==="UNDEFINED_CSN"?$x("visualElementStateChanged",d,c):a?cw("visualElementStateChanged",c,a,d):Sq("visualElementStateChanged",c,d))}
function nB(a,b){if(b===void 0){const c=Hw();for(let d=0;d<c.length;d++)c[d]!==void 0&&nB(a,c[d])}else a.i.forEach((c,d)=>{(d=a.h.get(d))&&Wx(a.client,b,d,c)}),a.i.clear(),a.h.clear()}
var oB=class{constructor(){this.o=[];this.i=new Map;this.h=new Map;this.j=new Set}clickCommand(a,b,c=0){return lB(this,a.clickTrackingParams,b,c)}stateChanged(a,b,c=0){this.visualElementStateChanged(new Aw({trackingParams:a}),b,c)}visualElementStateChanged(a,b,c=0){c===0&&this.j.has(c)?this.o.push([a,b]):mB(this,a,b,c)}};var qB=class extends kB{constructor(){super();this.install({document_disposed:{callback:this.h}});S("combine_ve_grafts")&&this.install({document_disposed:{callback:this.i}});this.install({flush_logs:{callback:this.j}});S("web_log_cfg_cee_ks")||dq(pB)}j(){Sq("finalPayload",{csn:Iw()})}h(){tw(vw)}i(){var a=nB;oB.instance||(oB.instance=new oB);a(oB.instance)}};
function pB(){const a=P("CLIENT_EXPERIMENT_EVENTS");if(a){var b=Hd();for(const c of a)b(c)&&Sq("genericClientExperimentEvent",{eventType:c});delete zo.CLIENT_EXPERIMENT_EVENTS}}
;var rB=class extends T{constructor(a,...b){super(a,b);this.errorType=1;Object.setPrototypeOf(this,new.target.prototype)}};function sB(a,b,c){if(a.h){const d=Ab(Kb(b,"key"))||"/UNKNOWN_PATH";a.h.start(d)}a=c;S("wug_networking_gzip_request")&&(a=et(c));return new window.Request(b,a)}
async function tB(a,b,c,d,e){const {value:f,done:g}=await b.read();if(g)return a.h?.success(),d;let h;try{h=c.parse(f)}catch(k){throw new rB("Failed to parse streaming response",f);}if(h!=null)for(const k of h)d.push(k),e?.(k);return tB(a,b,c,d,e)}
var uB=class{constructor(a){this.h=a}async fetch(a,b,c,d){a=sB(this,a,b);try{const e=await fetch(a);if(S("web_unified_fetch")&&d&&e.ok&&e.body&&typeof e.body.getReader==="function"){const f=e.clone().body.getReader(),{value:g}=await f.read();f.cancel().catch(()=>{});
if(g&&g[0]===91){const h=e.body.pipeThrough(new TextDecoderStream).getReader();return tB(this,h,new dm,[],d)}}return await this.handleResponse(e,c)}catch(e){if(W(e),c?.Ie&&e instanceof rB&&e.errorType===1)throw e;}}handleResponse(a,b){let c;c=a.text().then(d=>{if(b?.af&&a.ok)return Tf(b.af,d);d=d.replace(")]}'","");let e;if(b?.Ie&&d)try{e=JSON.parse(d)}catch(f){throw new rB("JSON parsing failed after fetch");}return e??JSON.parse(d)});
a.redirected||a.ok?this.h&&this.h.success():(this.h&&this.h.fi(),c=c.then(d=>{W(new T("Error: API fetch failed",a.status,a.url,d));return{...d,errorMetadata:{status:a.status}}}));
return c}};uB[Lu]=[new Nu(new Mu("NETWORK_SLI_TOKEN"))];var vB=new Mu("NETWORK_MANAGER_TOKEN");function wB(){let a=w("ytglobal.storage_");a||(a=new xB,v("ytglobal.storage_",a));return a}
var xB=class{async estimate(){const a=navigator;if(a.storage?.estimate)return a.storage.estimate();if(a.webkitTemporaryStorage?.queryUsageAndQuota)return yB()}};function yB(){const a=navigator;return new Promise((b,c)=>{a.webkitTemporaryStorage?.queryUsageAndQuota?a.webkitTemporaryStorage.queryUsageAndQuota((d,e)=>{b({usage:d,quota:e})},d=>{c(d)}):c(Error("webkitTemporaryStorage is not supported."))})}
v("ytglobal.storageClass_",xB);function zB(a,b){wB().estimate().then(c=>{a.h("idbQuotaExceeded",{...b,isSw:self.document===void 0,isIframe:self!==self.top,deviceStorageUsageMbytes:AB(c?.usage),deviceStorageQuotaMbytes:AB(c?.quota)})})}
class Tq{constructor(a,b){this.handleError=a;this.h=b;this.i=!1;self.document===void 0||self.addEventListener("beforeunload",()=>{this.i=!0});
this.j=Math.random()<=.2}ta(a){this.handleError(a)}logEvent(a,b){switch(a){case "IDB_DATA_CORRUPTED":S("idb_data_corrupted_killswitch")||this.h("idbDataCorrupted",b);break;case "IDB_UNEXPECTEDLY_CLOSED":this.h("idbUnexpectedlyClosed",b);break;case "IS_SUPPORTED_COMPLETED":S("idb_is_supported_completed_killswitch")||this.h("idbIsSupportedCompleted",b);break;case "QUOTA_EXCEEDED":zB(this,b);break;case "TRANSACTION_ENDED":this.j&&Math.random()<=.1&&this.h("idbTransactionEnded",b);break;case "TRANSACTION_UNEXPECTEDLY_ABORTED":this.h("idbTransactionAborted",
{...b,hasWindowUnloaded:this.i})}}}function AB(a){return typeof a==="undefined"?"-1":String(Math.ceil(a/1048576))}
;var qA={pd:{feedbackEndpoint:jA(AA),modifyChannelNotificationPreferenceEndpoint:jA(CA),playlistEditEndpoint:jA(DA),shareEntityEndpoint:jA(zA),subscribeEndpoint:jA(xA),undoFeedbackEndpoint:jA(BA),unsubscribeEndpoint:jA(yA),webPlayerShareEntityServiceEndpoint:jA(EA)}};function BB(){const a=Tu();Ou(a,{Zb:vB,jd:uB});Ou(a,{Zb:hB,jd:Jp});const b=eA(),c=a.resolve(hB),d=a.resolve(vB),e={};b&&(e.client_location=b);pA(d,c,e);Ou(a,{Zb:Yz,Qd:Vz.instance})}
;const CB=new Map;function DB(a,b,c,d=()=>{},e=null){b=new EB(a,b,c,d,e);
CB.set(a,b)}
function FB(a){if(!a.onReadyPatchApplied){var b=a.addEventListener;a.addEventListener=(c,d)=>{c==="onReady"?Promise.resolve().then(()=>{d(a)}):b.call(a,c,d)};
a.onReadyPatchApplied=!0}}
function GB(a){if(w("yt.player.Application.create"))Promise.resolve().then(()=>{HB(a)});
else{IB(Zn(a.webPlayerContextConfig.trustedJsUrl),()=>{HB(a)},()=>{a.I||a.zc()});
const b=a.webPlayerContextConfig.trustedCssUrl;b&&JB(Zn(b))}}
function HB(a){if(!a.I){var b=w("yt.player.Application.create");try{a.api=b(a.container,{args:a.playerVars},a.webPlayerContextConfig,void 0).getInternalApi(),FB(a.api),a.api.isReady=()=>!0,a.h(a.api)}catch(c){throw a.zc(),c;
}}}
var EB=class extends y{constructor(a,b,c,d,e){super();this.container=a;this.webPlayerContextConfig=b;this.h=c;this.zc=d;this.playerVars=e;GB(this)}ba(){this.api&&this.api.destroy();th(this.container);super.ba()}};function JB(a){const b=`ytp-${a.toString()}`;if(!document.getElementById(b)){var c=document.createElement("link");c.id=b;fb(c,a);(document.getElementsByTagName("head")[0]||document.body).appendChild(c)}}
function IB(a,b,c){const d=`ytp-${a.toString()}`,e=document.getElementById(d);if(e)e.dataset.failed?c():e.dataset.loaded?b():(e.addEventListener("error",()=>{c()}),e.addEventListener("load",()=>{b()}));
else{var f=document.createElement("script");f.id=d;f.addEventListener("error",()=>{f.dataset.failed="true";c()});
f.addEventListener("load",()=>{f.dataset.loaded="true";b()});
ab(f,a);a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(f,a.firstChild)}}
;function KB(a){P("ENABLE_WEBVIEW_API")&&window.ytwebviewplayer&&(window.addEventListener("message",b=>{try{const d=JSON.parse(b.data),e=d.methodName,f=d.args||[];a:{for(const g of f)if(String(g).includes("javascript:")){var c=!0;break a}c=!1}if(c)throw Error(`Dangerous call to "${e}" with [${f}].`);if(e&&typeof a[e]==="function")a[e](...f);else throw Error(`Unknown API method: "${e}".`);}catch(d){kw(d)}}),a.addEventListener("onReady",()=>{window.ytwebviewplayer.postMessage(JSON.stringify({type:"onPlayerReady"}))}),
a.addEventListener("onStateChange",b=>{window.ytwebviewplayer.postMessage(JSON.stringify({type:"onStateChange",
state:b}))}),a.addEventListener("onError",b=>{window.ytwebviewplayer.postMessage(JSON.stringify({type:"onError",
errorCode:b}))}))}
;const LB={["api.invalidparam"]:2,auth:150,["drm.auth"]:150,["heartbeat.net"]:150,["heartbeat.servererror"]:150,["heartbeat.stop"]:150,["html5.unsupportedads"]:5,["fmt.noneavailable"]:5,["fmt.decode"]:5,["fmt.unplayable"]:5,["html5.missingapi"]:5,["html5.unsupportedlive"]:5,["drm.unavailable"]:5,["mrm.blocked"]:151,["embedder.identity.denied"]:152,["embedder.identity.missing.referrer"]:153};const MB=new Set("endSeconds startSeconds mediaContentUrl suggestedQuality videoId rct rctn playmuted muted_autoplay_duration_mode".split(" "));function NB(a){return(a.search("cue")===0||a.search("load")===0)&&a!=="loadModule"}
function OB(a,b,c){if(typeof a==="string")return{videoId:a,startSeconds:b,suggestedQuality:c};b={};for(const e of MB)a[e]&&(b[e]=a[e]);if(a=a.embedConfig||a.embed_config){a:if(typeof a==="string")var d=a;else{if(ma(a))try{d=JSON.stringify(a);break a}catch(e){console.error("Invalid embedConfig JSON",e)}d=void 0}b.embed_config=d}return b}
function PB(a,b,c,d){if(ma(a)&&!Array.isArray(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){const e=b[d];a[e]&&(c[e]=a[e])}return c}b={index:b,startSeconds:c,suggestedQuality:d};typeof a==="string"&&a.length===16?b.list="PL"+a:b.playlist=a;return b}
;function QB(a,b,c){a.o.push({eventType:b,listener:c});a.api.addEventListener(b,c)}
function RB(a){if(a.h)if(a.j)a.sendMessage("alreadyInitialized");else if(a.F){a.j=!0;a.F=!1;a.sendMessage("initialDelivery",SB(a));a.sendMessage("onReady");Az("ep_init_ar");for(const b of a.G)TB(a,b);a.G=[]}}
function TB(a,b,c=a.h){if(c){b.channel="widget";a.sessionId&&(b.id=a.sessionId);try{const d=JSON.stringify(b);c.postMessage(d,a.targetOrigin)}catch(d){W(d)}}}
function SB(a){if(!a.api)return null;const b=a.api.getApiInterface();mb(b,"getVideoData");const c={apiInterface:b};for(let e=0,f=b.length;e<f;e++){const g=b[e];if(g.search("get")===0||g.search("is")===0){var d=0;g.search("get")===0?d=3:g.search("is")===0&&(d=2);d=g.charAt(d).toLowerCase()+g.substring(d+1);try{const h=a.api[g]();c[d]=h}catch(h){}}}c.videoData=a.api.getVideoData();c.currentTimeLastUpdated_=Date.now()/1E3;return c}
function UB(a,b){a.sendMessage("infoDelivery",b)}
function VB(a,b,c){return d=>{b==="onError"?a.api.logApiCall(`${b} invocation`,c,d):a.api.logApiCall(`${b} invocation`,c);a.sendMessage(b,d)}}
var ZB=class extends y{constructor(){var a=WB,b=XB;super();this.api=a;this.j=this.F=!1;this.G=[];this.P={};this.o=[];this.i=[];this.Z=!1;this.sessionId=this.h=null;this.targetOrigin="*";this.Y=S("web_player_split_event_bus_iframe");this.A=P("POST_MESSAGE_ORIGIN")||`${document.location.protocol}//${document.location.hostname}`;this.u=c=>{this.onMessage(c)};
YB.addEventListener("message",this.u);if(a=P("WIDGET_ID"))this.sessionId=a;b&&this.u(b);QB(this,"onReady",()=>{this.F=!0;var c=this.api.getVideoData();c.isPlayable||(this.Z=!0,this.errorCode=(c=c.errorCode)?LB[c]||5:5,this.sendMessage("onError",Number(this.errorCode)));RB(this);this.h||this.j||window.parent===window||!this.sessionId||TB(this,{event:"readyToListen"},window.parent)});
QB(this,"onVideoProgress",this.Wa.bind(this));QB(this,"onVolumeChange",this.Ob.bind(this));QB(this,"onApiChange",this.ga.bind(this));QB(this,"onPlaybackQualityChange",this.Ba.bind(this));QB(this,"onPlaybackRateChange",this.Fa.bind(this));QB(this,"onStateChange",this.Ja.bind(this));QB(this,"onWebglSettingsChanged",this.Mc.bind(this));QB(this,"onCaptionsTrackListChanged",this.la.bind(this));QB(this,"captionssettingschanged",this.qa.bind(this))}sendMessage(a,b){a={event:a,info:b===void 0?null:b};this.j?
TB(this,a):this.G.push(a)}Ja(a){a={playerState:a,currentTime:this.api.getCurrentTime(),duration:this.api.getDuration(),videoData:this.api.getVideoData(),videoStartBytes:0,videoBytesTotal:this.api.getVideoBytesTotal(),videoLoadedFraction:this.api.getVideoLoadedFraction(),playbackQuality:this.api.getPlaybackQuality(),availableQualityLevels:this.api.getAvailableQualityLevels(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.api.getPlaybackRate(),mediaReferenceTime:this.api.getMediaReferenceTime()};
this.api.getVideoUrl&&(a.videoUrl=this.api.getVideoUrl());this.api.getVideoContentRect&&(a.videoContentRect=this.api.getVideoContentRect());this.api.getProgressState&&(a.progressState=this.api.getProgressState());this.api.getPlaylist&&(a.playlist=this.api.getPlaylist());this.api.getPlaylistIndex&&(a.playlistIndex=this.api.getPlaylistIndex());UB(this,a)}Ba(a){a={playbackQuality:a};this.api.getAvailableQualityLevels&&(a.availableQualityLevels=this.api.getAvailableQualityLevels());this.api.getPreferredQuality&&
(a.preferredQuality=this.api.getPreferredQuality());UB(this,a)}Fa(a){UB(this,{playbackRate:a})}ga(){const a=this.api.getOptions(),b={namespaces:a};for(let c=0,d=a.length;c<d;c++){const e=a[c],f=this.api.getOptions(e);a.join(", ");b[e]={options:f};for(let g=0,h=f.length;g<h;g++){const k=f[g],l=this.api.getOption(e,k);b[e][k]=l}}this.sendMessage("apiInfoDelivery",b)}Ob(){UB(this,{muted:this.api.isMuted(),volume:this.api.getVolume()})}Wa(a){a={currentTime:a,videoBytesLoaded:this.api.getVideoBytesLoaded(),
videoLoadedFraction:this.api.getVideoLoadedFraction(),currentTimeLastUpdated_:Date.now()/1E3,playbackRate:this.api.getPlaybackRate(),mediaReferenceTime:this.api.getMediaReferenceTime()};this.api.getProgressState&&(a.progressState=this.api.getProgressState());UB(this,a)}Mc(){UB(this,{sphericalProperties:this.api.getSphericalProperties()})}la(){if(this.api.getCaptionTracks){const a={captionTracks:this.api.getCaptionTracks()};UB(this,a)}}qa(){if(this.api.getSubtitlesUserSettings){const a={subtitlesUserSettings:this.api.getSubtitlesUserSettings()};
UB(this,a)}}onMessage(a){if(!(this.A!=="*"&&a.origin!==this.A||this.h&&a.source!==this.h||typeof a.data!=="string")){try{var b=JSON.parse(a.data)}catch(f){return}if(b)switch(b.event){case "listening":var c=a.source;a=a.origin;b=b.id;a!=="null"&&(this.A=this.targetOrigin=a);this.h=c;this.sessionId=b;RB(this);break;case "command":c=b.func;var d=b.args;if(c==="addEventListener"&&d)b=d[0],c=a.origin,b==="onReady"?this.api.logApiCall(`${b} invocation`,c):b==="onError"&&this.Z&&(this.api.logApiCall(`${b} invocation`,
c,this.errorCode),this.errorCode=void 0),this.api.logApiCall(`${b} registration`,c),this.P[b]||b==="onReady"||(a=VB(this,b,c),this.i.push({eventType:b,listener:a,origin:c}),this.Y?this.api.handleExternalCall("addEventListener",[b,a],c):this.api.addEventListener(b,a),this.P[b]=!0);else if(b=c,c=d,a=a.origin,this.api.isExternalMethodAvailable(b,a)){c=c||[];if(c.length>0&&NB(b)){var e=c;if(ma(e[0])&&!Array.isArray(e[0]))d=e[0];else switch(d={},b){case "loadVideoById":case "cueVideoById":d=OB(e[0],e[1]!==
void 0?Number(e[1]):void 0,e[2]);break;case "loadVideoByUrl":case "cueVideoByUrl":d=e[0];typeof d==="string"&&(d={mediaContentUrl:d,startSeconds:e[1]!==void 0?Number(e[1]):void 0,suggestedQuality:e[2]});b:{if((e=d.mediaContentUrl)&&(e=/\/([ve]|embed)\/([^#?]+)/.exec(e))&&e[2]){e=e[2];break b}e=null}d.videoId=e;d=OB(d);break;case "loadPlaylist":case "cuePlaylist":d=PB(e[0],e[1],e[2],e[3])}c.length=1;c[0]=d}this.api.handleExternalCall(b,c,a);NB(b)&&UB(this,SB(this))}}}}ba(){super.ba();YB.removeEventListener("message",
this.u);for(var a=0;a<this.o.length;a++){var b=this.o[a];this.api.removeEventListener(b.eventType,b.listener)}this.o=[];for(a=0;a<this.i.length;a++)b=this.i[a],this.Y?this.api.handleExternalCall("removeEventListener",[b.eventType,b.listener],b.origin):this.api.removeEventListener(b.eventType,b.listener);this.i=[]}};let YB=window;function $B(a,b,c){a.I||(b={id:a.id,command:b},c&&(b.data=c),aC.postMessage(JSON.stringify(b),a.origin))}
function bC(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}if(b!=null)return{value:b}}
function cC(a,b){switch(a){case "loadVideoById":return[OB(b)];case "cueVideoById":return[OB(b)];case "loadVideoByPlayerVars":return[b];case "cueVideoByPlayerVars":return[b];case "loadPlaylist":return[PB(b)];case "cuePlaylist":return[PB(b)];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];case "setLoop":return[b.loopPlaylists];case "setShuffle":return[b.shufflePlaylist];
case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey,b.ctrlKey,b.altKey,b.metaKey,b.key,b.code]}return[]}
function dC(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
var fC=class extends y{constructor(a,b){var c=WB;super();this.api=c;this.id=a;this.origin=b;this.h={};this.j=S("web_player_split_event_bus_iframe");this.i=d=>{this.onMessage(d)};
eC.addEventListener("message",this.i);$B(this,"RECEIVING")}addListener(a,b){if(!(a in this.h)){var c=this.o.bind(this,a);this.h[a]=c;this.addEventListener(a,c,b)}}o(a,b){this.I||$B(this,a,bC(a,b))}removeListener(a,b){a in this.h&&(this.removeEventListener(a,this.h[a],b),delete this.h[a])}addEventListener(a,b,c){this.j?a==="onReady"?this.api.addEventListener(a,b):this.api.handleExternalCall("addEventListener",[a,b],c||null):this.api.addEventListener(a,b)}removeEventListener(a,b,c){this.j?a==="onReady"?
this.api.removeEventListener(a,b):this.api.handleExternalCall("removeEventListener",[a,b],c||null):this.api.removeEventListener(a,b)}onMessage(a){if(a.origin===this.origin){var b=a.data;if(typeof b==="string"){try{b=JSON.parse(b)}catch(e){return}if(b.command){var c=b.command;b=b.data;a=a.origin;if(!this.I){var d=b||{};switch(c){case "addEventListener":typeof d.event==="string"&&this.addListener(d.event,a);break;case "removeEventListener":typeof d.event==="string"&&this.removeListener(d.event,a);break;
default:this.api.isReady()&&this.api.isExternalMethodAvailable(c,a||null)&&(b=cC(c,b||{}),b=this.api.handleExternalCall(c,b,a||null),(b=dC(c,b))&&$B(this,c,b))}}}}}}ba(){eC.removeEventListener("message",this.i);for(const a in this.h)this.h.hasOwnProperty(a)&&this.removeListener(a);super.ba()}};let eC=window,aC=window.parent;let gC=new gB;function hC(){return gC.j()}
function iC(a={}){return gC.invoke(a)}
;function jC(a){a.Fa=!1;if(a.la)for(var b in a.h)a.h.hasOwnProperty(b)&&a.la(b,a.h[b]);for(const c in a.G)a.G.hasOwnProperty(c)&&clearTimeout(Number(c));a.G={};a.u=null;a.la=null;b=a.api;for(const c in b)b.hasOwnProperty(c)&&(b[c]=null);b.addEventListener=(c,d)=>{a.addEventListener(c,d)};
b.removeEventListener=(c,d)=>{a.removeEventListener(c,d)};
b.destroy=()=>{a.dispose()};
b.getLastError=()=>a.getLastError();
b.getPlayerType=()=>a.getPlayerType();
b.getCurrentVideoConfig=()=>a.Ja;
b.loadNewVideoConfig=c=>{a.loadNewVideoConfig(c)};
b.isReady=()=>a.isReady()}
function kC(a){let b;a.webPlayerContextConfig?b=a.webPlayerContextConfig.rootElementId:b=a.config.attrs.id;a.elementId=b||a.elementId;a.elementId==="video-player"&&(a.elementId=a.A,a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.A:a.config.attrs.id=a.A);a.i?.id===a.elementId&&(a.elementId=`${a.elementId}-player`,a.webPlayerContextConfig?a.webPlayerContextConfig.rootElementId=a.elementId:a.config.attrs.id=a.elementId)}
function lC(a){if(!a.I&&!a.Y){var b=mC(a);if(b&&(nC(a)?"html5":null)==="html5")a.Z="html5",a.isReady()||oC(a);else if(pC(a),a.Z="html5",b&&a.j&&a.o)a.o.appendChild(a.j),oC(a);else{a.config&&(a.config.loaded=!0);let c=!1;a.F=()=>{c=!0;let d;d=qC(a,"player_bootstrap_method")?w("yt.player.Application.createAlternate")||w("yt.player.Application.create"):w("yt.player.Application.create");const e=a.config?rC(a.config):void 0;d&&d(a.o,e,a.webPlayerContextConfig,void 0);oC(a)};
a.Y=!0;b?a.F():(wx(sC(a),a.F),(b=tC(a))&&Dx(b||""),uC(a)&&!c&&v("yt.player.Application.create",null))}}}
function vC(a){a.config&&a.config.loaded!==!0&&(a.config.loaded=!0,!a.config.args||a.config.args.autoplay!=="0"&&a.config.args.autoplay!==0&&a.config.args.autoplay!==!1?a.api.loadVideoByPlayerVars(a.config.args??null):a.api.cueVideoByPlayerVars(a.config.args))}
function rC(a){const b={};for(const c of Object.keys(a)){const d=a[c];b[c]=typeof d==="object"?lh(d):d}return b}
function wC(a,b){let c=b;if(typeof b==="string"){if(a.Ba[b])return a.Ba[b];c=(...d)=>{const e=w(b);if(e)try{e.apply(t,d)}catch(f){throw d=new T("PlayerProxy error when executing callback",{error:f}),d.level="ERROR",d;}};
a.Ba[b]=c}return c?c:null}
function nC(a){let b=rh(a.elementId);!b&&a.i&&a.i.querySelector&&(b=a.i.querySelector(`#${a.elementId}`));return b}
function sC(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.jsUrl:(a=a.config.assets)?a.js:""}
function mC(a){let b=!0;const c=nC(a);c&&a.config&&(b=c.dataset.version===sC(a));return b&&!!w("yt.player.Application.create")}
function qC(a,b){let c;a.webPlayerContextConfig?c=a.webPlayerContextConfig.serializedExperimentFlags:a.config?.args&&(c=a.config.args.fflags);return(c||"").split("&").includes(`${b}=true`)}
function oC(a){if(!a.I){const b=nC(a);let c=!1;b&&b.getApiInterface&&b.getApiInterface()&&(c=!0);c?(a.Y=!1,!qC(a,"html5_remove_not_servable_check_killswitch")&&b?.isNotServable&&a.config&&b?.isNotServable(a.config.args?.video_id)||xC(a)):a.Wa=setTimeout(()=>{oC(a)},50)}}
function pC(a){a.cancel();jC(a);a.Z=null;a.config&&(a.config.loaded=!1);const b=nC(a);b&&(mC(a)||!uC(a)?a.j=b:(b&&b.destroy&&b.destroy(),a.j=null));a.o&&th(a.o)}
function tC(a){return a.webPlayerContextConfig?a.webPlayerContextConfig.cssUrl:(a=a.config.assets)?a.css:""}
function uC(a){a=a.config?.args?.fflags;return!!a&&a.indexOf("player_destroy_old_version=true")!==-1}
function xC(a){jC(a);a.Fa=!0;const b=nC(a);if(b){a.u=yC(a,b,"addEventListener");a.la=yC(a,b,"removeEventListener");let c=b.getApiInterface();c=c.concat(b.getInternalApiInterface());const d=a.api;for(let e=0;e<c.length;e++){const f=c[e];d[f]||(d[f]=yC(a,b,f))}}for(const c in a.h)a.h.hasOwnProperty(c)&&a.u&&a.u(c,a.h[c]);vC(a);a.qa&&a.qa(a.api);a.P.rb("onReady",a.api)}
function yC(a,b,c){const d=b[c];return(...e)=>{try{return a.lastError=null,d.apply(b,e)}catch(f){if(c!=="sendAbandonmentPing")throw f.params=c,a.lastError=f,e=new T("PlayerProxy error in method call",{error:f,method:c,playerId:a.A}),e.level="WARNING",e;}}}
function zC(a,b){const c=d=>{const e=()=>{if(!a.I)try{a.P.rb(b,d??void 0)}catch(g){var f=new T("PlayerProxy error when creating global callback",{error:g.message,event:b,playerId:a.A,data:d,originalStack:g.stack,componentStack:g.se});f.level="WARNING";throw f;}};
if(qC(a,"web_player_publish_events_immediately"))e();else{const f=setTimeout(()=>{e();var g=a.G,h=String(f);h in g&&delete g[h]},0);
ih(a.G,String(f))}};
return a.h[b]=c}
var AC=class extends y{constructor(a,b,c,d){super();this.A=b;this.webPlayerContextConfig=d;this.Fa=!1;this.api={};this.la=this.u=null;this.P=new L;this.h={};this.Z=this.qa=this.elementId=this.Ja=this.config=null;this.Y=!1;this.j=this.F=null;this.Ba={};this.Ob=["onReady"];this.lastError=null;this.Wa=NaN;this.G={};this.ga=0;this.i=this.o=a;Ob(this,this.P);jC(this);c?this.ga=setTimeout(()=>{this.loadNewVideoConfig(c)},0):d&&(kC(this),lC(this))}getId(){return this.A}loadNewVideoConfig(a){if(!this.I){this.ga&&
(clearTimeout(this.ga),this.ga=0);
var b=a||{};b instanceof lx||(b=new lx(b));this.config=b;this.setConfig(a);lC(this);this.isReady()&&vC(this)}}setConfig(a){this.Ja=a;this.config=rC(a);kC(this);this.qa||(this.qa=wC(this,this.config.args?.jsapicallback||"onYouTubePlayerReady"));this.config.args?this.config.args.jsapicallback=null:this.config.args={jsapicallback:null};if(this.config?.attrs){a=this.config.attrs;const b=a.width;b&&this.i&&(this.i.style.width=Gl(Number(b)||b));(a=a.height)&&this.i&&(this.i.style.height=Gl(Number(a)||a))}}isReady(){return this.Fa}addEventListener(a,
b){const c=wC(this,b);c&&(gb(this.Ob,a)>=0||this.h[a]||(b=zC(this,a),this.u&&this.u(a,b)),this.P.subscribe(a,c),a==="onReady"&&this.isReady()&&setTimeout(()=>{c(this.api)},0))}removeEventListener(a,b){this.I||(b=wC(this,b))&&this.P.unsubscribe(a,b)}getPlayerType(){return this.Z||(nC(this)?"html5":null)}getLastError(){return this.lastError}cancel(){this.F&&Ax(sC(this),this.F);
clearTimeout(this.Wa);this.Y=!1}ba(){pC(this);if(this.j&&this.config&&this.j.destroy)try{this.j.destroy()}catch(b){var a=new T("PlayerProxy error during disposal",{error:b});a.level="ERROR";throw a;}this.Ba=null;for(a in this.h)this.h.hasOwnProperty(a)&&delete this.h[a];this.Ja=this.config=this.api=null;delete this.o;delete this.i;super.ba()}};const BC={},CC="player_uid_"+(Math.random()*1E9>>>0);function DC(a,b){var c="player";c=typeof c==="string"?rh(c):c;const d=`${CC}_${na(c)}`;let e=BC[d];e=new AC(c,d,a,b);BC[d]=e;e.addOnDisposeCallback(()=>{delete BC[e.getId()]});
return e.api}
;let WB=null,EC=null,XB;function FC(a){WB=a;WB.addEventListener("onVideoDataChange",GC);WB.addEventListener("onReady",HC);a=P("POST_MESSAGE_ID","player");const b=P("POST_MESSAGE_ORIGIN");P("ENABLE_JS_API")?EC=new ZB:P("ENABLE_POST_API")&&typeof a==="string"&&typeof b==="string"&&(EC=new fC(a,b));XB=void 0}
function IC(){By();S("ytidb_create_logger_embed_killswitch")||Qq();qB.h||(qB.h=new qB);qB.h.install({flush_logs:{callback:()=>{Qv()}}});
Yq||iu();BB();Kl.va(()=>{QA()});
const a=I("att_init_delay",200);S("enable_rta_manager")&&setTimeout(()=>{S("attmusi")&&aB(window);var b=new Xz;var c={preload:!S("enable_rta_npi"),Pd:S("attmusi")};c=c??{preload:!0};const d=c.Zh?void 0:new Zt;Sz.instance=new Sz(b,c,d);b=Sz.instance;if((S("attmusi")||S("attmusiw"))&&S("attmusi_ue")){b={s:b.o.bind(b),ir:b.u.bind(b)};c=window;c.attmp=b;if(c.attmq!==void 0)for(var e of c.attmq)e(b);c.attmq=void 0}else e=b.o.bind(b),v("yt.aba.att",e),e=b.u.bind(b),v("yt.aba.att2",e)},a);
dq(()=>{if(S("enable_zw_ping")){var b=P("INNERTUBE_CLIENT_NAME","UNKNOWN_INTERFACE"),c="/establish_zw";b==="WEB_EMBEDDED_PLAYER"?c="/embed/establish_zw":b==="TVHTML5"&&(c="https://www.youtube.com/tv/establish_zw");P("COOKIELESS",!1)&&b==="WEB_EMBEDDED_PLAYER"?(b=new Headers,b.set("X-Goog-Visitor-Id",P("VISITOR_DATA")),fetch(c,{method:"GET",mode:"no-cors",headers:b})):fetch(c,{method:"GET",mode:"no-cors",credentials:"include"})}})}
function JC(){Gz();const a=Qp();var b=Tp(119),c=window.devicePixelRatio>1;if(document.body&&Vl(document.body,"exp-invert-logo"))if(c&&!Vl(document.body,"inverted-hdpi")){var d=document.body;if(d.classList)d.classList.add("inverted-hdpi");else if(!Vl(d,"inverted-hdpi")){const f=Tl(d);Ul(d,f+(f.length>0?" inverted-hdpi":"inverted-hdpi"))}}else!c&&Vl(document.body,"inverted-hdpi")&&Wl();if(b!=c){b=`f${Math.floor(119/31)+1}`;d=Up(b)||0;d=c?d|67108864:d&-67108865;d===0?delete Pp[b]:(c=d.toString(16),Pp[b]=
c.toString());b=!0;S("web_secure_pref_cookie_killswitch")&&(b=!1);c=a.h;d=[];for(e in Pp)Pp.hasOwnProperty(e)&&d.push(`${e}=`+encodeURIComponent(String(Pp[e])));var e=d.join("&");Lp(c,e,63072E3,a.i,b)}}
function GC(){KC()}
function HC(){Az("ep_init_pr");KC()}
function KC(){var a=WB.getVideoData(1);a=a.title?a.title+" - YouTube":"YouTube";document.title!==a&&(document.title=a)}
function LC(){WB&&WB.sendAbandonmentPing&&WB.sendAbandonmentPing();P("PL_ATT")&&gC.dispose();var a=Kl;for(let b=0,c=yy.length;b<c;b++)a.wa(yy[b]);yy.length=0;yx(zy.toString());Ay=!1;Ao("DCLKSTAT",0);Nb(EC);WB&&(WB.removeEventListener("onVideoDataChange",GC),WB.destroy(),WB=null)}
;Az("ep_init_eps");v("yt.setConfig",Ao);v("yt.config.set",Ao);v("yt.setMsg",vx);v("yt.msgs.set",vx);v("yt.logging.errors.log",kw);
v("writeEmbed",function(){Az("ep_init_wes");var a=P("PLAYER_CONFIG");if(!a){var b=P("PLAYER_VARS");b&&(a={args:b})}my(!0);a.args.ps==="gvn"&&(document.body.style.backgroundColor="transparent");a.attrs||(a.attrs={width:"100%",height:"100%",id:"video-player"});b=document.referrer;window!==window.top&&b&&b!==document.URL&&(a.args.loaderUrl=b);b=P("WEB_PLAYER_CONTEXT_CONFIGS")?.WEB_PLAYER_CONTEXT_CONFIG_ID_EMBEDDED_PLAYER;if(!b.serializedForcedExperimentIds){const c=No(window.location.href);c.forced_experiments&&
(b.serializedForcedExperimentIds=c.forced_experiments)}a.args?.autoplay?vz("watch",["pbs","pbu","pbp"]):a.args&&Yw(a.args)?vz("video_preview",["ol"]):vz("embed_no_video",["ep_init_ar"]);S("embeds_use_player_instances_library")||P("ENABLE_WEBVIEW_API")?(DB(document.getElementById("player"),b,c=>{P("ENABLE_WEBVIEW_API")?(c=c.getTrustedApi(),FB(c),KB(c)):FC(c)},()=>{throw Error("Unable to load player JS");
},a.args),P("ENABLE_WEBVIEW_API")||IC()):(a=DC(a,b),FC(a),IC());
Az("ep_init_wee")});
v("yt.abuse.player.botguardInitialized",w("yt.abuse.player.botguardInitialized")||hC);v("yt.abuse.player.invokeBotguard",w("yt.abuse.player.invokeBotguard")||iC);v("yt.abuse.dclkstatus.checkDclkStatus",w("yt.abuse.dclkstatus.checkDclkStatus")||Cy);v("yt.player.exports.navigate",w("yt.player.exports.navigate")||ly);v("yt.util.activity.init",w("yt.util.activity.init")||wu);v("yt.util.activity.getTimeSinceActive",w("yt.util.activity.getTimeSinceActive")||Au);
v("yt.util.activity.setTimestamp",w("yt.util.activity.setTimestamp")||xu);window.addEventListener("load",R(function(){JC()}));
window.addEventListener("pageshow",R(function(a){a.persisted||JC()}));
window.addEventListener("pagehide",R(function(a){S("embeds_web_enable_dispose_player_if_page_not_cached_killswitch")?LC():a.persisted||LC()}));
v("yt.logging.errors.log",kw);hb(P("ERRORS")||[],a=>{kw.apply(null,a)});
Ao("ERRORS",[]);zp(wp(),{});
window.onerror=function(a,b="Unknown file",c=0,d,e,f){var g=!1,h=Bo("log_window_onerror_fraction");if(h&&Math.random()<h)g=!0;else{h=document.getElementsByTagName("script");for(let k=0,l=h.length;k<l;k++)if(h[k].src.indexOf("/debug-")>0){g=!0;break}}g&&(g=!1,e?g=!0:(typeof a==="string"?h=a:ErrorEvent&&a instanceof ErrorEvent?(g=!0,h=a.message,b=a.filename,c=a.lineno,d=a.colno):(h="Unknown error",b="Unknown file",c=0),e=new T(h),e.name="UnhandledWindowError",e.message=h,e.fileName=b,e.lineNumber=c,
isNaN(d)?delete e.columnNumber:e.columnNumber=d),S("wiz_enable_component_stack_propagation_killswitch")||(a=e,f?.componentStack||!(a=a.se))||(f||(f={}),f.componentStack=a),f&&sw(e,f),g?kw(e):W(e))};
vj=lw;window.addEventListener("unhandledrejection",a=>{if(a.reason instanceof Error){const b=a.reason;sw(b,{source:"unhandledrejection"});b.name==="AbortError"&&(b.level="WARNING")}lw(a.reason);a.preventDefault()});
(function(){if(P("ENABLE_JS_API")){var a=b=>{XB=b;window.removeEventListener("message",a)};
window.addEventListener("message",a)}})();
Az("ep_init_epe");}).call(this);
