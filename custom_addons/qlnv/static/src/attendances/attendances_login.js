odoo.define('qlnv.attendances_login', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var rpc = require('web.rpc');
    const session = require('web.session');
    var web_client = require('web.web_client');
    var QWeb = core.qweb;
    var login = 0;
    const { Component, useState } = owl;
    //user useState to create a state variable

    var ClientAction = AbstractAction.extend({
        contentTemplate: 'attendances_login_template',
        events: {
            "click .attendance_sign_in_out": _.debounce(function () {
                this.update_attendance();
            }, 200, true),
        },
        start: function () {
            var self = this;
            return this._super().then(function () {
                self.render_attendances_user();
            });
        },

        willStart: function () {
            var self = this;
            var def = this._rpc({
                model: 'res.users',
                method: 'get_model_data',
                args: [],
            })
                .then(function (res) {
                    debugger
                    self.res = res
                    console.log(res)
                });
            return Promise.all([def, this._super.apply(this, arguments)]);
        },

        render_attendances_user: function () {
            var self = this
            self.$('.block_attendances').append(QWeb.render('attendances_render', { widget: this.res }));
            // self.$('.block_attendances').append(QWeb.render('button_render_attendances_template', { widget: this.res }));
        },

        update_attendance: async function () {
            console.log('check button')
            var self = this;
            await this._rpc({
                model: 'hr.face.recognition',
                method: 'get_login',
                args: [],
            }).then(function (result) {
                login = result
                console.log(login)
            });

            if (login == 1) {
                var self = this;
                    this._rpc({
                        model: 'res.users',
                        method: 'create_attendances',
                        args: []
                    })
                        .then(function (result) {
                            debugger
                            console.log("create" + result)
                        });
                self.displayNotification({ title: 'Success', type: 'success', message: "Login success", sticky: false });
            }
            if (login == 2) {
                self.displayNotification({ title: 'Error', type: 'danger', message: "Please upload image", sticky: false });
            }
            if (login == 0) {
                self.displayNotification({ title: 'False', type: 'warning', message: "Login false", sticky: false });
            }
        }
    });

    core.action_registry.add('attendances-login-action', ClientAction);
    return ClientAction;
});