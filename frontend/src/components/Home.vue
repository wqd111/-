// Home.vue

<template>

    <div>
        <div class="home-title">
            <h1>高血压用药推荐系统</h1>
        </div>
        <div class="demo-image__placeholder">
            <div class="block">
                <el-image :src="src"></el-image>
            </div>
        </div>
        <div id="login-btn">
            <router-link to="/login">
                <el-button type="primary" size="medium">登录/注册</el-button>
            </router-link>
        </div>

    </div>

</template>

<script type="text/javascript">

export default {

data () {
    return {
        src: require("../assets/home.png")
    }
    
},

methods: {
    
}

}

</script>

<style type="text/css" scoped>
.home-title{
    font-size: 18px;
    margin-top: 5%
}

.block{
    margin-top: 3%;
}
#login-btn{
    margin-top: 3%;
}
</style>
