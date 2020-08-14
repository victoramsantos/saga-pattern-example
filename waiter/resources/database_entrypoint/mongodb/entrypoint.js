db.createCollection("products");
db.products.insertMany([
    {
        name: "Batata Frita",
        type: "FOOD",
        id: 1
    },
    {
        name: "Coca",
        type: "DRINK",
        id: 2
    },
    {
        name: "Big Mac",
        type: "FOOD",
        id: 3
    },
    {
        name: "Tequila",
        type: "DRINK",
        id: 4
    },
    {
        name: "Hot Dog",
        type: "FOOD",
        id: 5
    },
    {
        name: "Torta de  limao",
        type: "FOOD",
        id: 6
    },
    {
        name: "Pizza",
        type: "FOOD",
        id: 7
    },
    {
        name: "Pitu",
        type: "DRINK",
        id: 8
    }
]);
db.createCollection("customerOrders");
db.menuCatalog.insertMany([
    {
        order: 1,
        status: "DONE",
        pendingItems: [
            1,3
        ]
    }
]);