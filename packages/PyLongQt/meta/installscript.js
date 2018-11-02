function Component() {
}

Component.prototype.createOperations = function()
{
    // call default implementation
    component.createOperations();
    // ... add custom operations
    var winpath = installer.environmentVariable("PYTHONPATH")+";@TargetDir@/lib";
    component.addOperation("EnvironmentVariable","PYTHONPATH",winpath,true);
}
