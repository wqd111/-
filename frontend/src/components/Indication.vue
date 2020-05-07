<template>
    <div>
        <div class='breadcrumb'>
            <el-breadcrumb separator="/" class="bc">
                <el-breadcrumb-item :to="{ path: '/mainwindow' }">首页</el-breadcrumb-item>
                <el-breadcrumb-item :to="{ path: '/ingraph'}">适应证知识图谱</el-breadcrumb-item>
                <el-breadcrumb-item>适应证表格</el-breadcrumb-item>
                <router-link :to="{name: 'IndicaionGraph'}">
                    <el-button round size="mini" id="back-btn">返回</el-button>
                </router-link>
            </el-breadcrumb>
        </div>
        <div class='disease_title'>
            <p>适应证</p>
        </div>
        <div class='disease_search'>
            <input v-model="searchVal" placeholder="请输入内容" class="disease_input">
            <el-button type="primary" icon="el-icon-search" @click="search_disease()" id="search_btn">搜索</el-button>
            <el-radio-group v-model="radio">
                <el-radio :label="0">全部</el-radio>
                <el-radio :label="1">+</el-radio>
                <el-radio :label="2">-</el-radio>
                <el-radio :label="3">±</el-radio>
            </el-radio-group>
            <router-link to="/addnode">
            
                <el-button type="primary" id="add_btn">添加数据</el-button>
            </router-link>
            
        </div>
        
        <div class='disease_table'>
            <el-table 
            :data="tableData" heigt="500" border style="width:85%">
                <el-table-column prop="disease" label="适应证" width="330"></el-table-column>
                <el-table-column prop="type" label="适应证类型" width="330"></el-table-column>
                <el-table-column prop="drugtype" label="药品类型" width="330"></el-table-column>
                <el-table-column fixed="right" label="操作" width="100">
                    
                    <template slot-scope="scope">
                        <el-button type="text" size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                        <el-button type="text" size="small" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
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
            value:'',
            searchVal:"",
            tableData:[],
            radio: 0,
            
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
            const path = `http://localhost:5000/graph/query/indication/search`

            var label = this.radio

            axios
            .get(path,{
                params:{
                    table: "indication",
                    msg: search,
                    msg2: label
                }
            })
            .then(response => {
                var is_success = response.data.code
                if(is_success == 200){
                    this.tableData = response.data.data
                    this.value = response.data.value
                    
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
.disease_title{
    font-size: 32px;
    font-weight: bold;
    text-align: left;
    margin-left:13%;
    margin-top:100px;
}
.disease_search{
    width:74%;
    margin-left:13%;
    margin-top:40px;
    
}

.disease_input{
    float:left;
    height:30px;
    width:200px;
    margin-top:5px;
}

.disease_table{
    margin-left: 13%;
    margin-top:50px;
    margin-bottom:100px;
    
}

#add_btn{
    float: right;
    margin-left:100%;
    position:relative;
    top:-40px;
}

#search_btn{
    float:left;
    margin-left:10px;
}
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

#back-btn{
    margin-left:90%;
    position:relative;
    top:-25px;
}

</style>

