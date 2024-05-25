odoo.define('qlnv.chart_render', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var rpc = require('web.rpc');
    const session = require('web.session');
    var web_client = require('web.web_client');
    var QWeb = core.qweb;
    var login = 0;
    const { Component, onWillStart, useRef, onMounted } = owl
    //user useState to create a state variable
    
    var dashboardAction = AbstractAction.extend({
        template: 'chart_render_template',
        jsLibs: [
            '/web/static/lib/Chart/Chart.js',
        ],
        start: function () {
            var self = this;

            const data = {
            labels: [2021,2022,2023,2024],
                datasets: [{
                    label: 'Sản lượng thực tế',
                    data: [10232, 9213, 11242, 9102],
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                },
                {
                    label: 'Sản lượng ước tính',
                    data: [16500, 14672, 15263, 15233],
                    fill: false,
                    borderColor: 'rgba(12, 134, 75,1)',
                    tension: 0.1
                },
                {
                    label: 'Sản lượng',
                    data: [ 66, 36, 54, 46],
                    fill: false,
                    borderColor: 'rgba(233, 113, 255,1)',
                    tension: 0.1
                }]
            };
            const data1 = {
                labels: ['Chứng nhận', 'Đang phát triển', 'Chưa phát triển'],
                datasets: [{
                    label: 'Sản lượng',
                    data: [5,7,10],
                    ticks: [5],
                    backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)','rgba(233, 113, 255,0.2)'],
                    borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)','rgba(233, 113, 255,1)'],
                    borderWidth: 1
                }]
            };


            const options = {
                scales: {
                    y: {
                        beginAtZero: true,
                        stacked: true,
                    }
                }
            };

            const options1 = {
                scales: {
                    y: {
                        beginAtZero: true,
                    }
                }
            };
            const options2 = {
                scales: {
                    y: {
                        beginAtZero: true,
                    },
                    x: {
                        ticks: {
                            callback: function(value, index, values) {
                                // Hide every other label
                                return index % 2 === 0 ? value : '';
                            }
                        }
                    }
                }
            };
            

            self.renderChar('#chart_total_quantity','line', data,options) 
            self.renderChar('#chart_example','doughnut', data1,options1) 
            self.renderChar('#chart_example1','polarArea', data1,options1) 

                
            // self.renderChar('#chart_example','Vùng trồng', 'bar' ,[5,7,0], ['Vùng trồng được chứng nhận', 'Vùng trồng đang phát triển'],['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)']);
            // self.renderChar('#chart_total_quantity','Sản lượng cây điều','line', [65, 59, 80, 81, 56, 55, 40], [2020, 2021, 2022, 2023], ['rgb(75, 192, 192)'],['rgba(54, 162, 235, 0.2)'])
        },
        init: function () {
            this._super.apply(this, arguments);
            console.log('init')
        },

        renderChar: function (id,type, data,options) {
            var self = this;    
            var ctx = self.$(id);
            var myChart = new Chart(ctx, {
                type: type,
                data: data,
                options: options
    
                
            });
        },
    });

    core.action_registry.add('dashboard-action', dashboardAction);
    return dashboardAction;
});