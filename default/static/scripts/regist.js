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
			var mail=$("#mail").val();
           if(mail.length==0){
                $("#tip3").html("请输邮箱");
                flag=0;
				 $("#mail").focus();
                return false;
            }
			else{
				$("#tip3").html("");
			}
			 var phone=$("#phone").val();
            if(phone.length==0){
                 $("#tip4").html("请输电话");
				 $("#phone").focus();
				 flag=0;
                 return false;
            }else if(isNaN(phone)){
                  $("#tip4").html("只能为数字");
                  $("#phone").focus();
				 flag=0;
                 return false;
             }
			else if(phone.length!=11){
                 $("#tip4").html("电话为11位");
				 $("#phone").focus();
				 flag=0;
                 return false;
            }
			else{
				$("#tip4").html("");
			}
			var name=$("#name").val();
           if(name.length==0){
                $("#tip5").html("请输名字");
                flag=0;
				 $("#name").focus();
                return false;
            }
			else{
				$("#tip5").html("");
			}

		 })
        $("#return").click(function(){
            $("#form1").attr("action", "/login/");
            $("#form1").attr("method", "get");
        })
});