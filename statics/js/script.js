$(document).ready(function(){
    $("#submit").click(function(){
        var text = $("#text").val();
        var pd = {"text":text};
	$('p').html("<p><font color='grey'> &nbsp&nbsp&nbsp &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp loading...</font>");
        $.ajax({
            type:"post",
            url:"/",
            data:pd,
            cache:false,
	    success:function(data){
		$('p').html("");
                window.location.href = "/down";
            },	
	  
        });
    
    });





});
