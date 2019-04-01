$("document").ready(function(){
         $("#submit").click(function(){
            var flag=1;
           var name=$("#username").val();
           if(name.length==0||name=="张三"){
                $("#tip1").html("请填账号");
                flag=0;
				 $("#username").focus();
                return false;
            }
			else{
				$("#tip1").html("");
			}
		   
            var password=$("#password").val();
            if(password.length==0){
                 $("#tip2").html("请填密码");
                 flag=0;
				 $("#password").focus();
                 return false;
            }
			else if(password.length!=6){
                 $("#tip2").html("密码为六位");
                 flag=0;
				 $("#password").focus();
                 return false;
            }
			else{
				$("#tip2").html("");
			}
		 })
          
});