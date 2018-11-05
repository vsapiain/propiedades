$(document).ready(function(){
    $('.search-text').keyup(function(){
         var text = $(this).val().trim();
         $('.card').hide();
         var count = $('.card:contains("'+text+'")').length;
         $(".number-word").text(count);
         $(".number-word").parent().show();
         if (text == "")
            $(".number-word").parent().hide();
         $('.card:contains("'+text+'")').closest('.card').show();
    });

    $.expr[":"].contains = $.expr.createPseudo(function(arg) {
        return function( elem ) {
        return $(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
      };
    });
});