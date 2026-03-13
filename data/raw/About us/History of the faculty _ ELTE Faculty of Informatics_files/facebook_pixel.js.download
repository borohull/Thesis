/**
 * @file
 * facebook_pixel.js
 *
 * Defines the behavior of the facebook pixel module.
 */

(function (Drupal, drupalSettings, once) {

  'use strict';

  function initTracking() {
    var facebook_pixel_id = drupalSettings.facebook_pixel.facebook_id;

    // Define Drupal.facebook_pixel.fb_disable as a dynamic condition to
    // disable FB Pixel at runtime.
    // This is helpful for GDPR compliance module integration
    // and works even with static caching mechanisms like boost module.
    Drupal.facebook_pixel = (typeof Drupal.facebook_pixel !== "undefined") ? Drupal.facebook_pixel : {};
    Drupal.facebook_pixel.fb_disable = false;

    // Define Opt-out conditions check
    if (drupalSettings.facebook_pixel.fb_disable_advanced) {
      // Facebook Pixel Opt-Out Code
      window.fbOptout = function (reload = 0) {
        reload = (typeof reload !== 'undefined') ? reload : 0;
        var optoutWindowDisableKey = 'fb-disable';
        document.cookie = optoutWindowDisableKey + '=true; expires=Thu, 31 Dec 2999 23:59:59 UTC; path=/';
        window[optoutWindowDisableKey] = true;
        if (reload) {
          location.reload();
        }
      };
      if (document.cookie.indexOf('fb-disable=true') > -1) {
        window['fb-disable'] = true;
      }
      // End Facebook Pixel Opt-Out Code
      Drupal.facebook_pixel.fb_disable = Drupal.facebook_pixel.fb_disable || window['fb-disable'] == true;
    }

    // Define eu_cookie_compliance conditions check (https://www.drupal.org/project/eu_cookie_compliance)
    if (drupalSettings.facebook_pixel.eu_cookie_compliance) {
      if (typeof Drupal.eu_cookie_compliance === "undefined") {
        console.warn("facebook_pixel: facebook_pixel eu_cookie_compliance integration option is enabled, but eu_cookie_compliance javascripts seem to be loaded after facebook_pixel, which may break functionality.");
      }
      var eccHasAgreed = (typeof Drupal.eu_cookie_compliance !== "undefined" && Drupal.eu_cookie_compliance.hasAgreed());
      Drupal.facebook_pixel.fb_disable = Drupal.facebook_pixel.fb_disable || !eccHasAgreed;
    }

    // Define Do-not-track conditions check (see https://www.w3.org/TR/tracking-dnt/)
    if (drupalSettings.facebook_pixel.donottrack) {
      var DNT = (typeof navigator.doNotTrack !== "undefined" && (navigator.doNotTrack === "yes" || navigator.doNotTrack == 1)) || (typeof navigator.msDoNotTrack !== "undefined" && navigator.msDoNotTrack == 1) || (typeof window.doNotTrack !== "undefined" && window.doNotTrack == 1);
      // If eccHasAgreed is true, it overrides DNT because eu_cookie_compliance contains a setting for opt-in with DNT:
      // "Automatic. Respect the DNT (Do not track) setting in the browser, if present. Uses opt-in when DNT is 1 or not set, and consent by default when DNT is 0."
      Drupal.facebook_pixel.fb_disable = Drupal.facebook_pixel.fb_disable || (DNT && (typeof eccHasAgreed == "undefined" || !eccHasAgreed));
    }

    if (!Drupal.facebook_pixel.fb_disable) {
      let elements = once('facebook_pixel_pageload_tracking', 'body');
      elements.forEach(function () {
        !function (f,b,e,v,n,t,s) {
        if(f.fbq) { return;
        }n = f.fbq = function () {n.callMethod ?
        n.callMethod.apply(n,arguments):n.queue.push(arguments)};
        if(!f._fbq) { f._fbq = n;
        }n.push = n;n.loaded = !0;n.version = '2.0';
        n.queue = [];t = b.createElement(e);t.async = !0;
        t.src = v;s = b.getElementsByTagName(e)[0];
        s.parentNode.insertBefore(t,s)}(window, document,'script',
        'https://connect.facebook.net/en_US/fbevents.js');
        fbq('init', facebook_pixel_id);
        fbq('track', 'PageView');

        drupalSettings.facebook_pixel.events.forEach(function (event) {
          fbq("track", event['event'], JSON.parse(event['data']));
        });
      });
    }
  }

  Drupal.behaviors.facebook_pixel = {
    attach(context) {
      let elements = once('facebook_pixel_behavior', 'body')
      elements.forEach(function () {
        initTracking();
      });

      document.addEventListener('eu_cookie_compliance.changeStatus', function() {
        initTracking();
      });
    },
  };

}(Drupal, drupalSettings, once));
