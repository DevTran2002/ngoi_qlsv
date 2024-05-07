odoo.define('qlnv.attendances_login', function (require) {
    "use strict";

    console.log("Load module")
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');

    var ClientAction = AbstractAction.extend({
        contentTemplate : 'abcde'
    });

    core.action_registry.add('my-custom-action', ClientAction);
    return ClientAction;
});