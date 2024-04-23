odoo.define(
    "face_recognized_attendance_login.my_attendance",
    function (require) {
        "use strict";
        var core = require("web.core");
        var Widget = require("web.Widget");
        var rpc = require("web.rpc");
        var login = 0;
        // MyAttendances.include({
        //     update_attendance: async function () {
        //         await rpc
        //             .query({
        //                 model: "hr.employee",
        //                 method: "get_login_screen",
        //             })
        //             .then(function (data) {
        //                 login = data;
        //             });
        //         if (login == 1) {
        //             window.alert("Success to recognize the face. ");
        //         } else {
        //             window.alert("Failed to recognize the face. Please try again....");
        //         }
        //     },
        // });
    }
);
