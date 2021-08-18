function Component() {
}

Component.prototype.createOperations = function() {
    component.createOperations();

    if (systemInfo.productType === "windows") {
        component.addOperation("CreateShortcut", "@TargetDir@/LongQt.exe", "@StartMenuDir@/LongQt/LongQt.lnk",
            "workingDirectory=@TargetDir@", "description=Simulate heart cells");
        component.addOperation("CreateShortcut", "@TargetDir@/LongQtGrapher.exe", "@StartMenuDir@/LongQt/LongQtGrapher.lnk",
            "workingDirectory=@TargetDir@", "description=Plot previously run simulations");
        component.addOperation("CreateShortcut", "@TargetDir@/LQGridEditor.exe", "@StartMenuDir@/LongQt/LQGridEditor.lnk",
            "workingDirectory=@TargetDir@", "description=Easily setup grid simulations");
    }
}
