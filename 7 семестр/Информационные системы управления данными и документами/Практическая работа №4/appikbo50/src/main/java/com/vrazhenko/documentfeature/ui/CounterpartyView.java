package com.vrazhenko.documentfeature.ui;

import com.vaadin.flow.component.button.Button;
import com.vaadin.flow.component.button.ButtonVariant;
import com.vaadin.flow.component.formlayout.FormLayout;
import com.vaadin.flow.component.grid.Grid;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.data.binder.Binder;
import com.vaadin.flow.router.Route;
import com.vaadin.flow.router.Menu;
import com.vrazhenko.base.ui.MainLayout;
import com.vrazhenko.documentfeature.Counterparty;
import com.vrazhenko.documentfeature.CounterpartyService;
import org.springframework.beans.factory.annotation.Autowired;


@Route(value = "counterparties", layout = MainLayout.class)
@Menu(title = "Контрагенты", icon = "vaadin:building", order = 2)
public class CounterpartyView extends VerticalLayout {

    private final CounterpartyService service;
    private final Grid<Counterparty> grid = new Grid<>(Counterparty.class);

    private final TextField name = new TextField("Наименование");
    private final TextField inn = new TextField("ИНН");
    private final TextField address = new TextField("Адрес");

    private final Binder<Counterparty> binder = new Binder<>(Counterparty.class);
    private Counterparty currentCounterparty = new Counterparty();

    public CounterpartyView(@Autowired CounterpartyService service) {
        this.service = service;
        grid.setColumns("name", "inn", "address");
        grid.getColumnByKey("name").setHeader("name");
        grid.getColumnByKey("inn").setHeader("INN");
        grid.getColumnByKey("address").setHeader("address");
        grid.getColumns().forEach(col -> col.setAutoWidth(true));
        updateGrid();
        FormLayout formLayout = new FormLayout(name, inn, address);
        Button saveButton = new Button("Сохранить");
        saveButton.addThemeVariants(ButtonVariant.LUMO_PRIMARY);
        saveButton.addClickListener(event -> {
            if (binder.writeBeanIfValid(currentCounterparty)) {
                service.save(currentCounterparty);
                updateGrid();
                clearForm();
            }
        });
        binder.forField(name).bind(Counterparty::getName, Counterparty::setName);
        binder.forField(inn).bind(Counterparty::getInn, Counterparty::setInn);
        binder.forField(address).bind(Counterparty::getAddress, Counterparty::setAddress);
        binder.setBean(currentCounterparty);
        add(formLayout, saveButton, grid);
    }

    private void updateGrid() {
        grid.setItems(service.findAll());
    }

    private void clearForm() {
        currentCounterparty = new Counterparty();
        binder.setBean(currentCounterparty);
    }
}
