// Utility function
function Util () {};

/*
	class manipulation functions
*/
Util.hasClass = function(el, className) {
	if (el.classList) return el.classList.contains(className);
	else return !!el.className.match(new RegExp('(\\s|^)' + className + '(\\s|$)'));
};

Util.addClass = function(el, className) {
	var classList = className.split(' ');
 	if (el.classList) el.classList.add(classList[0]);
 	else if (!Util.hasClass(el, classList[0])) el.className += " " + classList[0];
 	if (classList.length > 1) Util.addClass(el, classList.slice(1).join(' '));
};

Util.removeClass = function(el, className) {
	var classList = className.split(' ');
	if (el.classList) el.classList.remove(classList[0]);
	else if(Util.hasClass(el, classList[0])) {
		var reg = new RegExp('(\\s|^)' + classList[0] + '(\\s|$)');
		el.className=el.className.replace(reg, ' ');
	}
	if (classList.length > 1) Util.removeClass(el, classList.slice(1).join(' '));
};

Util.toggleClass = function(el, className, bool) {
	if(bool) Util.addClass(el, className);
	else Util.removeClass(el, className);
};

Util.setAttributes = function(el, attrs) {
  for(var key in attrs) {
    el.setAttribute(key, attrs[key]);
  }
};

/*
  DOM manipulation
*/
Util.getChildrenByClassName = function(el, className) {
  var children = el.children,
    childrenByClass = [];
  for (var i = 0; i < el.children.length; i++) {
    if (Util.hasClass(el.children[i], className)) childrenByClass.push(el.children[i]);
  }
  return childrenByClass;
};

/*
	Animate height of an element
*/
Util.setHeight = function(start, to, element, duration, cb) {
	var change = to - start,
	    currentTime = null;

  var animateHeight = function(timestamp){
    if (!currentTime) currentTime = timestamp;
    var progress = timestamp - currentTime;
    var val = parseInt((progress/duration)*change + start);
    // console.log(val);
    element.setAttribute("style", "height:"+val+"px;");
    if(progress < duration) {
        window.requestAnimationFrame(animateHeight);
    } else {
    	cb();
    }
  };

  //set the height of the element before starting animation -> fix bug on Safari
  element.setAttribute("style", "height:"+start+"px;");
  window.requestAnimationFrame(animateHeight);
};

/*
	Smooth Scroll
*/

Util.scrollTo = function(final, duration, cb) {
  var start = window.scrollY || document.documentElement.scrollTop,
      currentTime = null;

  var animateScroll = function(timestamp){
  	if (!currentTime) currentTime = timestamp;
    var progress = timestamp - currentTime;
    if(progress > duration) progress = duration;
    var val = Math.easeInOutQuad(progress, start, final-start, duration);
    window.scrollTo(0, val);
    if(progress < duration) {
        window.requestAnimationFrame(animateScroll);
    } else {
      cb && cb();
    }
  };

  window.requestAnimationFrame(animateScroll);
};

/*
  Focus utility classes
*/

//Move focus to an element
Util.moveFocus = function (element) {
  if( !element ) element = document.getElementsByTagName("body")[0];
  element.focus();
  if (document.activeElement !== element) {
    element.setAttribute('tabindex','-1');
    element.focus();
  }
};

/*
  Misc
*/

Util.getIndexInArray = function(array, el) {
  return Array.prototype.indexOf.call(array, el);
};

Util.cssSupports = function(property, value) {
  if('CSS' in window) {
    return CSS.supports(property, value);
  } else {
    var jsProperty = property.replace(/-([a-z])/g, function (g) { return g[1].toUpperCase();});
    return jsProperty in document.body.style;
  }
};

/*
	Polyfills
*/
//Closest() method
if (!Element.prototype.matches) {
	Element.prototype.matches = Element.prototype.msMatchesSelector || Element.prototype.webkitMatchesSelector;
}

if (!Element.prototype.closest) {
	Element.prototype.closest = function(s) {
		var el = this;
		if (!document.documentElement.contains(el)) return null;
		do {
			if (el.matches(s)) return el;
			el = el.parentElement || el.parentNode;
		} while (el !== null && el.nodeType === 1);
		return null;
	};
}

//Custom Event() constructor
if ( typeof window.CustomEvent !== "function" ) {

  function CustomEvent ( event, params ) {
    params = params || { bubbles: false, cancelable: false, detail: undefined };
    var evt = document.createEvent( 'CustomEvent' );
    evt.initCustomEvent( event, params.bubbles, params.cancelable, params.detail );
    return evt;
   }

  CustomEvent.prototype = window.Event.prototype;

  window.CustomEvent = CustomEvent;
}

/*
	Animation curves
*/
Math.easeInOutQuad = function (t, b, c, d) {
	t /= d/2;
	if (t < 1) return c/2*t*t + b;
	t--;
	return -c/2 * (t*(t-2) - 1) + b;
};

(function() {
	var cart = document.getElementsByClassName('js-cd-cart');
	if (cart.length > 0) {
		var cartAddBtns = document.getElementsByClassName('js-cd-add-to-cart'),
			cartBody = cart[0].getElementsByClassName('cd-cart__body')[0],
			cartList = cartBody.getElementsByTagName('ul')[0],
			cartListItems = cartList.getElementsByClassName('cd-cart__product'),
			cartTotal = cart[0].getElementsByClassName('cd-cart__checkout')[0].getElementsByTagName('span')[0],
			cartCount = cart[0].getElementsByClassName('cd-cart__count')[0],
			cartCountItems = cartCount.getElementsByTagName('li'),
			cartUndo = cart[0].getElementsByClassName('cd-cart__undo')[0],
			productId = 0,
			cartTimeoutId = false,
			animatingQuantity = false;
		initCartEvents();

		function initCartEvents() {
		    let itemStorage = sessionStorage.length ;
		    if(sessionStorage.length>0){
		        for(let i=0; i<sessionStorage.length; i++) {
		            let key_ = sessionStorage.key(i);
		            let productAdded =  sessionStorage.getItem(key_);
		            addToCartLoad($(productAdded));
		        }
		    }
			for (var i = 0; i < cartAddBtns.length; i++) {
				(function(i) {
					cartAddBtns[i].addEventListener('click', addToCart);
				})(i);
			}
			cart[0].getElementsByClassName('cd-cart__trigger')[0].addEventListener('click', function(event) {
				event.preventDefault();
				toggleCart();
			});
			cart[0].addEventListener('click', function(event) {
				if (event.target == cart[0]) {
					toggleCart(true);
				} else if (event.target.closest('.cd-cart__delete-item')) {
					event.preventDefault();

					removeProduct(event.target.closest('.cd-cart__product'));
				}
			});
			cart[0].addEventListener('change', function(event) {
				if (event.target.tagName.toLowerCase() == 'select') quickUpdateCart();
			});
			cartUndo.addEventListener('click', function(event) {
				if (event.target.tagName.toLowerCase() == 'a') {
					event.preventDefault();

					if (cartTimeoutId) clearInterval(cartTimeoutId);
					var deletedProduct = cartList.getElementsByClassName('cd-cart__product--deleted')[0];
					Util.addClass(deletedProduct, 'cd-cart__product--undo');
					deletedProduct.addEventListener('animationend', function cb() {
						deletedProduct.removeEventListener('animationend', cb);
						Util.removeClass(deletedProduct, 'cd-cart__product--deleted cd-cart__product--undo');
						deletedProduct.removeAttribute('style');
						quickUpdateCart();
					});

					Util.removeClass(cartUndo, 'cd-cart__undo--visible');
				}
			});

		};
        addDynamicEventListener(document.body, 'click', '.js-cd-add-to-cart', function (event) {
            var ctl =  $('.js-cd-add-to-cart');
            if (cartListItems.length==0)
                toggleCart();
            addToCartDyn(event,ctl);
        });
		function addToCart(event) {
		   event.preventDefault();
		   if (animatingQuantity) return;
            animatingQuantity = true;
            var cartIsEmpty = Util.hasClass(cart[0], 'cd-cart--empty');
            addProduct(this,false)
            updateCartCount(cartIsEmpty);
            updateCartTotal(this.getAttribute('data-price'), true);
            Util.removeClass(cart[0], 'cd-cart--empty');

		};
		function addToCartLoad(ctl) {
		    if (animatingQuantity) return;
            animatingQuantity = true;
            var cartIsEmpty = Util.hasClass(cart[0], 'cd-cart--empty');
            addProduct($(ctl),true);
            updateCartCount(cartIsEmpty);

            var price_ = ctl.find("span").html().replace("$","");
            updateCartTotal(price_, true);
            Util.removeClass(cart[0], 'cd-cart--empty');
		};
		function addToCartDyn(event,ctl) {
		    event.preventDefault();
		    if (animatingQuantity) return;
            animatingQuantity = true;
            var cartIsEmpty = Util.hasClass(cart[0], 'cd-cart--empty');
            let estado = false;
            if (addProduct($(ctl),false))
                estado = true;
            updateCartCountDyn(cartIsEmpty,estado);
            if (estado)
                updateCartTotal($(ctl).attr("data-price"), true);
            Util.removeClass(cart[0], 'cd-cart--empty');
		};

		function toggleCart(bool) {
			var cartIsOpen = (typeof bool === 'undefined') ? Util.hasClass(cart[0], 'cd-cart--open') : bool;
			if (cartIsOpen) {
				Util.removeClass(cart[0], 'cd-cart--open');
				if (cartTimeoutId) clearInterval(cartTimeoutId);
				Util.removeClass(cartUndo, 'cd-cart__undo--visible');
				removePreviousProduct();

				setTimeout(function() {
					cartBody.scrollTop = 0;
					if (Number(cartCountItems[0].innerText) == 0) Util.addClass(cart[0], 'cd-cart--empty');
				}, 500);
			} else {
				Util.addClass(cart[0], 'cd-cart--open');
			}
		};
		function addProduct(target,carga) {
		    estado = false;
		    obj = new Object();
            var productAdded = '<li class="cd-cart__product"><div class="cd-cart__details"><h3 class="truncate"><a href="#0">Cambio plan Oro</a></h3><span class="cd-cart__price">$25.99 </span> <div class="cd-cart__actions"><a href="#0" class="cd-cart__delete-item pull-right"><i class="fa fa-minus-square" aria-hidden="true"></i></a></div></div></li>';
            var insertar = true;
		    if (!carga){
		        let cod = target.attr("id");
		        obj.tipo = cod.substring(0,1);
		        obj.codigo = cod.substring(1);
		        obj.nombre = '';
		        obj.precio = '';
		        obj = cargarDetalle(obj);

		        //tipo planes
                if (obj.tipo == 1){
                    $(".cd-cart__body li").each(function(index){
                        let id_aux = $(this).children().attr("id");
                        if (id_aux.replace("det_","") == cod)
                            insertar = false;
                    });
                }
		        productAdded = '<li class="cd-cart__product"><div id=det_'+ cod + ' class="cd-cart__details"><h3 class="truncate"><a href="#0">' + obj.nombre + '</a></h3><span class="cd-cart__price">$' + Miles(obj.precio) +  '</span> <div class="cd-cart__actions"><a href="#0" class="cd-cart__delete-item pull-right"><i class="fa fa-minus-square" aria-hidden="true"></i></a></div></div></li>';
		    }else{
		        let id_="-1"
		        let nombre = "";
		        $(target).find("div").each(function(index){
		            if (typeof $(this).attr("id") != 'undefined'){
                        nombre = $(".truncate", $(this)).text();
                        id_ = $(this).attr("id").replace("det_","");
                    }
                });
		        let precio_ = target.find("span").html();
                productAdded = '<li class="cd-cart__product"><div id=det_'+ id_ + ' class="cd-cart__details"><h3 class="truncate"><a href="#0">' + nombre +  ' </a></h3><span class="cd-cart__price">' + precio_ + ' </span> <div class="cd-cart__actions"><a href="#0" class="cd-cart__delete-item pull-right"><i class="fa fa-minus-square" aria-hidden="true"></i></a></div></div></li>';
		    }
	     	productId = productId + 1;
			//var productAdded = '<li class="cd-cart__product"><div class="cd-cart__details"><h3 class="truncate"><a href="#0">Cambio plan Oro</a></h3><span class="cd-cart__price">$25.99 </span> <div class="cd-cart__actions"><a href="#0" class="cd-cart__delete-item pull-right"><i class="fa fa-minus-square" aria-hidden="true"></i></a></div></div></li>';
		    if (insertar){
                cartList.insertAdjacentHTML('beforeend', productAdded);
                addItemStorage(productAdded);
                estado = true;
		    }
		    return estado;
		};
		function cargarDetalle(obj){
            let id = obj.codigo;
            let adicional= ''
            if (obj.tipo == '1')
                adicional = 'Cambio plan ';
            obj.nombre = adicional +  $("#item_"+id +" td:eq(0)").html();
            let precio = $("#item_"+id +" td:eq(1)").html();
            precio = precio.split('.').join('').replace('$','').replace('+ IVA','').trim();
            obj.precio = precio;
            return obj;
  		}
  		function addItemStorage(item){
		    registrarValor = false;
		    var id_ = "-1";
		    $(item).find("div").each(function(index){
		        if (typeof $(this).attr("id") != 'undefined'){
                    id_ = $(this).attr("id").replace("det_","");
                }
		    });
		    if (id_!="-1"){
		        let itemStorage = sessionStorage.getItem(id_);
                if(itemStorage==null || itemStorage.indexOf(id_)==-1){
                    sessionStorage.setItem(id_,item);
                }
            }
		}
		function removeItemStorage(item){
		    let id_="-1";
            $(item).find("div").each(function(index){
                if (typeof $(this).attr("id") != 'undefined'){
                    id_ = $(this).attr("id").replace("det_","");
                }
            });
		    /*
		    let itemStorage = sessionStorage.getItem('itemCart');
		    if(itemStorage!=null && itemStorage.indexOf(item)!=-1){
		        let res = itemStorage.replace(item,"");
                if (res.trim()=="")
                    sessionStorage.clear();
                else
                    sessionStorage.setItem("itemCart",res);
            }*/
            let itemStorage = sessionStorage.getItem(id_);
            if(itemStorage!=null && itemStorage.indexOf(id_)!=-1){
                sessionStorage.removeItem(id_);
            }
		}
        /*
		function addItemStorage(item){
		    registrarValor = false;
		    $(item).find("div").each(function(index){
		        if (typeof $(this).attr("id") != 'undefined'){
                    let id_ = $(this).attr("id").replace("det_","");
                }
		    });

		    let itemStorage = sessionStorage.getItem('itemCart');
		    let item_aux = $(itemStorage).html();
            if(itemStorage==null || itemStorage.indexOf(item)==-1){
		        if (itemStorage==null)
		            itemStorage=item;
		        else
		            itemStorage+=item;
		        sessionStorage.setItem("itemCart",itemStorage);
		    }
		}
		function removeItemStorage(item){
		    let itemStorage = sessionStorage.getItem('itemCart');
		    if(itemStorage!=null && itemStorage.indexOf(item)!=-1){
		        let res = itemStorage.replace(item,"");
                if (res.trim()=="")
                    sessionStorage.clear();
                else
                    sessionStorage.setItem("itemCart",res);
            }
		}
		*/
		function removeProduct(product) {
		    if (cartTimeoutId) clearInterval(cartTimeoutId);
			removePreviousProduct();
            let item = $(product).parent().html().trim();
            removeItemStorage(item);
			var topPosition = product.offsetTop,
				productQuantity = 1,
				productTotPrice = Number((product.getElementsByClassName('cd-cart__price')[0].innerText).split('.').join('').replace('$', '')) * productQuantity;
			product.style.top = topPosition + 'px';
			Util.addClass(product, 'cd-cart__product--deleted');
			updateCartTotal(productTotPrice, false);
			updateCartCount(true, -productQuantity);
			Util.addClass(cartUndo, 'cd-cart__undo--visible');
			cartTimeoutId = setTimeout(function() {
				Util.removeClass(cartUndo, 'cd-cart__undo--visible');
				removePreviousProduct();
			}, 8000);
		};

		function removePreviousProduct() {
			var deletedProduct = cartList.getElementsByClassName('cd-cart__product--deleted');
			if (deletedProduct.length > 0) deletedProduct[0].remove();
		};

		function updateCartCount(emptyCart, quantity) {
			if (typeof quantity === 'undefined') {
				var actual = Number(cartCountItems[0].innerText) + 1;
				var next = actual + 1;
				if (emptyCart) {
					cartCountItems[0].innerText = actual;
					cartCountItems[1].innerText = next;
					animatingQuantity = false;
				} else {
                    Util.addClass(cartCount, 'cd-cart__count--update');
                    setTimeout(function() {
                        cartCountItems[0].innerText = actual;
                    }, 150);
                    setTimeout(function() {
                        Util.removeClass(cartCount, 'cd-cart__count--update');
                    }, 200);
                    setTimeout(function() {
                        cartCountItems[1].innerText = next;
                        animatingQuantity = false;
                    }, 230);

				}
			} else {
			    var actual = Number(cartCountItems[0].innerText) + quantity;
				var next = actual + 1;
				cartCountItems[0].innerText = actual;
				cartCountItems[1].innerText = next;
				animatingQuantity = false;
			}
		};

		function updateCartCountDyn(emptyCart, cargar_contador) {
			if (typeof quantity === 'undefined') {
				var actual = Number(cartCountItems[0].innerText) + 1;
				var next = actual + 1;
				if (emptyCart) {
					cartCountItems[0].innerText = actual;
					cartCountItems[1].innerText = next;
					animatingQuantity = false;
				} else {
				    if (cargar_contador){
                        Util.addClass(cartCount, 'cd-cart__count--update');
                        setTimeout(function() {
                            cartCountItems[0].innerText = actual;
                        }, 150);
                        setTimeout(function() {
                            Util.removeClass(cartCount, 'cd-cart__count--update');
                        }, 200);
                        setTimeout(function() {
                            cartCountItems[1].innerText = next;
                            animatingQuantity = false;
                        }, 230);
                    }
				}
			} else {
			    var actual = Number(cartCountItems[0].innerText) + quantity;
				var next = actual + 1;
				cartCountItems[0].innerText = actual;
				cartCountItems[1].innerText = next;
				animatingQuantity = false;
			}
		};

		function updateCartTotal(price, bool) {
	        let total = '';
	        if (bool)
	            total = Miles((Number(cartTotal.innerText.split('.').join('')) + Number(price.toString().split('.').join(''))).toString());
	        else
	            total = Miles((Number(cartTotal.innerText.split('.').join('')) - Number(price.toString().split('.').join(''))).toString());
	        cartTotal.innerText = total;
			//cartTotal.innerText = bool ? (Number(cartTotal.innerText) + Number(price)).toFixed(2) : (Number(cartTotal.innerText) - Number(price)).toFixed(2);
		};
		function quickUpdateCart() {
			var quantity = 0;
			var price = 0;
			for (var i = 0; i < cartListItems.length; i++) {
				if (!Util.hasClass(cartListItems[i], 'cd-cart__product--deleted')) {
					var singleQuantity = Number(cartListItems[i].getElementsByTagName('select')[0].value);
					quantity = quantity + singleQuantity;
					price = price + singleQuantity * Number((cartListItems[i].getElementsByClassName('cd-cart__price')[0].innerText).split('.').join('').replace('$', ''));
				}
			}
			cartTotal.innerText = price.toFixed(2);
			cartCountItems[0].innerText = quantity;
			cartCountItems[1].innerText = quantity + 1;
		};

	}
})();