
<template>

    <div>
        <div class="manager-btn">
            <el-divider>点击按钮进入下列功能</el-divider>
            <router-link to="/allgraph">
                <el-button type="primary" class="all-btn"><b>查看全部图谱</b></el-button>
            </router-link>
            <router-link to="/guide">
                <el-button type="primary" class="zhinan-btn"><b>临床指南管理</b></el-button>
            </router-link>
            <el-button type="primary" class="paper-btn"><b>相关文献审核</b></el-button>
        </div>

        <div class="user-btn">
            <el-divider>点击按钮修改以下图谱</el-divider>
            <router-link to="/ingraph">
                <el-button type="primary" class="in-btn"><b>适应证<br/><br/>知识图谱</b></el-button>
            </router-link>
            <router-link to="/disease">
                <el-button type="primary" class="disease-btn"><b>疾病<br/><br/>知识图谱</b></el-button>
            </router-link>
            <router-link to="/druggraph">
                <el-button type="primary" class="drug-btn"><b>药品<br/><br/>知识图谱</b></el-button>
            </router-link>
            <router-link to="/contragraph">
                <el-button type="primary" class="con-btn"><b>相对/绝对禁忌证<br/><br/>知识图谱</b></el-button>
            </router-link>
            <router-link to="/combgraph">
                <el-button type="primary" class="combine-btn"><b>药物联合治疗<br/><br/>知识图谱</b></el-button>
            </router-link>
            <el-button type="primary" class="addgraph-btn" icon="el-icon-circle-plus-outline"></el-button>
        </div>
        

    </div>

</template>

<script type="text/javascript">

export default {

data () {
    return {
        
    }
    
},

methods: {
    
}

}

</script>

<style type="text/css" scoped>
.manager-btn{
    width:80%;
    margin-left:10%;
}

.all-btn{
    height:250px;
    width:250px;
    font-size:30px;
    color:black;
    background-color:#FFFACD;
    border-color:#FFFACD;
    float:left;
    margin-left:10%;
    margin-top:3%;
}

.zhinan-btn{
    height:250px;
    width:250px;
    font-size:30px;
    color:black;
    background-color:#98FB98;
    border-color:#98FB98;
    float:left;
    margin-left:9.5%;
    margin-top:3%;
}
.paper-btn{
    height:250px;
    width:250px;
    font-size:30px;
    color:black;
    background-color:Plum;
    border-color:Plum;
    float:left;
    margin-left:9.5%;
    margin-top:3%;
}

.user-btn{
    width:80%;
    margin-left:10%;
    margin-top:25%;
   
}

.in-btn{
    height:250px;
    width:250px;
    font-size:30px;
    color:black;
    background-color:#6495ED;
    border-color:#6495ED;
    float:left;
    margin-left:10%;
    margin-top:3%;
}

.con-btn{
    height:250px;
    width:250px;
    font-size:30px;
    color:black;
    background-color:#FA8072;
    border-color:#FA8072;
    float:left;
    margin-left:10%;
    margin-top:5%;
}

.disease-btn{
    height:250px;
    width:250px;
    font-size:30px;
    color:black;
    background-color:#FFE4C4;
    border-color:#FFE4C4;
    float:left;
    margin-left:9.5%;
    margin-top:3%;
}

.drug-btn{
    height:250px;
    width:250px;
    font-size:30px;
    color:black;
    background-color:#87CEFA;
    border-color:#87CEFA;
    float:left;
    margin-left:9.5%;
    margin-top:3%;
}

.combine-btn{
    height:250px;
    width:250px;
    font-size:30px;
    color:black;
    background-color:LightBlue;
    border-color:LightBlue;
    float:left;
    margin-left:9.5%;
    margin-top:5%;
    margin-bottom:100px;
}

.addgraph-btn{
    height:250px;
    width:250px;
    font-size:30px;
    color:black;
    background-color:Lavender;
    border-color:Lavender;
    float:left;
    margin-left:9.5%;
    margin-top:5%;
    font-size:120px;
}

</style>
