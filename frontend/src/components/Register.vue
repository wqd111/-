<template>
    <div>
        <div class="outline">
            <h1>高血压用药推荐系统管理平台</h1>
        </div> 
        <p class="register_text">注册新用户</p>
        <div class="register">
            <input type="text" placeholder="请输入用户名" class="id_input" v-model="idVal">
            <span class="search-reset1" @click="clearInput1()">&times;</span>
            <input type="text" placeholder="请输入密码" class="password_input" v-model="passVal">
            <span class="search-reset2" @click="clearInput2()">&times;</span>
            <input type="text" placeholder="确认密码" class="password_confirm" v-model="passVal_confirm">
            <span class="search-reset3" @click="clearInput3()">&times;</span>
            <input type="text" placeholder="请输入手机号" class="phone_input" v-model="phoneVal">
            <span class="search-reset4" @click="clearInput4()">&times;</span>
            

            <router-link to='/login'>
                <button id="login_btn" >已有账户？点击登录</button>
            </router-link>
            <button id="register_btn" @click="register()">注册</button>

            

        </div>
    </div>
</template>

<script type="text/javascript">
// import xxx from someSrc     es6中得到模块的方法。

import axios from 'axios'

export default {
    //注册组件
    data(){
       return{
           idVal: "",
           passVal: "",
           passVal_confirm: "",
           phoneVal: "",
           result:"",
       }
            
        
    },
    

    methods:{
        getRegister(){
            const path = `http://localhost:5000/user/register`

            axios
            .get(path,{
                params:{
                    name: this.idVal,
                    password: this.passVal,
                    phone:this.phoneVal
                }
            })
            .then(response => {
                this.result = response.data
                if(this.result.code == 200){
                    alert('注册成功！id:' + this.result.data.id)
                }
                else{
                    alert(this.result.msg)
                }
            })
            .catch(error => {
                console.log(error)
            })
        },
        clearInput1(){
            this.idVal = "";
        },
        clearInput2(){
            this.passVal = "";
        },
        clearInput3(){
            this.passVal_confirm = "";
        },
        clearInput4(){
            this.phoneVal = "";
        },
        register(){
            if(this.passVal===this.passVal_confirm && this.idVal && this.phoneVal && this.passVal){
                this.getRegister()
            }
            else{
                alert('ERROR')
            }
        }


    }



}



</script>

<style type="text/css" scoped>

input::-ms-clear {
    display: none
}




.register {
    height: 45px;
    width: 420px;
    margin: 0 auto;
    margin-top: 20px;
    border: 1px;
    position: relative;
}


.id_input  {
    border: 2px solid #e4e4e4;
    box-sizing: border-box;
    width: 420px;
    height: 45px;
    font-size: 18px;
    float: left;
    padding-left: 10px;
    padding-right: 10px;
    overflow: hidden;
    
}
.password_input  {
    border: 2px solid #e4e4e4;
    box-sizing: border-box;
    width: 420px;
    height: 45px;
    font-size: 18px;
    float: left;
    padding-left: 10px;
    padding-right: 10px;
    overflow: hidden;
    margin-top:40px;
    
}
.password_confirm {
    border: 2px solid #e4e4e4;
    box-sizing: border-box;
    width: 420px;
    height: 45px;
    font-size: 18px;
    float: left;
    padding-left: 10px;
    padding-right: 10px;
    overflow: hidden;
    margin-top:40px;
}
.phone_input {
    border: 2px solid #e4e4e4;
    box-sizing: border-box;
    width: 420px;
    height: 45px;
    font-size: 18px;
    float: left;
    padding-left: 10px;
    padding-right: 10px;
    overflow: hidden;
    margin-top:40px;
}

.search-reset1 {
    width: 21px;
    height: 21px;
    position: relative;
    top:-33px;
    left:390px;
    display: block;
    line-height: 21px;
    text-align: center;
    cursor: pointer;
    font-size: 20px;
    
   
}
.search-reset2 {
    width: 21px;
    height: 21px;
    position: relative;
    top:-33px;
    left:390px;
    display: block;
    line-height: 21px;
    text-align: center;
    cursor: pointer;
    font-size: 20px;

   
}
.search-reset3 {
    width: 21px;
    height: 21px;
    position: relative;
    top:-33px;
    left:390px;
    display: block;
    line-height: 21px;
    text-align: center;
    cursor: pointer;
    font-size: 20px;

   
}
.search-reset4 {
    width: 21px;
    height: 21px;
    position: relative;
    top:-33px;
    left:390px;
    display: block;
    line-height: 21px;
    text-align: center;
    cursor: pointer;
    font-size: 20px;

   
}

#register_btn{
    
    height: 45px;
    width: 420px;
    border: 1px solid mediumseagreen;
    background-color: mediumseagreen;
    color: white;
    font-size: 16px;
    font-weight: bold;
    float: left;
    margin-top: 10px;
    cursor: pointer;
}

#login_btn {
    background-color: transparent;
    border-style: none;
    outline: none;
    color: cornflowerblue;
    float:left;
    font-size: 16px;
    margin-top:10px;
    cursor: pointer;
}

.register_text {
    font-size:18px;
    color: mediumseagreen;
}

.outline{
    margin-top: 80px;
}
</style>

