import Entity
import EntityPortfolio

portfolio = EntityPortfolio.EntityPortfolio()

def test_edit_asset():
    new_asset = Entity.Entity(49.2, 4, "test asset", "test desc", False, "n/a")
    portfolio.add_asset(new_asset)
    assert new_asset.get_single_value() == 49.2
    assert new_asset.get_amount() == 4
    assert new_asset.get_total_value() == 196.8 #49.2 * 4
    assert new_asset.get_name() == "test asset"
    assert new_asset.get_description() == "test desc"
    assert new_asset.get_auto_update() == False

    new_asset.set_amount(2)
    new_asset.set_single_value(10)
    new_asset.set_name("test asset 2")
    new_asset.set_description("test desc 2")

    assert new_asset.get_single_value() == 10
    assert new_asset.get_amount() == 2
    assert new_asset.get_total_value() == 20
    assert new_asset.get_name() == "test asset 2"
    assert new_asset.get_description() == "test desc 2"
    
    

def test_edit_liability():
    new_liability = Entity.Entity(49.2, 4, "test liability", "test desc", False, "n/a")
    portfolio.add_liability(new_liability)
    assert new_liability.get_single_value() == 49.2
    assert new_liability.get_amount() == 4
    assert new_liability.get_total_value() == 196.8 #49.2 * 4
    assert new_liability.get_name() == "test liability"
    assert new_liability.get_description() == "test desc"
    assert new_liability.get_auto_update() == False

    new_liability.set_amount(2)
    new_liability.set_single_value(10)
    new_liability.set_name("test liability 2")
    new_liability.set_description("test desc 2")

    assert new_liability.get_single_value() == 10
    assert new_liability.get_amount() == 2
    assert new_liability.get_total_value() == 20
    assert new_liability.get_name() == "test liability 2"
    assert new_liability.get_description() == "test desc 2"
