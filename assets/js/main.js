$(document).ready(() => {


  $('.information').on('click', event => {
      $(event.currentTarget).closest('.item').siblings().find('.more-info').removeClass('rotate');
      $(event.currentTarget).closest('.item').find('.extra-info').slideToggle();
      $(event.currentTarget).find('.more-info').toggleClass('rotate');
      $('.menu').slideUp();
      $('#menu-button').removeClass('pressed');
      $('.content').removeClass('move-up');
      //close siblings
      $(event.currentTarget).closest('.item').siblings().find('.extra-info').slideUp();
      $(event.currentTarget).closest('.item').siblings().find('.extra-info').find('li').removeClass('active');
      $('.sizes').slideUp();
      $('.addcart-button').removeClass('sizes-on');
      $('.extra-info').css("padding-bottom", "0px");
      $(".current-size").html("select size");
      return false;
  });

  $('.extra-info li').on('click' , event => {
    $(event.currentTarget).addClass('active');
    $(event.currentTarget).siblings().removeClass('active');
    $('.sizes').slideUp();
    return false;
  })


  $('#menu-button').on('click' , () => {
    if ($('.menu-container').css("display") != "block") {
      $("html, body").animate({ scrollTop: 0 }, "slow");
    }
    toggleMenu();
    if ($('.cartoverview').css("display") == "block") {
      toggleCartOverview();
    }
    if ($('.currencyMenu').css("display") == "block") {
      toggleCurrency();
    }
    if ($('.user-form').css("display") == "block") {
      toggleUser();
    }
    return false;
  })

  function toggleMenu() {
    $('.menu').slideToggle();
    $('#menu-button').toggleClass('pressed');
    $('.content').toggleClass('move-up');
    return false;
  }

  function toggleUser() {
    $('.user-form').slideToggle();
    $('#user-button').toggleClass('pressed');
    return false;
  }

  $('#user-button').on('click' , () => {
    toggleUser();
    if ($('.menu').css("display") == "block") {
      toggleMenu();
    }
    if ($('.currencyMenu').css("display") == "block") {
      toggleCurrency();
    }
    if ($('.cartoverview').css("display") == "block") {
      toggleCartOverview();
    }
    return false;
  })

  $('#icon').on('click' , () => {
    toggleCartOverview();
    if ($('.menu').css("display") == "block") {
      toggleMenu();
    }
    if ($('.currencyMenu').css("display") == "block") {
      toggleCurrency();
    }
    if ($('.user-form').css("display") == "block") {
      toggleUser();
    }
    return false;
  })

  function toggleCartOverview () {
      $('#icon').toggleClass('pressed');
      $('.cartoverview').slideToggle();
      return false;
  }

  $('.filter-button').on('click' , () => {
    $('.filter').toggle("slide");
    return false;
  })

  $('#closefilter').on('click' , () => {
    $('.filter').toggle("slide");
    return false;
  })

  /*$('.content').on('click' , () => {
    $('.menu').slideUp();
    $('#menu-button').removeClass('pressed');
    $('.content').removeClass('move-up');
    $('.extra-info').slideUp();
    $('.more-info').removeClass('rotate');
    $('.extra-info').find('li').removeClass('active');
    $('.addcart-button').addClass('disabled');
    $('.sizes').slideUp();
    $('.addcart-button').removeClass('sizes-on');
    $('.extra-info').css("padding-bottom", "0px");
    $(".current-size").html("select size");
    $('.cartoverview').slideUp();
    $('#icon').removeClass('pressed');
    if ($('.currencyMenu').css("display") == "block") {
      toggleCurrency();
    }
    if ($('.user-form').css("display") == "block") {
      toggleUser();
    }
    return false;
  })*/

  $('.dropdown-size-container').on('click' , event => {
    $('.sizes').slideToggle();
    $('.addcart-button').toggleClass('sizes-on');
    if ($('.addcart-button').css("display") === "none") {
      $('.extra-info').css("padding-bottom", "53px");
    } else if ($('.addcart-button').css("display") === "block") {
      $('.extra-info').css("padding-bottom", "0px");
    }
      $('.size-arrow .material-icons').toggleClass('rotate-180');
    return false;
  })

  /*$('.sizes li').on('click' , event => {
    $('.sizes').slideUp();
    $('.addcart-button').toggleClass('sizes-on');
    if ($('.addcart-button').css("display") === "none") {
      $('.extra-info').css("padding-bottom", "53px");
    } else if ($('.addcart-button').css("display") === "block") {
      $('.extra-info').css("padding-bottom", "0px");
    }
    $(".current-size").html($(event.currentTarget).html());
    return false;
  })

  let items = parseInt($('.counter').html());
  $('.addcart-button').on('click' , () => {
    if ($('.addcart-button').css("opacity") == 1) {
      items += 1;
      $('.counter').html(items);
      $('#amount').html(items);
      if($(".counter").html()!="0") $(".counter").css("display", "inline");
      $('div.tooltip').fadeIn();
      setTimeout(function(){ $('div.tooltip').fadeOut(); }, 2000);
      return false;
    }
  })

/ shoppingCartCost();

  function shoppingCartCost() {
    let subTotal = 0;
    $('.price').each(function(i, obj) {
        subTotal += parseFloat($(obj).html());
      });
    $('#subTotal').html(subTotal.toFixed(2));
    $('#delivery').html(4.99);
    $('#total').html((parseFloat(subTotal) + parseFloat($('#delivery').html())).toFixed(2));
  }

  function shoppingCartCostUpdate() {
    let subTotal = 0;
    $('.price').each(function(i, obj) {
      if (i < ($('.price').length-3)) {
        subTotal += parseFloat($(obj).html());
      }
      });
    $('#subTotal').html(subTotal.toFixed(2));
    $('#delivery').html(4.99);
    $('#total').html((parseFloat(subTotal) + parseFloat($('#delivery').html())).toFixed(2));
  }

  let prices = [];
  $('.price').each(function(i, obj) {
    if (i < ($('.price').length-3)) {
      prices.push($(obj).html());
    }
  });

 $(".input").on("change paste keyup", function() {
    if ($(this).val() < 0 || $(this).val() > 20) {
      $(this).val("1");
    }
    if ($(this).hasClass("quantity0")) {
        $(this).closest('tr').find(".price").html(($(this).val()*prices[0]).toFixed(2));
    } else {
      $(this).closest('tr').find(".price").html(($(this).val()*prices[1]).toFixed(2));
    }
    shoppingCartCostUpdate();
});


  function amountCost() {
    $('.price').each(function(i, obj) {
      if (i < ($('.price').length-3)) {
        $('.price').html($('.price').html());
      }
    });
  }

  $('.fa-remove').on('click',function(e){
         e.preventDefault();
        $(this).parents('tr').remove();
        shoppingCartCostUpdate();
      });*/


  $('#currency').on('click' , () => {
    toggleCurrency();
    if ($('.cartoverview').css("display") == "block") {
      toggleCartOverview();
    }
    if ($('.menu').css("display") == "block") {
      toggleMenu();
    }
    if ($('.user-form').css("display") == "block") {
      toggleUser();
    }
    return false;
 })

  function toggleCurrency() {
      $('#currency').toggleClass('pressed');
      $('.currencyMenu').slideToggle();
  }

  let arrow = '<i class="material-icons currencyarrow">keyboard_arrow_down</i>';

  $('#dollar').on('click' , () => {
    let currentSign = "dollar";
    if ($('#dollar').html() == "$") {
      if ($('#currency').html() == ('\u20ac' + arrow)) {
        convertEuroToDollar(currentSign);
      } else if ($('#currency').html() == ('\u00A3' + arrow)) {
        convertPoundToDollar(currentSign);
      }
      $('span.tooltip').html("Currency changed to 'Dollar'");
    } else if ($('#dollar').html() == '\u20ac') {
      if ($('#currency').html() == ('$' + arrow)) {
        convertDollarToEuro(currentSign);
      } else if ($('#currency').html() == ('\u00A3' + arrow)) {
        convertPoundToEuro(currentSign);
      }
      $('span.tooltip').html("Currency changed to 'Euro'");
    } else {
      if ($('#currency').html() == ('$' + arrow)) {
        convertDollarToPound(currentSign);
      } else if ($('#currency').html() == ('\u20ac' + arrow)) {
        convertEuroToPound(currentSign);
      }
      $('span.tooltip').html("Currency changed to 'Pound'");
    }
    setTimeout(function(){ $('span.tooltip').fadeIn(); }, 300);
    setTimeout(function(){ $('span.tooltip').fadeOut(); }, 1500);

  })

  $('#pound').on('click' , () => {
    let currentSign = "pound";
    if ($('#pound').html() == "$") {
      if ($('#currency').html() == ('\u20ac' + arrow)) {
        convertEuroToDollar(currentSign);
      } else if ($('#currency').html() == ('\u00A3' + arrow)) {
        convertPoundToDollar(currentSign);
      }
      $('span.tooltip').html("Currency changed to 'Dollar'");
    } else if ($('#pound').html() == '\u20ac') {
      if ($('#currency').html() == ('$' + arrow)) {
        convertDollarToEuro(currentSign);
      } else if ($('#currency').html() == ('\u00A3' + arrow)) {
        convertPoundToEuro(currentSign);
      }
      $('span.tooltip').html("Currency changed to 'Euro'");
    } else {
      if ($('#currency').html() == ('$' + arrow)) {
        convertDollarToPound(currentSign);
      } else if ($('#currency').html() == ('\u20ac' + arrow)) {
        convertEuroToPound(currentSign);
      }
      $('span.tooltip').html("Currency changed to 'Pound'");
    }
    setTimeout(function(){ $('span.tooltip').fadeIn(); }, 300);
    setTimeout(function(){ $('span.tooltip').fadeOut(); }, 1500);

  })

  function convertDollarToEuro(currentSign) {
    $('.price').each(function(i, obj) {
      let priceEuro = Math.ceil($(obj).html() / 1.192) - 0.01;
      $(obj).html(priceEuro);
    });
    $('.currencysign').each(function(i, obj) {
        $(obj).html("&euro;");
    });
    $('#currency').removeClass('pressed');
    $('.currencyMenu').slideUp();
    $('#currency').html('&euro;' + arrow);
    if (currentSign == "dollar") {
      $('#dollar').html('&dollar;');
    } else if (currentSign == "pound") {
      $('#pound').html('&dollar;');
    }
  }

  function convertDollarToPound(currentSign) {
    $('.price').each(function(i, obj) {
      let pricePound = ($(obj).html() / 1.347).toFixed(2);
      $(obj).html(pricePound);
    });
    $('.currencysign').each(function(i, obj) {
        $(obj).html("&pound;");
    });
    $('#currency').removeClass('pressed');
    $('.currencyMenu').slideUp();
    $('#currency').html('&pound;' + arrow);
    if (currentSign == "dollar") {
      $('#dollar').html('&dollar;');
    } else if (currentSign == "pound") {
      $('#pound').html('&dollar;');
    }
  }

  function convertEuroToDollar(currentSign) {
    $('.price').each(function(i, obj) {
        let priceDollar = ($(obj).html() * 1.192).toFixed(2);
        $(obj).html(priceDollar);
      });
      $('.currencysign').each(function(i, obj) {
          $(obj).html("&dollar;");
      });
      $('#currency').removeClass('pressed');
      $('.currencyMenu').slideUp();
      $('#currency').html('&dollar;' + arrow);
      if (currentSign == "dollar") {
        $('#dollar').html('&euro;');
      } else if (currentSign == "pound") {
        $('#pound').html('&euro;');
      }
  }

  function convertEuroToPound(currentSign) {
    $('.price').each(function(i, obj) {
        let pricePound = ($(obj).html() * 0.883).toFixed(2);
        $(obj).html(pricePound);
      });
      $('.currencysign').each(function(i, obj) {
          $(obj).html("&pound;");
      });
      $('#currency').removeClass('pressed');
      $('.currencyMenu').slideUp();
      $('#currency').html('&pound;' + arrow);
      if (currentSign == "dollar") {
        $('#dollar').html('&euro;');
      } else if (currentSign == "pound") {
        $('#pound').html('&euro;');
      }
  }

  function convertPoundToEuro(currentSign) {
    $('.price').each(function(i, obj) {
        let priceEuro = Math.ceil($(obj).html() / 0.883) -0.01;
        $(obj).html(priceEuro);
      });
      $('.currencysign').each(function(i, obj) {
          $(obj).html("&euro;");
      });
      $('#currency').removeClass('pressed');
      $('.currencyMenu').slideUp();
      $('#currency').html('&euro;' + arrow);
      if (currentSign == "dollar") {
        $('#dollar').html('&pound;');
      } else if (currentSign == "pound") {
        $('#pound').html('&pound;');
      }
  }

  function convertPoundToDollar(currentSign) {
    $('.price').each(function(i, obj) {
        let priceDollar = ($(obj).html() * 1.347).toFixed(2);
        $(obj).html(priceDollar);
      });
      $('.currencysign').each(function(i, obj) {
          $(obj).html("&dollar;");
      });
      $('#currency').removeClass('pressed');
      $('.currencyMenu').slideUp();
      $('#currency').html('&dollar;' + arrow);
      if (currentSign == "dollar") {
        $('#dollar').html('&pound;');
      } else if (currentSign == "pound") {
        $('#pound').html('&pound;');
      }
  }


  $(document).ready(function() {
       // messages timeout for 10 sec
       setTimeout(function() {
           $('.message').fadeOut('slow');
       }, 3000); // <-- time in milliseconds, 1000 =  1 sec
   });

})
