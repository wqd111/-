<template>
    
    <div>
        
        <div class="outline">
            <h1>高血压用药推荐系统管理平台</h1>
            <div class="login_header">
				<span @click="cur=0" :class="{active:cur==0}">用户名登录</span>
				<span @click="cur=1" :class="{active:cur==1}">手机号登录</span>
		    </div>
        </div> 

        
        <div class="login" v-show="cur==0">
            <el-input placeholder="用户名" class="id_input" v-model="idVal" clearable></el-input>
            
            <el-input placeholder="密码" class="password_input" v-model="passVal" show-password></el-input>
            
            <button class="forget_btn" @click="forgetpw()">忘记密码</button>
            <router-link to="/register">
                <button class="register_btn">注册账户</button>
            </router-link>
            <button class="login_btn" @click="login()">登录</button>
                   

        </div>
        
        <div class="login" v-show="cur==1">
            <el-input placeholder="手机号" class="id_input" v-model="phoneVal" clearable></el-input>
            
            <el-input placeholder="密码" class="password_input" v-model="passVal" show-password></el-input>
            
            <button class="forget_btn" @click="forgetpw()">忘记密码</button>
            <router-link to="/register">
                <button class="register_btn">注册账户</button>
            </router-link>
            <button class="login_btn" @click="login()">登录</button>

        </div>

        <!-- <p>{{ result }}</p> -->


    </div>
</template>

<script type="text/javascript">
// import xxx from someSrc     es6中得到模块的方法。

import axios from 'axios'

export default {
    //注册组件
    data(){
       return{
           idVal:"",
           passVal:"",
           phoneVal:"",
           cur:0,
           result: "",
       }
    },

    methods:{
        sendUsername() {
            this.$router.push({
            path: '/mainwindow', 
            name:"MainWindow",
            params: { 
                name: this.idVal, 
            },
            /* query: {
                name: 'name', 
            } */
        })

        },
        getLogin() {
            const path = `http://localhost:5000/user/login`

            axios
            .get(path,{
                params:{
                    name: this.idVal,
                    password: this.passVal
                }
            })
            .then(response => {
                this.result = response.data
                //alert(this.result)
                this.sendUsername()
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

        login(){
            var id = this.idVal;
            var pw = this.passVal;
            if (id ==='' || pw === ''){
                alert('请输入用户名或密码')
            } else {     
                this.getLogin()
            }
        },

    }



}



</script>

<style type="text/css" scoped>

.login {
    height: 45px;
    width: 420px;
    margin: 0 auto;
    margin-top: 20px;
    border: 1px;
    position: relative;
}


.id_input  {
    
    width: 420px;
    height: 45px;
    font-size: 18px;
    
    
    
}
.password_input  {
    
    width: 420px;
    height: 45px;
    font-size: 18px;
    
    margin-top:40px;
    
}



.login_btn {
    
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

.forget_btn {
    background-color: transparent;
    border-style: none;
    outline: none;
    color: cornflowerblue;
    
    font-size: 16px;
    float:right;
    margin-top:10px;
    cursor: pointer;
}

.register_btn {
    background-color: transparent;
    border-style: none;
    outline: none;
    color: cornflowerblue;
    float:left;
    font-size: 16px;
    margin-top:10px;
    cursor: pointer;
}

.login_text {
    font-size:18px;
    
    color: mediumseagreen;
}

.login_header{
    margin-top:50px;
    font-size: 18px;
    
}
.login_header span{
    margin-right: 20px;
    cursor: pointer;
}
.active{
    color: mediumseagreen;
    padding-bottom: 10px;
}
.outline{
    margin-top: 50px;
}
</style>