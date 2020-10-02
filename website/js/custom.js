$("document").ready(function(){
    $("#submit").click(function(){
        //for first name
        var fn=document.getElementById("first_name").value;
        var regFn= /^[0-9]+$/;

        //for last name
        var ln=document.getElementById("last_name").value;
        var regLn= /^[0-9]+$/;

        //for email
        var em=document.getElementById("email").value;
        var regEmail= /^([a-z 0-9 \.-]+)@([a-z 0-9 -]+).([a-z]{2,8})(.[a-z]{2,8})?$/;

        //for username
        var un=document.getElementById("username").value;

        //for password
        var pw=document.getElementById("password").value;

         //for Re-password
         var rpw=document.getElementById("repassword").value;


        //first name
            if (fn.trim()==""){
                $("#error_first_name").text("*please fillout this field")
                .css({
                    'visibility':'visible',
                    'color':'red',
                })
                return false;
            }
            else if(regFn.test(fn)==true){
                $("#error_first_name").text("*Name can't be numeric")
                .css({
                    'visibility':'visible',
                    'color':'red',
                })
                return false;
            }

            else if(regFn.test(fn)==false){
                $("#error_first_name").text("Accepted")
                .css({
                    'visibility':'visible',
                    'color':'green',
                })

                //last name
                    if (ln.trim()==""){
                        $("#error_last_name").text("*please fillout this field")
                        .css({
                            'visibility':'visible',
                            'color':'red',
                        })
                        return false;
                    }
                    else if(regLn.test(ln)==true){
                        $("#error_last_name").text("*Name can't be numeric")
                        .css({
                            'visibility':'visible',
                            'color':'red',
                        })
                        return false;
                    }

                    else if(regLn.test(ln)==false){
                        $("#error_last_name").text("Accepted")
                        .css({
                            'visibility':'visible',
                            'color':'green',
                        })


                        //email
                            if (em.trim()==""){
                                $("#error_email").text("*please fillout this field")
                                .css({
                                    'visibility':'visible',
                                    'color':'red',
                                })
                                return false;
                            }

                            else if(regEmail.test(em)==false){
                                $("#error_email").text("*Invalid Email ID")
                                .css({
                                    'visibility':'visible',
                                    'color':'red',
                                })
                                return false;
                            }

                            else if(regEmail.test(em)==true){
                                $("#error_email").text("Accepted")
                                .css({
                                    'visibility':'visible',
                                    'color':'green',
                                })

                                //username
                                    if (un.trim()==""){
                                        $("#error_username").text("*please fillout this field")
                                        .css({
                                            'visibility':'visible',
                                            'color':'red',
                                        })
                                        return false;
                                    }
                                    else if(un.trim().length <4){
                                        $("#error_username").text("*Minimum 4 alphanumeric keywords required")
                                        .css({
                                            'visibility':'visible',
                                            'color':'red',
                                        })
                                        return false;
                                    }

                                    else if(un.trim().length >= 4){
                                        $("#error_username").text("Accepted")
                                        .css({
                                            'visibility':'visible',
                                            'color':'green',
                                        })

                                    
                                    
                                    }

                                    //password
                                        if (pw.trim()==""){
                                            $("#error_password").text("*please fillout this field")
                                            .css({
                                                'visibility':'visible',
                                                'color':'red',
                                            })
                                            return false;
                                        }
                                        else if(pw.trim().length <4){
                                            $("#error_password").text("*Minimum 4 alphanumeric keywords required")
                                            .css({
                                                'visibility':'visible',
                                                'color':'red',
                                            })
                                            return false;
                                        }

                                        else if(pw.trim().length >=4){
                                            $("#error_password").text("Accepted")
                                            .css({
                                                'visibility':'visible',
                                                'color':'green',
                                            })
                                        }

                                            //Re-password
                                                if (rpw.trim()==""){
                                                    $("#error_repassword").text("*please fillout this field")
                                                    .css({
                                                        'visibility':'visible',
                                                        'color':'red',
                                                    })
                                                    return false;
                                                }
                                                else if(rpw.trim()!=pw.trim()){
                                                    $("#error_repassword").text("*Password didn't match. Try again!")
                                                    .css({
                                                        'visibility':'visible',
                                                        'color':'red',
                                                    })
                                                    return false;
                                                }

                                                else if (rpw.trim()==pw.trim()){
                                                    $("#error_repassword").text("Accepted")
                                                    .css({
                                                        'visibility':'visible',
                                                        'color':'green',
                                                    })
                                                }

                                                //start next code here
                                                
                                




                                        
                                }
                
                        
                }
                
            }

        return true;
    })
})