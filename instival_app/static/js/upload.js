$('.dropdown-menu a').on('click', function(){   
    //change dropdown text
    $(this).parent().parent().prev().html($(this).html() + '<span class="caret"></span>');
    
    var value = $(this).parent().parent().prev().val();
    var select = $(this).html();
    
    //if chose other display textbox
   if(value=="1"){
         if(select=="Other Festival" ) {
        		document.getElementById('f_text').style.display='';
        	}
         else {
        		document.getElementById('f_text').style.display='none';
        	}
   }
    if(value=="2"){
        if(select=="Other Country") {
        		document.getElementById('c_text').style.display='';
        	}
         else {
        		document.getElementById('c_text').style.display='none';
        	}
    }

})




