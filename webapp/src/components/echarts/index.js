import BaseEchart from './baseEchart';
import React, { PureComponent } from 'react';
import { Layout, Dropdown, Button, Menu, Row, Col, Tabs } from "antd";
import {
    MenuUnfoldOutlined,
    MenuFoldOutlined,
    UserOutlined,
    VideoCameraOutlined,
    UploadOutlined,
    GithubOutlined,
    SearchOutlined,
    FileAddOutlined,
    FileOutlined,
    AreaChartOutlined,
    EditOutlined
} from "@ant-design/icons";




const View = () => {

    function handleMenuClick(e) {
        // message.info('Click on menu item.');
        console.log('click', e);
    }

    let xAxisValue = ['电子元件', '汽车行业', '通讯行业', '机械行业', '家电行业', '电子信息',
        '医疗行业', '输配电气', '安防设备', '纺织服装', '金属制品', '交运设备', '仪器仪表',
    ]

    let yAxisValue = [{

        type: 'value',
        scale: true,
        name: '库存周转率(次\年)',
        max: 30,
        min: 0,
        interval: 5,
        boundaryGap: [0.4, 0.4]

    }, {

        type: 'value',
        scale: true,
        name: '百分比',
        max: 30,
        min: 0,
        interval: 5,
        boundaryGap: [0.4, 0.4],
        axisLabel: {
            formatter: '{value} %'
        }

    },]
    let seriesName = ['2019-09库存占总资产比例(行业)', '2014-2019.09最小库存周转率(企业)',
        '2014-2019.09最大库存周转率(企业)', '2014-2019.09最小库存周转率(行业)',
        '2014-2019.09最大库存周转率(行业)', '2019-09库存周转率(行业)',
    ]
    let seriesDatas = [
        [6.82, 8.38, 20.21, 12.23, 9.35, 18.57, 8.49, 11.75, 14.64, 26.41, 15.88, 15.16, 9.57],
        [0.80, 2.06, 0.15, 0.62, 2.56, 0.80, 0.43, 1.10, 0.34, 0.99, 2.38, 1.24, 1.45],
        [14.16, 18.33, 10.37, 6.13, 13.22, 22.87, 4.21, 7.27, 5.37, 7.99, 14.79, 18.87, 8.43
        ],
        [5.11, 8.86, 2.54, 2.51, 5.68, 3.68, 2.39, 2.18, 2.96, 2.22, 3.20, 2.46, 2.95
        ],
        [7.48, 12.52, 6.24, 4.06, 7.65, 6.78, 2.89, 2.98, 4.20, 3.15, 5.06, 3.33, 3.78
        ],
        [6.19, 8.86, 5.15, 4.06, 7.02, 3.68, 2.42, 2.74, 2.96, 2.22, 3.20, 2.80, 2.95
        ]

    ]



    let echartsConfig = {
        title: {
            text: '库存管理分析',
            align: 'center',
            right: 'center'
        },
        grid: {
            left: '3%',
            right: '3%',
            bottom: '3%',
            top: '120',
            containLabel: true
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            top: '10%',
            bottom: '10%',

        },
        color: ['rgba(128, 128, 128, 0.5)', 'red', '#61a0a8', '#d48265', '#91c7ae', '#749f83', '#ca8622', '#bda29a', '#6e7074', '#546570', '#c4ccd3'],

        series: [{

            type: 'bar',
            yAxisIndex: 1,
            barWidth: '30%'
        }, {

            type: 'scatter',
            symbolSize: 15,
        },
        {

            type: 'scatter',
            symbolSize: 16,

        },
        {

            type: 'scatter',
            symbolSize: 17,
        },
        {

            type: 'scatter',
            symbolSize: 18,

        },
        {

            type: 'scatter',
            symbolSize: 19,
        }]


    }

    const menu = (
        <Menu onClick={handleMenuClick}>

            {seriesName.map((item, index) => (<Menu.Item key={index}>
                <UserOutlined />
                {item}
            </Menu.Item>))}



        </Menu>
    );


    return (
        <Layout>
            <Layout
                style={{
                    paddingTop: 10,
                    marginBottom: 10
                }}
            >
                <Row >
                    <Col span={16}>
                        <BaseEchart echartsConfig={echartsConfig} xAxisValue={xAxisValue} yAxisValue={yAxisValue} seriesDatas={seriesDatas} seriesName={seriesName} />

                    </Col>
                    <Col span={8}>
                        <Row  >
                            <Dropdown overlay={menu}>
                                <Button icon={<AreaChartOutlined />}>
                                    系列数据设置
                                </Button>
                            </Dropdown>
                        </Row>

                    </Col>
                </Row>
            </Layout>
        </Layout>

    )

}

export default View;