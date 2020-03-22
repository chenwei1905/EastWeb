import React from 'react';
import ReactEcharts from 'echarts-for-react';


const BaseEchart = (props) => {
    //data必须是数组
    const { echartsConfig, xAxisValue, yAxisValue, seriesDatas, seriesName } = props;

    echartsConfig.series.map((item, index) => {
        item.data = seriesDatas[index];
        item.name = seriesName[index];
        return item;
    })

    // let getOption = () => ({
    //     title: echartsConfig.title, //标题设置
    // //     grid: echartsConfig.grid, //网格设置
    // //     tooltip: echartsConfig.tooltip, //
    // //     legend: {data:seriesName}, //现实系列的名字
    // //     color: echartsConfig.color,
    // //    xAxis: {data:xAxisValue}, //x的坐标值
    // //     yAxis: yAxisValue, //y的坐标设置
    //     //series: echartsConfig.series, //系列值
    // })

    return (<ReactEcharts
        option={{
            title: echartsConfig.title, //标题设置
            grid: echartsConfig.grid, //网格设置
            tooltip: echartsConfig.tooltip, //
            legend: {
                data: seriesName, ...echartsConfig.legend,
            }, //现实系列的名字
            color: echartsConfig.color,
            xAxis: { data: xAxisValue } || echartsConfig.xAxis, //x的坐标值不传设置为默认值
            yAxis: yAxisValue || echartsConfig.yAxisValue, //y的坐标设置
            series: echartsConfig.series, //系列值
        }}
        style={{ height: '400px', width: '100%' }}
        opts={{ renderer: 'svg' }}
        className='react_for_echarts' />)
}

export default BaseEchart;