odoo.define('qlnv.attendances_login', function (require) {
    "use strict";

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var rpc = require('web.rpc');
    const session = require('web.session');
    var web_client = require('web.web_client');
    var QWeb = core.qweb;

    const { useState} = owl;

    var ClientAction = AbstractAction.extend({
        contentTemplate : 'attendances_login_template',
        events: {
            "click .attendance_sign_in_out": _.debounce(function() {
                this.update_attendance();
            }, 200, true),
        },
        start: function () {
            var self = this;
            return this._super().then(function () {
                self.render_attendances_user();
            });
        },
        willStart:function(){
            var self = this;
            var def = this._rpc({
                model: 'res.users',
                method: 'get_model_data',
                args: [],
            })
            .then(function (res) {
                debugger
                self.res = res
            });

        return Promise.all([def, this._super.apply(this, arguments)]);
        },

        render_attendances_user:function(){
            debugger
            var self = this
            console.log(this.res)
            self.$('.block_attendances').append(QWeb.render('userAttendances', { widget: this.res }));

        },

        update_attendance:function(){
            console.log('check button')
            var self = this;
            this._rpc({
                model: 'hr.face.recognition',
                method: 'get_login',
                args: [],
            }).then(function (result) {
                console.log(result.params);
                var res = result.params
                self.displayNotification({  title: res.title, type: res.type , message: res.message,sticky : res.sticky });
            });
        },

        

    });

    core.action_registry.add('attendances-login-action', ClientAction);
    return ClientAction;
});