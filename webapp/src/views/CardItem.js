import { Layout, Menu, Card } from "antd";
import {DragSource, DropTarget} from 'react-dnd';
import flow from 'lodash/flow';
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined
} from "@ant-design/icons";
import React, { Component } from 'react';



const Types = { // 设定类型，只有DragSource和DropTarget的类型相同时，才能完成拖拽和放置
    CARD: 'CARD'
};

//DragSource相关设定
const CardSource = {  //设定DragSource的拖拽事件方法
    beginDrag(props,monitor,component){ //拖拽开始时触发的事件，必须，返回props相关对象
        return {
            index:props.index
        }
    },
    endDrag(props, monitor, component){
      //拖拽结束时的事件，可选
    },
    canDrag(props, monitor){
      //是否可以拖拽的事件。可选
    },
    isDragging(props, monitor){
      // 拖拽时触发的事件，可选
    }
};

function collect(connect,monitor) { //通过这个函数可以通过this.props获取这个函数所返回的所有属性
    return{
        connectDragSource:connect.dragSource(),
        isDragging:monitor.isDragging()
    }
}

//DropTarget相关设定
const CardTarget = {
    drop(props, monitor, component){ //组件放下时触发的事件
        //...
    },
    canDrop(props,monitor){ //组件可以被放置时触发的事件，可选
        //...
    },
    hover(props,monitor,component){ //组件在target上方时触发的事件，可选
        //...
    },
    
};

function collect1(connect,monitor) {//同DragSource的collect函数
    return{
        connectDropTarget:connect.dropTarget(),
        isOver:monitor.isOver(), //source是否在Target上方
        isOverCurrent: monitor.isOver({ shallow: true }), 
        canDrop: monitor.canDrop(),//能否被放置
        itemType: monitor.getItemType(),//获取拖拽组件type
    }
}

class CardItem extends Component{

    render(){
        const { isDragging, connectDragSource, connectDropTarget} = this.props;
        let opacity = isDragging ? 0.1 : 1; //当被拖拽时呈现透明效果

        return connectDragSource( //使用DragSource 和 DropTarget
            connectDropTarget( <div> 
                <Card
                    title={this.props.title}
                    style={{ width: 300 ,opacity}}
                >
                    <p>{this.props.content}</p>
                </Card>
            </div> )
        )
    }
}

// 使组件连接DragSource和DropTarget
// let flow = require('lodash.flow');
export default flow(
    DragSource(Types.CARD,CardSource,collect),
    DropTarget(Types.CARD,CardTarget,collect1)
)(CardItem)