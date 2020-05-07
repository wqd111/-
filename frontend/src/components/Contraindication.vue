<template>
    <div>
        <div class='breadcrumb'>
            <el-breadcrumb separator="/" class="bc">
                <el-breadcrumb-item :to="{ path: '/mainwindow' }">首页</el-breadcrumb-item>
                <el-breadcrumb-item :to="{ path: '/contragraph'}">禁忌证图谱</el-breadcrumb-item>
                <el-breadcrumb-item>禁忌证表格</el-breadcrumb-item>
                <router-link :to="{name: 'MainWindow'}">
                    <el-button round size="mini" id="back-btn">返回</el-button>
                </router-link>
            </el-breadcrumb>
        </div>
        <div class='disease_title'>
            <p>禁忌证</p>
        </div>
        <div id='disease_search'>
            <input v-model="searchVal" placeholder="请输入内容" class="disease_input">
            <el-button type="primary" icon="el-icon-search" @click="search_disease()" id="search_btn">搜索</el-button>
            
            <el-button type="primary" class="add_btn">添加数据</el-button>
            
        </div>
        
        <div class='disease_table'>
            <el-table 
            :data="tableData" heigt="500" border style="width:85%">
                <el-table-column prop="classification" label="药品类型" width="330"></el-table-column>
                <el-table-column prop="name" label="禁忌证" width="330"></el-table-column>
                <el-table-column prop="type" label="禁忌证类型" width="330"></el-table-column>
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
            
            searchVal:"",
            tableData: [
                {
                    classification:'二氢吡啶类CCB',
                    name:'快速型心律失常',
                    type:'相对'
                },{
                    classification:'二氢吡啶类CCB',
                    name:'心力衰竭',
                    type:'相对'
                },{
                    classification:'非二氢吡啶类CCB',
                    name:'二度至三度房室传导阻滞',
                    type:'绝对'
                },{
                    classification:'非二氢吡啶类CCB',
                    name:'心力衰竭',
                    type:'绝对'
                },{
                    classification:'ACEI',
                    name:'妊娠',
                    type:'绝对'
                },{
                    classification:'ACEI',
                    name:'高血钾',
                    type:'绝对'
                },{
                    classification:'ACEI',
                    name:'双侧肾动脉狭窄',
                    type:'绝对'
                },{
                    classification:'ARB',
                    name:'妊娠',
                    type:'绝对'
                },{
                    classification:'ARB',
                    name:'高血钾',
                    type:'绝对'
                },{
                    classification:'ARB',
                    name:'双侧肾动脉狭窄',
                    type:'绝对'
                },{
                    classification:'噻嗪类利尿剂',
                    name:'痛风',
                    type:'绝对'
                },{
                    classification:'噻嗪类利尿剂',
                    name:'妊娠',
                    type:'相对'
                },{
                    classification:'醛固酮拮抗剂',
                    name:'肾衰竭',
                    type:'绝对'
                },{
                    classification:'醛固酮拮抗剂',
                    name:'高血钾',
                    type:'绝对'
                },{
                    classification:'二氢吡啶类CCB',
                    name:'快速型心律失常',
                    type:'相对'
                },{
                    classification:'β受体阻滞剂',
                    name:'二度至三度房室传导阻滞',
                    type:'绝对'
                },{
                    classification:'β受体阻滞剂',
                    name:'哮喘',
                    type:'绝对'
                },{
                    classification:'β受体阻滞剂',
                    name:'慢性阻塞性肺病',
                    type:'相对'
                },{
                    classification:'β受体阻滞剂',
                    name:'周围血管病',
                    type:'相对'
                },{
                    classification:'α受体阻滞剂',
                    name:'体位性低血压',
                    type:'绝对'
                },{
                    classification:'α受体阻滞剂',
                    name:'心力衰竭',
                    type:'相对'
                },
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

#back-btn{
    margin-left:90%;
    position:relative;
    top:-25px;
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

.disease_input{
    float:left;
    height:30px;
    width:200px;
    margin-top:5px;
}

.disease_table{
    margin-left: 13%;
    margin-top:80px;
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

