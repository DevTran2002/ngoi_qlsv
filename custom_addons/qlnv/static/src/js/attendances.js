import { registry } from "./core/registry";

const serviceRegistry = registry.category("services");

const myService = {
    dependencies: ["notification"],
    start(env, { notification }) {
        let counter = 1;
        setInterval(() => {
            notification.add(`Tick Tock ${counter++}`);
        }, 5000);
    }
};

serviceRegistry.add("myService", myService);