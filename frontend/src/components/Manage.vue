<template>
    <div>
        <div class='breadcrumb'>
            <el-breadcrumb separator="/" class="bc">
                <el-breadcrumb-item :to="{ path: '/mainwindow' }">首页</el-breadcrumb-item>
                <el-breadcrumb-item>用户管理</el-breadcrumb-item>
                <router-link :to="{name: 'MainWindow'}">
                    <el-button round size="mini" class="back-btn">返回</el-button>
                </router-link>
            </el-breadcrumb>
        </div>
        <div class='disease_title'>
            <p>用户管理</p>
        </div>
        <div id='disease_search'>
            <input v-model="searchVal" placeholder="请输入内容" id="disease_input">
            <el-button type="primary" icon="el-icon-search" @click="search_disease()" id="search_btn">搜索</el-button>
            
            <el-button type="primary" class="add_btn">添加数据</el-button>
            
        </div>
        
        <div id='disease_table'>
            <el-table 
            :data="tableData" heigt="500" border style="width:85%">
                <el-table-column prop="id" label="用户ID" width="100"></el-table-column>
                <el-table-column prop="name" label="用户名" width="200"></el-table-column>
                <el-table-column prop="pw" label="密码" width="300"></el-table-column>
                <el-table-column prop="phone" label="手机号" width="300"></el-table-column>
                
                <el-table-column fixed="right" label="设置为管理员" width="200">
                    
                    <template slot-scope="scope">
                        <el-switch
                            v-model="value"
                            active-color="#13ce66"
                            inactive-color="grey">
                        </el-switch>

                    </template>
                    
                </el-table-column>
            </el-table>
        </div>
        
        
        
    </div>
    
</template>

<script type="text/javascript">

import axios from 'axios'

export default {
    //注册组件
    data(){
        return{
            value:false,
            searchVal:"",
            tableData: [
                {
                    id:'1',
                    name:'111',
                    pw:'111',
                    phone:'111'
                }
            ]
        }
    },
    

    methods:{
        handleEdit(index, row) {
            console.log(index, row);
        },
        handleDelete(index, row) {
            console.log(index, row);
        },
        getMongo(search) {
            const path = `http://localhost:5000/mongo/query`

            axios
            .get(path,{
                params:{
                    table: "icd",
                    msg: search
                }
            })
            .then(response => {
                var is_success = response.data.code
                if(is_success == 200){
                    this.tableData = response.data.data
                }
                else{
                    alert(response.data.msg)
                    this.tableData = []
                }
                
            })
            .catch(error => {
                console.log(error)
            })
        },
        search_disease(){
            var search = this.searchVal;
            this.getMongo(search);
            /* if (search){
                
            } */
        }
        
    }
    
}
</script>
<style type="text/css">
.breadcrumb{
    margin-left:10%;
    width: 80%;
    height:50px;
    margin-top:-25px;
    border-left: 1px solid LightSteelBlue;
    border-bottom: 1px solid LightSteelBlue;
    border-right: 1px solid LightSteelBlue;
}

.bc{
    margin-left:20px;
    padding-top:20px;
    
}

.back-btn{
    margin-left:80%;
    margin-top:-2%;
}
.disease_title{
    font-size: 32px;
    font-weight: bold;
    text-align: left;
    margin-left:13%;
    margin-top:100px;
}
#disease_search{
    width:74%;
    margin-left:13%;
    margin-top:20px;
    
}

#disease_input{
    float:left;
    height:30px;
    width:200px;
    margin-top:5px;
}

#disease_table{
    margin-left: 13%;
    margin-top:100px;
    margin-bottom:100px;
}

.add_btn{
    float: right;
    margin-left:100%;
}

#search_btn{
    float:left;
    margin-left:10px;
}


</style>

