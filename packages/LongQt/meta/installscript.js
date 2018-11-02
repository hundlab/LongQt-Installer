function Component() {
}

Component.prototype.createOperations = function() {
    component.createOperations();

    if (systemInfo.productType === "windows") {
        component.addOperation("CreateShortcut", "@TargetDir@/bin/LongQt.exe", "@StartMenuDir@/LongQt/LongQt.lnk",
            "workingDirectory=@TargetDir@/bin", "description=Simulate heart cells");
        component.addOperation("CreateShortcut", "@TargetDir@/bin/LongQtGrapher.exe", "@StartMenuDir@/LongQt/LongQtGrapher.lnk",
            "workingDirectory=@TargetDir@/bin", "description=Plot previously run simulations");
        component.addOperation("CreateShortcut", "@TargetDir@/bin/LQGridEditor.exe", "@StartMenuDir@/LongQt/LQGridEditor.lnk",
            "workingDirectory=@TargetDir@/bin", "description=Easily setup grid simulations");
    }
}
