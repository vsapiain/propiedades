var nice = !1;
! function(e) {
    "use strict";
    var a = HOUZEZ_ajaxcalls_vars.houzez_rtl,
        t = HOUZEZ_ajaxcalls_vars.houzez_date_language,
        s = HOUZEZ_ajaxcalls_vars.currency_position,
        n = HOUZEZ_ajaxcalls_vars.stripe_page,
        i = HOUZEZ_ajaxcalls_vars.twocheckout_page;
    a = "yes" == a;
    var o = e("#detail-slider");
    o.length && o.owlCarousel({
        loop: !0,
        autoWidth: !0,
        dots: !1,
        autoplayHoverPause: !0,
        items: 1,
        smartSpeed: 700,
        slideBy: 1,
        nav: !0,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
    });
    var l = e(".clickToShow").text().substring(0, 6);
    e(".clickToShow").hide().after('<span class="clickToShowButton">' + l + "........"), e(".clickToShowButton").click(function(a) {
        a.preventDefault(), e(".clickToShow").show(), e(".clickToShowButton").hide()
    });
    var r = e(".clickToShowPhone").text().substring(0, 6);
    e(".clickToShowPhone").hide().after('<span class="clickToShowButtonPhone">' + r + "........"), e(".clickToShowButtonPhone").click(function(a) {
        a.preventDefault(), e(".clickToShowPhone").show(), e(".clickToShowButtonPhone").hide()
    });
    var c = /Chrome/.test(navigator.userAgent) && /Google Inc/.test(navigator.vendor);
    /Safari/.test(navigator.userAgent) && /Apple Computer/.test(navigator.vendor);

    function h(a) {
        e(a).attr("checked") ? e(a).parents(".method-row").next(".method-option").slideDown() : e(a).parents(".method-row").next(".method-option").slideUp()
    }
    e(window).on("load", function() {
        e(".body-splash").length > 0 && e(".body-splash").addClass("loaded")
    }), e(".map-zoom-actions #houzez-gmap-full").on("click", function() {
        1 == e(this).hasClass("active") ? (e(this).removeClass("active").children("span").text("Fullscreen"), e(this).children("i").removeClass("fa-square-o").addClass("fa-arrows-alt"), e("#houzez-gmap-main").removeClass("mapfull"), e(".header-media").delay(1e3).queue(function(a) {
            e(".header-media").css("height", "auto"), a()
        })) : (e(".header-media").height(e("#houzez-gmap-main").height()), e(this).addClass("active").children("span").text("Default"), e(this).children("i").removeClass("fa-arrows-alt").addClass("fa fa-square-o"), e("#houzez-gmap-main").addClass("mapfull"))
    }), e(".panel-btn, .panel-btn-close").on("click", function() {
        e(".compare-panel").hasClass("panel-open") ? e(".compare-panel").removeClass("panel-open") : e(".compare-panel").addClass("panel-open")
    }), e(".method-select input").on("change", function() {
        e(this).is(":checked") ? (e(".method-option").slideUp(), e(this).parents(".method-row").next(".method-option").slideDown()) : e(".method-option").slideUp()
    }), h(".payment-paypal"), h(".payment-stripe"), e("button.stripe-button-el span").prepend('<i class="fa fa-credit-card"></i>'), e("#stripe_package_recurring").click(function() {
        e(this).attr("checked") ? e(".houzez_payment_form").append('<input type="hidden" name="houzez_stripe_recurring" id="houzez_stripe_recurring" value="1">') : e("#houzez_stripe_recurring").remove()
    }), e("input[name='houzez_payment_type']").click(function() {
        var a = e(this).parents("form");
        "2checkout" === e(this).val() ? (a.attr("action", i), e("#houzez_complete_membership, #houzez_complete_order").addClass("hidden"), e("#houzez_complete_membership_2checkout, #houzez_complete_order_2checkout").removeClass("hidden")) : (a.attr("action", n), e("#houzez_complete_membership, #houzez_complete_order").removeClass("hidden"), e("#houzez_complete_membership_2checkout, #houzez_complete_order_2checkout").addClass("hidden"))
    }), e(".btn-number").click(function(a) {
        a.preventDefault();
        var t = e(this).attr("data-field"),
            s = e(this).attr("data-type"),
            n = e("input[name='" + t + "']"),
            i = parseInt(n.val());
        isNaN(i) ? n.val(0) : "minus" == s ? (i > n.attr("min") && n.val(i - 1).change(), parseInt(n.val()) == n.attr("min") && e(this).attr("disabled", !0)) : "plus" == s && (i < n.attr("max") && n.val(i + 1).change(), parseInt(n.val()) == n.attr("max") && e(this).attr("disabled", !0))
    }), e(".input-number").focusin(function() {
        e(this).data("oldValue", e(this).val())
    }), e(".input-number").change(function() {
        var a = parseInt(e(this).attr("min")),
            t = parseInt(e(this).attr("max")),
            s = parseInt(e(this).val()),
            n = e(this).attr("name");
        s >= a ? e(".btn-number[data-type='minus'][data-field='" + n + "']").removeAttr("disabled") : (alert("Sorry, the minimum value was reached"), e(this).val(e(this).data("oldValue"))), s <= t ? e(".btn-number[data-type='plus'][data-field='" + n + "']").removeAttr("disabled") : (alert("Sorry, the maximum value was reached"), e(this).val(e(this).data("oldValue")))
    }), e(".input-number").keydown(function(a) {
        -1 !== e.inArray(a.keyCode, [46, 8, 9, 27, 13, 190]) || 65 == a.keyCode && !0 === a.ctrlKey || a.keyCode >= 35 && a.keyCode <= 39 || (a.shiftKey || a.keyCode < 48 || a.keyCode > 57) && (a.keyCode < 96 || a.keyCode > 105) && a.preventDefault()
    });
    var d = e("#header-section").data("sticky"),
        p = e("#header-section .header-bottom").data("sticky"),
        u = e(".advance-search-header").data("sticky"),
        g = (e(".top-bar").length, e("#header-section").innerHeight()),
        m = e(".advance-search-header").innerHeight(),
        v = e("#header-section .header-bottom").innerHeight(),
        f = 0;
    1 == d && (f = g), 1 == u && (f = m), 1 == p && (f = v), e("#header-section").hasClass("header-section-3") && (f = v), e("#header-section").hasClass("header-section-2") && (f = v), e(document).ready(function() {
        var a = e("#wpadminbar");
        a.length && (f += a.outerHeight())
    });
    var w = e(".scrolltop-btn");
    e(window).on("scroll", function() {
        e(this).scrollTop() > 100 ? w.fadeIn(1e3) : w.fadeOut(1e3)
    }), e(".back-top").on("click", function() {
        return e("html, body").animate({
            scrollTop: 0
        }, "slow"), !1
    });
    var b, C, y = e(".property-menu-wrap").innerHeight();

    function _() {
        if (e(".header-media .banner-parallax").length) {
            var a = e(".header-media").offset().top + 15,
                t = e(window).scrollTop() - a;
            e(window).scrollTop() >= a ? e(".banner-bg-wrap").css("transform", "translate3d(0," + -.3 * -t + "px,0)") : e(window).scrollTop() < a && e(".banner-bg-wrap").css("transform", "translate3d(0,0px,0)")
        }
    }

    function x(a) {
        e(a + " .login-tabs > li").on("click", function() {
            1 != e(this).hasClass("active") && (e(".login-tabs > li").removeClass("active"), e(this).addClass("active"), e(a + " .login-block .tab-pane").removeClass("in active"), e(a + " .login-block .tab-pane").eq(e(this).index()).addClass("in active"))
        })
    }
    e(".property-menu-wrap").length && (e(".target").each(function() {
        e(this).on("click", function(a) {
            var t = e(this).attr("href"),
                s = e(t).offset().top;
            s = s - f - (y - 2), e("html, body").animate({
                scrollTop: s
            }, {
                duration: 1e3,
                easing: "easeInOutExpo",
                queue: !1
            }), a.preventDefault()
        })
    }), e(window).on("scroll", function() {
        e(".target-block").each(function() {
            if (e(window).scrollTop() >= e(this).offset().top - f - y) {
                var a = e(this).attr("id");
                e(".target").removeClass("active"), e(".target[href=#" + a + "]").addClass("active")
            } else e(window).scrollTop() <= 0 && e(".target").removeClass("active")
        })
    }), e(window).on("scroll", function() {
        e(window).scrollTop() >= e(".detail-media").offset().top + 200 ? e(".property-menu-wrap").css({
            top: f
        }).fadeIn() : e(window).scrollTop() <= e(".detail-media").offset().top + 200 && e(".property-menu-wrap").css({
            top: f
        }).fadeOut()
    })), e(function() {
        e('#header-section a[href*="#"]:not([href="#"])').click(function() {
            if (location.pathname.replace(/^\//, "") == this.pathname.replace(/^\//, "") && location.hostname == this.hostname) {
                var a = e(this.hash);
                if ((a = a.length ? a : e("[name=" + this.hash.slice(1) + "]")).length) return e("html, body").animate({
                    scrollTop: a.offset().top
                }, 1e3), !1
            }
        })
    }), e("#commentform input.submit").addClass("btn btn-primary"), e(".widget_nav_menu, .widget_pages").addClass("widget-pages"), e(".footer-widget.widget_mc4wp_form_widget").addClass("widget-newsletter"), e(".blog-article .pagination-main ul.pagination a").wrap("<li></li>"), e(".houzez_sticky").theiaStickySidebar({
        additionalMarginTop: (b = f, C = f, e(".property-menu-wrap").length && (C = b + e(".property-menu-wrap").innerHeight()), C),
        minWidth: 768,
        updateSidebarHeight: !1
    }), e("#houzez_mortgage_calculate").length > 0 && e("#houzez_mortgage_calculate").click(function(a) {
        a.preventDefault();
        var t, n, i, o, l, r, c, h = HOUZEZ_ajaxcalls_vars.monthly_payment,
            d = HOUZEZ_ajaxcalls_vars.weekly_payment,
            p = HOUZEZ_ajaxcalls_vars.bi_weekly_payment,
            u = HOUZEZ_ajaxcalls_vars.currency_symbol;
        r = e("#mc_payment_period").val(), n = e("#mc_total_amount").val().replace(/,/g, "") - e("#mc_down_payment").val().replace(/,/g, ""), t = parseInt(e("#mc_term_years").val(), 10) * r, l = (o = n * ((i = parseFloat(e("#mc_interest_rate").val(), 10) / (100 * r)) / (1 - Math.pow(1 + i, -t)))) * r, "12" == r ? c = h : "26" == r ? c = p : "52" == r && (c = d), "after" == s ? (e("#mortgage_mwbi").html("<h3>" + c + ":<span> " + Math.round(100 * o) / 100 + u + "</span></h3>"), e("#amount_financed").html(Math.round(100 * n) / 100 + u), e("#mortgage_pay").html(Math.round(100 * o) / 100 + u), e("#annual_cost").html(Math.round(100 * l) / 100 + u)) : (e("#mortgage_mwbi").html("<h3>" + c + ":<span> " + u + Math.round(100 * o) / 100 + "</span></h3>"), e("#amount_financed").html(u + Math.round(100 * n) / 100), e("#mortgage_pay").html(u + Math.round(100 * o) / 100), e("#annual_cost").html(u + Math.round(100 * l) / 100)), e("#total_mortgage_with_interest").html(), e(".morg-detail").show()
    }), e(".input_date").length > 0 && e(".input_date").datepicker(jQuery.datepicker.regional[t]), e(".search-date").length > 0 && e(".search-date").datepicker(jQuery.datepicker.regional[t]), _(), e(window).scroll(function(e) {
        _()
    }), e("a[data-fancy^='property_video']").length > 0 && e("a[data-fancy^='property_video']").prettyPhoto({
        allow_resize: !0,
        default_width: 1900,
        default_height: 1e3,
        animation_speed: "normal",
        theme: "default",
        slideshow: 3e3,
        autoplay_slideshow: !1
    }), e("a[data-fancy^='property_gallery']").length > 0 && e("a[data-fancy^='property_gallery']").prettyPhoto({
        allow_resize: !0,
        default_width: 1900,
        default_height: 1e3,
        animation_speed: "normal",
        theme: "facebook",
        slideshow: 3e3,
        autoplay_slideshow: !1
    }), e("#property_name").keyup(function() {
        var a = e(this).val(),
            t = 0;
        e(".my-property-listing .item-wrap").each(function() {
            e(this).text().search(new RegExp(a, "i")) < 0 ? e(this).fadeOut() : (e(this).show(), t++)
        });
        e(".my-property-search button").text(t)
    }), e(".banner-search-tabs .search-tab").on("click", function() {
        1 != e(this).hasClass("active") && (e(".banner-search-tabs .search-tab").removeClass("active"), e(this).addClass("active"), e(".banner-search-taber .tab-pane").removeClass("active in"), e(".banner-search-taber .tab-pane").eq(e(this).index()).addClass("active").delay(5).queue(function(a) {
            e(this).addClass("in"), a()
        }))
    }), e(".detail-tabs > li").on("click", function() {
        1 != e(this).hasClass("active") && (e(".detail-tabs > li").removeClass("active"), e(this).addClass("active"), e(".detail-content-tabber .tab-pane").removeClass("active in"), e(".detail-content-tabber .tab-pane").eq(e(this).index()).addClass("active in"))
    }), e(".plan-tabs > li").on("click", function() {
        1 != e(this).hasClass("active") && (e(".plan-tabs > li").removeClass("active"), e(this).addClass("active"), e(".plan-tabber .tab-pane").removeClass("active in"), e(".plan-tabber .tab-pane").eq(e(this).index()).addClass("active in"))
    }), e(".houzez-tabs > li").on("click", function() {
        1 != e(this).hasClass("active") && (e(".houzez-tabs > li").removeClass("active"), e(this).addClass("active"), e(".houzez-taber-body .tab-pane").removeClass("active in"), e(".houzez-taber-body .tab-pane").eq(e(this).index()).addClass("active").delay(50).queue(function(a) {
            e(this).addClass("in"), a()
        }))
    }), e(".profile-tabs > li").on("click", function() {
        1 != e(this).hasClass("active") && (e(".profile-tabs > li").removeClass("active"), e(this).addClass("active"), e(".profile-tab-pane").removeClass("active in"), e(".profile-tab-pane").eq(e(this).index()).addClass("active in"))
    }), x(".widget"), x(".footer-widget"), x(".modal"), e(".add-title-tab > .add-expand").click(function() {
        e(this).toggleClass("active"), e(this).parent().next(".add-tab-content").slideToggle()
    }), e(".accord-tab").click(function() {
        e(".accord-tab").not(this).removeClass("active"), e(this).toggleClass("active"), e(".accord-tab").not(this).next(".accord-content").slideUp(), e(this).next(".accord-content").slideToggle()
    }), e('a[data-toggle="tab"]').on("shown.bs.tab", function(e) {
        e.target, e.relatedTarget
    });
    var k = e("#houzez-simple-map");
    if (k.length) {
        k.data("styles");
        e("#mapTab").click(function() {
            document.getElementById("houzez-simple-map").style.display = "block", H()
        });
        var z = null,
            I = {
                center: new google.maps.LatLng(k.data("latitude"), k.data("longitude")),
                zoom: k.data("zoom")
            },
            H = function() {
                z = new google.maps.Map(document.getElementById("houzez-simple-map"), I);
                var e = {
                    lat: k.data("latitude"),
                    lng: k.data("longitude")
                };
                new google.maps.Marker({
                    position: e,
                    map: z
                })
            }
    }

    function T() {
        e(".navi ul li").each(function() {
            e(this).has("ul").not(".houzez-megamenu li").addClass("has-child")
        }), e(".navi ul .has-child").hover(function() {
            e(this).addClass("active")
        }, function() {
            e(this).removeClass("active")
        })
    }

    function S() {
        if (e(window).width() > 991) {
            var a = e(".container"),
                t = e(".header-section,#header-section"),
                s = a.innerWidth(),
                n = e(window).width(),
                i = a.offset();
            e(".navi ul li").hasClass("houzez-megamenu") && e(".navi ul .houzez-megamenu").each(function() {
                e("> .sub-menu", this).wrap("<div class='houzez-megamenu-inner'></div>");
                var a = e(this).offset();
                t.children(".container").length > 0 ? e("> .houzez-megamenu-inner", this).css({
                    width: s,
                    left: -(a.left - i.left)
                }) : e("> .houzez-megamenu-inner", this).css({
                    width: n,
                    left: -a.left
                })
            })
        }
    }
    e(".selectpicker").length > 0 && e(".selectpicker").selectpicker({
        dropupAuto: !1
    }), e(window).on("load", function() {
        e(".grid-block").length > 0 && e(".grid-block").isotope({
            itemSelector: ".grid-item",
            horizontalOrder: !0
        })
    }), 1 == ("ontouchstart" in window || window.DocumentTouch && document instanceof DocumentTouch) == !1 && e('[data-toggle="tooltip"]').tooltip(), e(".actions li").on("click", function() {
        e(this).children(".share_tooltip").hasClass("in") ? e(this).children(".share_tooltip").removeClass("in") : (e(".actions li").children(".share_tooltip").removeClass("in"), e(this).children(".share_tooltip").addClass("in"))
    }), e(document).mouseup(function(a) {
        var t = e(".share-btn");
        t.is(a.target) || 0 !== t.has(a.target).length || e(".share_tooltip").removeClass("in")
    }), e(".grid").length > 0 && e(".grid").each(function() {
        e(this).children().find("img").matchHeight({
            byRow: !0,
            property: "height",
            target: null,
            remove: !1
        })
    }), T(), S(), e(window).on("resize", function() {
        S()
    }), e(window).bind("load", function() {
        S()
    }), e(".view-btn").on("click", function() {
        e(".view-btn").removeClass("active"), e(this).addClass("active"), e(this).hasClass("btn-list") ? e(".property-listing").removeClass("grid-view grid-view-3-col").addClass("list-view") : e(this).hasClass("btn-grid") ? e(".property-listing").removeClass("list-view grid-view-3-col").addClass("grid-view") : e(this).hasClass("btn-grid-3-col") && e(".property-listing").removeClass("list-view grid-view").addClass("grid-view grid-view-3-col")
    });
    var U = e(".top-bar"),
        Z = e("#header-section"),
        O = Z.find(".header-bottom"),
        j = e(".advance-search-header"),
        q = e(".header-mobile"),
        D = e(".advanced-search-mobile"),
        B = e(".header-section").outerHeight(),
        M = Z.outerHeight(),
        E = e(".splash-footer").outerHeight(),
        A = j.outerHeight(),
        P = U.outerHeight(),
        W = q.outerHeight(),
        F = D.outerHeight(),
        R = Z.data("sticky"),
        Q = O.data("sticky"),
        V = q.data("sticky");

    function K(a) {
        a.outerHeight();
        var t = a.clone().removeAttr("style").removeClass("houzez-header-transparent nav-left"),
            s = t.attr("class");
        e(t).hasClass("header-bottom") && (s = e(".header-bottom").parent("#header-section").attr("class"));
        var n = e(t).wrap("<div class='sticky_nav'></div>").parent().addClass(s);

        function i() {
            if (e("#wpadminbar").length > 0 && ee() > 600) {
                var a = e("#wpadminbar").outerHeight();
                n.css("top", a)
            } else n.css("top", "0")
        }
        e("body").append(n), e(n).hasClass("header-section-4") && e(".sticky_nav .logo-desktop img").attr("src", HOUZEZ_ajaxcalls_vars.simple_logo), e(window).on("scroll", function() {
            if (e("#wpadminbar").length > 0 && ee() > 600) {
                var a = e("#wpadminbar").outerHeight();
                n.css("top", a)
            }
            e(window).scrollTop() >= 600 ? n.addClass("sticky-on") : n.removeClass("sticky-on")
        }), i(), e(window).resize(function() {
            i()
        }), S(), T()
    }

    function L() {
        var a = null,
            t = null,
            s = null;
        ee() > 991 ? (a = e(".advance-search-header"), t = e(".advance-search-header").outerHeight()) : (a = e(".advanced-search-mobile"), t = e(".advanced-search-mobile").outerHeight()), a.data("sticky") && (e(".splash-search")[0] ? (s = e(".splash-search").offset().top, s += 200) : s = ee() > 991 ? e(".advance-search-header").offset().top + 65 : e(".advanced-search-mobile").offset().top, 0 == s && (s = e("#header-section").height()), e(window).scroll(function() {
            var n = e(window).scrollTop(),
                i = e("#wpadminbar").height() + "px";
            "nullpx" == i && (i = "0px"), n >= s ? (a.addClass("visible-scroll") ,a.addClass("advanced-search-sticky"), a.css("top", i), e("#section-body").css("padding-top", t),e(".advanced-search-mobile").addClass("none-visible-scroll")) : ( a.removeClass("visible-scroll"),a.addClass("none-visible-scroll") ,e(".advanced-search-mobile").addClass("none-visible-scroll") ,a.removeClass("advanced-search-sticky"), a.removeAttr("style"), e("#section-body").css("padding-top", 0) ),n>100?(e(".advanced-search-mobile").css("top","0px"),e(".advanced-search-mobile").css("display","block")):(e(".advanced-search-mobile").css("top","60px"),e(".advanced-search-mobile").css("display","none"));
        }))

        if (ee() < 991){
            e(".advanced-search-mobile").css("top","60px");
            e(".advanced-search-mobile").addClass("advanced-search-sticky");
        }else{
            e(".advanced-search-mobile").removeClass("advanced-search-sticky");
        }

    }

    function N() {
        var a = e(".search-panel .search-bottom").outerHeight();
        e(".search-scroll").css("padding-bottom", a), e(window).width() < 991 && e(".search-panel").removeClass("panel-open")
    }

    function G(e, a) {
        var t, s = a;
        if (s && (s = s.match(/^url\("?(.+?)"?\)$/))[1]) return s = s[1], (t = new Image).src = s, "height" == e ? t.height : t.width
    }
    1 === Q && K(O), 1 === R && K(Z), 1 === V && K(q), L(), e(".search-panel-btn").on("click", function() {
        e(".search-panel").hasClass("panel-open") ? e(".search-panel").removeClass("panel-open") : e(".search-panel").addClass("panel-open")
    }), N(), e(window).on("resize", function() {
        N()
    });
    var $ = 0,
        J = 0;

    function X() {
        var a = e(window).innerHeight(),
            t = e("#wpadminbar"),
            s = t.outerHeight();
        J = a - B - E, c ? e(".fave-screen-fix-inner").css("height", J - 1) : e(".fave-screen-fix-inner").css("height", J), ee() >= 992 ? (Z.length && ($ = M), Z.length && j.length && !j.hasClass("search-hidden") && ($ = parseInt(A) + parseInt(M)), Z.is("*") && j.hasClass("search-hidden") && ($ = M), Z.length && U.length && ($ = parseInt(M) + parseInt(P)), Z.length && j.length && !j.hasClass("search-hidden") && U.length && ($ = parseInt(M) + parseInt(P) + parseInt(A)), Z.length && t.length && ($ = parseInt(M) + parseInt(s)), Z.length && t.length && U.length && ($ = parseInt(M) + parseInt(s) + parseInt(P)), Z.length && t.length && j.length && !j.hasClass("search-hidden") && ($ = parseInt(M) + parseInt(s) + parseInt(A)), Z.length && t.length && j.length && !j.hasClass("search-hidden") && U.length && ($ = parseInt(M) + parseInt(s) + parseInt(A) + parseInt(P)), Z.length && t.length && j.length && j.hasClass("search-hidden") && U.length && ($ = parseInt(M) + parseInt(s) + parseInt(P))) : (D.length && !D.hasClass("search-hidden") && q.length && ($ = parseInt(F) + parseInt(W)), D.hasClass("search-hidden") && q.is("*") && ($ = W), q.length && ($ = W), q.length && U.length && ($ = parseInt(W) + parseInt(P)), q.length && D.length && !D.hasClass("search-hidden") && U.length && ($ = parseInt(W) + parseInt(P) + parseInt(F)), q.length && t.length && ($ = parseInt(W) + parseInt(s)), q.length && t.length && D.length && !D.hasClass("search-hidden") && ($ = parseInt(W) + parseInt(s) + parseInt(F)), q.length && t.length && D.length && !D.hasClass("search-hidden") && U.length && ($ = parseInt(W) + parseInt(s) + parseInt(F) + parseInt(P)), q.length && t.length && D.length && D.hasClass("search-hidden") && U.length && ($ = parseInt(W) + parseInt(s) + parseInt(P)), q.length && t.length && U.length && ($ = parseInt(W) + parseInt(s) + parseInt(P)));
        var n = 0;
        if (n = Z.hasClass("houzez-header-transparent") ? ae() - $ + M : ae() - $, c ? e(".fave-screen-fix").css("height", n - 1) : e(".fave-screen-fix").css("height", n), e(".banner-parallax-fix").css("height", n), ee() > 768) {
            var i = e(".banner-parallax-auto .banner-inner").css("background-image");
            if ("none" != i) {
                var o = e(".banner-parallax-auto").width() * G("height", i) / G("width", i);
                o > ae() ? e(".banner-parallax-auto").css("height", n) : e(".banner-parallax-auto").css("height", o - $)
            } else e(".banner-parallax-auto").css("height", n)
        } else e(".banner-parallax-auto").css("height", 300)
    }

    function Y() {
        var a = e("#wpadminbar"),
            t = e(".board-header"),
            s = e(".steps-nav"),
            n = s.outerHeight(),
            i = a.outerHeight(),
            o = e(window).outerHeight(),
            l = t.outerHeight(),
            r = 0;
        r = o - M, t.length && (t.is(":hidden") ? r = r : r -= l), U.length && (r -= P), a.length && (r -= i), s.length && (r -= n), e(window).width() > 991 ? c ? e(".dashboard-fix").css("height", r - 1) : e(".dashboard-fix").css("height", r) : e(".dashboard-fix").css("height", "100%")
    }

    function ee() {
        return Math.max(e(window).width(), window.innerWidth)
    }

    function ae() {
        return Math.max(e(window).height(), window.innerHeight)
    }
    X(), Y(), e(window).on("resize", function() {
        X(), L(), Y()
    }), e(window).bind("load", function() {
        X(), Y()
    }), e(".search-expand-btn").on("click", function() {
        e(this).toggleClass("active"), 1 == e(this).hasClass("active") ? e(".search-expandable .advanced-search").slideDown() : (e(".search-expandable .advanced-search").add(".search-expandable .advance-fields").slideUp(), e(".advance-btn").removeClass("active"))
    }), e(".advanced-search .advance-btn").on("click", function() {
        e(this).toggleClass("active"), 1 == e(this).hasClass("active") ? e(this).closest(".advanced-search").find(".advance-fields").slideDown() : e(this).closest(".advanced-search").find(".advance-fields").slideUp()
    }), e(".advanced-search-mobile .advance-btn").on("click", function() {
        e(this).toggleClass("active"), 1 == e(this).hasClass("active") ? e(this).closest(".advanced-search-mobile").find(".advance-fields").slideDown() : e(this).closest(".advanced-search-mobile").find(".advance-fields").slideUp()
    }), e(".advance-trigger").on("click", function() {
        e(this).toggleClass("active"), 1 == e(this).hasClass("active") ? (e(this).children("i").removeClass("fa-plus-square").addClass("fa-minus-square"), e(".field-expand").slideDown()) : (e(this).children("i").removeClass("fa-minus-square").addClass("fa-plus-square"), e(".field-expand").slideUp())
    });
    var te, se = e(".owl-carousel");
    (se.on("initialized.owl.carousel", function() {
        setTimeout(function() {
            se.animate({
                opacity: 1
            }, 800), e(".gallery-area .slider-placeholder").remove()
        }, 800)
    }), e("#banner-slider").length > 0) && e("#banner-slider").owlCarousel({
        rtl: a,
        loop: !0,
        dots: !1,
        slideBy: 1,
        autoplay: !0,
        autoplaySpeed: 1e3,
        items: 1,
        smartSpeed: 1e3,
        nav: !0,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        addClassActive: !0,
        callbacks: !0,
        responsive: {
            0: {
                nav: !1,
                dots: !0
            },
            768: {
                nav: !0,
                dots: !1
            }
        }
    });
    if (e("#carousel-post-card").length > 0) {
        var ne = e("#carousel-post-card");
        ne.owlCarousel({
            rtl: a,
            loop: !1,
            dots: !0,
            autoplay: !0,
            autoplaySpeed: 700,
            slideBy: 1,
            nav: !1,
            responsive: {
                0: {
                    items: 1
                },
                320: {
                    items: 1
                },
                480: {
                    items: 1
                },
                768: {
                    items: 2
                },
                1000: {
                    items: 3
                },
                1280: {
                    items: 4
                }
            }
        }), e(".btn-prev-post-card").on("click", function() {
            ne.trigger("prev.owl.carousel", [700])
        }), e(".btn-next-post-card").on("click", function() {
            ne.trigger("next.owl.carousel", [700])
        })
    }
    if (e("#carousel-post-card-block").length > 0) {
        var ie = e("#carousel-post-card-block");
        ie.owlCarousel({
            rtl: a,
            loop: !0,
            dots: !0,
            autoplay: !0,
            autoplaySpeed: 700,
            slideBy: 1,
            nav: !1,
            responsive: {
                0: {
                    items: 1
                },
                320: {
                    items: 1
                },
                480: {
                    items: 1
                },
                768: {
                    items: 2
                },
                1000: {
                    items: 3
                },
                1280: {
                    items: 4
                }
            }
        }), e(".btn-prev-card-block").on("click", function() {
            ie.trigger("prev.owl.carousel", [700])
        }), e(".btn-next-card-block").on("click", function() {
            ie.trigger("next.owl.carousel", [700])
        })
    }
    if (e("#agents-carousel").length > 0) {
        var oe = e("#agents-carousel");
        oe.owlCarousel({
            rtl: a,
            loop: !0,
            dots: !1,
            slideBy: 1,
            autoplay: !0,
            autoplaySpeed: 700,
            nav: !1,
            responsive: {
                0: {
                    items: 1
                },
                320: {
                    items: 1
                },
                480: {
                    items: 1
                },
                768: {
                    items: 2
                },
                1000: {
                    items: 3
                },
                1280: {
                    items: 4
                }
            }
        }), e(".btn-prev-agents").on("click", function() {
            oe.trigger("prev.owl.carousel", [700])
        }), e(".btn-next-agents").on("click", function() {
            oe.trigger("next.owl.carousel", [700])
        })
    }
    if (e("#partner-carousel").length > 0 && (e("#partner-carousel").owlCarousel({
            rtl: a,
            loop: !1,
            dots: !0,
            slideBy: 2,
            autoplay: !0,
            autoplaySpeed: 700,
            nav: !1,
            responsive: {
                0: {
                    items: 1
                },
                320: {
                    items: 1
                },
                480: {
                    items: 3
                },
                768: {
                    items: 4
                },
                992: {
                    items: 4
                }
            }
        }), e(".btn-prev-partners").on("click", function() {
            e("#partner-carousel").trigger("prev.owl.carousel", [700])
        }), e(".btn-next-partners").on("click", function() {
            e("#partner-carousel").trigger("next.owl.carousel", [700])
        })), e("#agency-carousel").length > 0) {
        var le = e("#agency-carousel");
        le.owlCarousel({
            rtl: a,
            loop: !0,
            dots: !0,
            items: 4,
            slideBy: 4,
            nav: !1,
            smartSpeed: 400
        }), e(".btn-crl-agency-prev").on("click", function() {
            le.trigger("prev.owl.carousel", [400])
        }), e(".btn-crl-agency-next").on("click", function() {
            le.trigger("next.owl.carousel", [400])
        })
    }

    function re(a, t) {
        var s = e(a).html();
        e(t).html(s), e(t + " ul li").each(function() {
            e(this).children(".houzez-megamenu-inner").length && e(t + " .houzez-megamenu-inner > ul").unwrap(), e(this).has("ul").addClass("has-child")
        }), e(t + " ul .has-child").append('<span class="expand-me"></span>'), e(t + " .expand-me").on("click", function() {
            var a = e(this).parent("li");
            1 == a.hasClass("active") ? (a.removeClass("active"), a.children("ul").slideUp()) : (a.addClass("active"), a.children("ul").slideDown())
        })
    }

    function ce(a, t) {
        var s = e(".nav-dropdown"),
            n = e(".account-dropdown");
        e(document).mouseup(function(i) {
            var o = e(a);
            o.is(i.target) || 0 !== o.has(i.target).length || s.is(i.target) || 0 !== s.has(i.target).length || n.is(i.target) || 0 !== n.has(i.target).length || e(a).removeClass(t)
        })
    }
    e(".property-widget-slider").length > 0 && e(".property-widget-slider").owlCarousel({
        rtl: a,
        dots: !0,
        items: 1,
        smartSpeed: 700,
        slideBy: 1,
        nav: !0,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"]
    }), e(".prop_featured").change(function() {
        var a, t, s, n = HOUZEZ_ajaxcalls_vars.currency_symbol,
            i = HOUZEZ_ajaxcalls_vars.currency_position,
            o = e(this).parents(".payment-side-block"),
            l = e(this).parents(".houzez-per-listing-buttons-main"),
            r = parseFloat(o.find(".submission_price").text());
        return a = r + parseFloat(o.find(".submission_featured_price").text()), "after" === i ? (s = r + " " + n, t = a + " " + n) : (s = n + " " + r, t = n + " " + a), e(this).is(":checked") ? (o.find(".submission_total_price").text(t), e("#featured_pay").val(1), e('input[name="pay_ammout"]').val(100 * a), e("#houzez_listing_price").val(a), l.find("#stripe_form_simple_listing").hide(), l.find("#stripe_form_featured_listing").show()) : (o.find(".submission_total_price").text(s), e("#featured_pay").val(0), e('input[name="pay_ammout"]').val(100 * r), e("#houzez_listing_price").val(r), l.find("#stripe_form_featured_listing").hide(), l.find("#stripe_form_simple_listing").show()), !1
    }), e(".my-actions .pay-btn").on("click", function(a) {
        1 != e(this).parent().hasClass("open") ? (e(".my-actions .pay-btn").parent().removeClass("open"), e(this).parent().addClass("open")) : e(this).parent().removeClass("open")
    }), e("body").on("click", function(a) {
        e(".my-actions .pay-btn").is(a.target) || 0 !== e(".my-actions .pay-btn").has(a.target).length || 0 !== e(".open").has(a.target).length || e(".my-actions .pay-btn").parent().removeClass("open")
    }), e("#sort_properties").on("change", function() {
        ! function(e, a) {
            e = encodeURI(e), a = encodeURI(a);
            for (var t, s = document.location.search.substr(1).split("&"), n = s.length; n--;)
                if ((t = s[n].split("="))[0] == e) {
                    t[1] = a, s[n] = t.join("=");
                    break
                }
            n < 0 && (s[s.length] = [e, a].join("=")), document.location.search = s.join("&")
        }("sortby", e(this).val())
    }), e(".header-user .account-action > li").on("click", function(a) {
        e(this).hasClass("active") ? e(this).removeClass("active") : e(this).addClass("active")
    }), e(".header-right .account-action > li").on({
        mouseenter: function(a) {
            e(this).addClass("active")
        },
        mouseleave: function(a) {
            e(this).removeClass("active")
        }
    }), re(".main-nav", ".main-nav-dropdown"), re(".top-nav", ".top-nav-dropdown"), e(".nav-trigger").on("click", function() {
        e(this).hasClass("mobile-open") ? e(this).removeClass("mobile-open") : e(this).addClass("mobile-open")
    }), e(".header-single-page").length > 0 && e(".header-single-page .main-nav-dropdown li a").on("click", function(a) {
        e(".nav-trigger").removeClass("mobile-open")
    }), ce(".header-mobile .nav-trigger", "mobile-open"), ce(".top-bar .nav-trigger", "mobile-open"), ce(".account-action > li", "active"), te = ".auto-complete", e(document).mouseup(function(a) {
        e(te).is(a.target) || 0 !== e(te).has(a.target).length || e(te).fadeOut()
    }), e(".show-morg").on("click", function() {
        e(this).hasClass("active") ? (e(".morg-summery").slideUp(), e(this).removeClass("active")) : (e(".morg-summery").slideDown(), e(this).addClass("active"))
    });
    var he = e(".lightbox-slide");
    he.on("resized.owl.carousel", function() {
        var a = e(this);
        a.find(".owl-height").css("height", a.find(".owl-item.active").height())
    });
    var de = e(".lightbox-right").innerWidth();

    function pe() {
        var a = fe() - 60;
        if (e(".lightbox-popup").css("width", a), e(".lightbox-right").length > 0) {
            var t = e(".lightbox-right").innerWidth();
            e(".lightbox-left").css("width", a - t), e(".gallery-inner").css("width", a - t - 40), e(".lightbox-right").addClass("in"), e(".lightbox-left .lightbox-close").removeClass("show"), Modernizr.mq("(max-width: 1199px)") && (e(".expand-icon").removeClass("compress"), e(".popup-inner").removeClass("pop-expand")), Modernizr.mq("(max-width: 1024px)") && (e(".lightbox-left").css("width", "100%"), e(".lightbox-right").removeClass("in"), e(".gallery-inner").css("width", "100%"), e(".expand-icon").addClass("compress"), e(".lightbox-left .lightbox-close").addClass("show"))
        } else e(".lightbox-left").css("width", "100%"), e(".gallery-inner").css("width", "100%"), e(".lightbox-left .lightbox-close").addClass("show")
    }
    e(".popup-trigger").on("click", function() {
        e("#lightbox-popup-main").addClass("active").addClass("in"), he.show(function() {
            he.owlCarousel({
                rtl: a,
                dots: !1,
                items: 1,
                autoPlay: 1200,
                smartSpeed: 1200,
                autoplay: !0,
                autoplayHoverPause: !0,
                slideBy: 1,
                nav: !1,
                stopOnHover: !0,
                autoHeight: !0,
                navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
                responsive: {
                    768: {
                        nav: !0
                    }
                }
            })
        }), e(".lightbox-arrow-left").on("click", function() {
            he.trigger("prev.owl.carousel", [1200])
        }), e(".lightbox-arrow-right").on("click", function() {
            he.trigger("next.owl.carousel", [1200])
        }), e(document).keydown(function(e) {
            37 == e.keyCode ? he.trigger("prev.owl.carousel", [1200]) : 39 == e.keyCode && he.trigger("next.owl.carousel", [1200])
        })
    }), e(".lightbox-close").on("click", function() {
        he.trigger("destroy.owl.carousel"), he.html(he.find(".owl-stage-outer").html()).removeClass("owl-loaded"), e("#lightbox-popup-main").removeClass("active").removeClass("in")
    }), e(document).keydown(function(a) {
        27 == a.keyCode && e("#lightbox-popup-main").removeClass("active").removeClass("in")
    }), pe(), e(".lightbox-expand").on("click", function() {
        e(".lightbox-left .lightbox-close").toggleClass("show");
        var a = fe(),
            t = fe() - 60 - de;
        a >= 1024 && (e(this).hasClass("compress") ? (e(".lightbox-right").addClass("in"), e(".lightbox-left").css("width", t), e(this).removeClass("compress"), e(".popup-inner").removeClass("pop-expand")) : (e(".lightbox-left").css("width", "100%"), e(".lightbox-right").removeClass("in"), e(this).addClass("compress"), e(".popup-inner").addClass("pop-expand"))), a <= 1024 && (e(this).hasClass("compress") ? (e(".lightbox-right").addClass("in"), e(".lightbox-left").css("width", t), e(this).removeClass("compress")) : (e(".lightbox-left").css("width", "100%"), e(".lightbox-right").removeClass("in"), e(this).addClass("compress"))), a < 768 && e(".lightbox-left").css("width", "100%")
    });
    var ue = e(".login-here"),
        ge = e(".register-here"),
        me = e(".step-tab-login"),
        ve = e(".step-tab-register");

    function fe() {
        return Math.max(e(window).width(), e(window).innerWidth())
    }
    e(".step-login-btn a").on("click", function(a) {
        var t = e(this);
        t.hasClass("login-here") ? (t.hide(), ge.show(), me.addClass("in active"), ve.removeClass("in active"), e("#submit_property_form").append('<input type="hidden" name="login_while_submission" id="login_while_submission" value="1">')) : (t.hide(), ue.show(), me.removeClass("in active"), ve.addClass("in active"), e("#login_while_submission").remove()), a.preventDefault()
    }), e(".dsidx-prop-summary").length && (e(".dsidx-prop-summary .dsidx-prop-title").next("div").addClass("item-thumb"), e(".item-thumb a").addClass("hover-effect")), e(".impress-showcase-photo").length && e(".impress-showcase-photo").addClass("hover-effect"), e(window).on("load", function() {
        pe()
    }), e(window).on("resize", function() {
        pe()
    }), e(document).ready(function() {
        e(".tagcloud a").removeAttr("style")
    }), e('[data-toggle="popover"]').popover({
        trigger: "hover",
        html: !0
    }), e(".dropdown-toggle").dropdown()
}(jQuery);