const UNIT_CATEGORY = "#categories-menu",
    UNIT_FROM = "#sub-units-menu-from",
    UNIT_TO = "#sub-units-menu-to",
    UNIT_VALUE = "#fromUnitValue",
    CONVERT_BTN = "#buttonConvert",
    RESULT = "#result";
    


function InitOnStart()
{
    $(UNIT_FROM).prop('disabled', true);
    $(UNIT_TO).prop('disabled', true);
    $(CONVERT_BTN).prop('disabled', true);
    $(UNIT_VALUE).prop('disabled', true);
}

function InitSubUnitDisplay()
{
    $(UNIT_CATEGORY).change(function (e)
    {
        $(UNIT_FROM).empty();
        $(UNIT_FROM).prop('disabled', false);

        $.ajax({
            url: '/units-update?userCategory=' + document.getElementById('categories-menu').value,
            success: function (data) {
                $(UNIT_FROM).slice(1).remove();

                FillSubUnits(data["subUnits"])
            }
        });
        e.preventDefault();
    });
}

function InitConversionMechanism()
{
    let testCategory = "time",
        testFrom = "second",
        testTo = "minute",
        testValue = 50;

    $(CONVERT_BTN).click(function (e)
    {
        $.ajax({
            url: "/convert?userCategory=" + $(UNIT_CATEGORY).val() +
                "&unitFrom=" + $(UNIT_FROM).val() +
                "&unitFromAmount=" + $(UNIT_VALUE).val() +
                "&unitTo=" + $(UNIT_TO).val(),
            success: function (data)
            {
                $(RESULT).text(data["result"]);
            }
        });
        e.preventDefault();
    });



    /*
     *     let testCategory = "time",
        testFrom = "second",
        testTo = "minute",
        testValue = 50;
     * 
     *         $.ajax({
            url: "/convert?userCategory=" + testCategory +
                "&unitFrom=" + testFrom +
                "&unitFromAmount=" + testValue +
                "&unitTo=" + testTo,
            success: function (data) {
                $(RESULT).text(data["result"]);
            }
        });
    */

}


function InitEvents()
{
    // Sequence:
    // Select a category -> select unit from -> select unit to -> select unit value -> convert button active

    $(UNIT_FROM).change(function (e)
    {
        $(UNIT_VALUE).prop('disabled', false);
        e.preventDefault();
    });

    $(UNIT_VALUE).on("input", function (e) {
        $(UNIT_TO).prop('disabled', false);
        e.preventDefault();
    });

    $(UNIT_TO).change(function (e) {
        $(CONVERT_BTN).prop('disabled', false);
        e.preventDefault();
    });
}

function FillSubUnits(data)
{
    let len = data.length
    for (i = 0; i < len; i++)
    {
        $(UNIT_FROM).append("<option data-toggle='tooltip' data-placement='top' title='" + data[i]["desc"] +"'>" + data[i]["unit"] + "</option>");
        $(UNIT_TO).append("<option data-toggle='tooltip' data-placement='top' title='" + data[i]["desc"] + "'>" + data[i]["unit"] + "</option>");
    }
}