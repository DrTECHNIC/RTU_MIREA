package com.vrazhenko.documentfeature.ui;

import com.vaadin.flow.component.combobox.ComboBox;
import com.vaadin.flow.component.dependency.CssImport;
import com.vaadin.flow.component.grid.Grid;
import com.vaadin.flow.component.grid.GridSortOrder;
import com.vaadin.flow.component.orderedlayout.FlexComponent;
import com.vaadin.flow.component.orderedlayout.HorizontalLayout;
import com.vaadin.flow.component.orderedlayout.VerticalLayout;
import com.vaadin.flow.component.textfield.TextField;
import com.vaadin.flow.data.provider.SortDirection;
import com.vaadin.flow.data.value.ValueChangeMode;
import com.vaadin.flow.router.Route;
import com.vrazhenko.base.ui.MainLayout;
import com.vrazhenko.documentfeature.Document;
import com.vrazhenko.documentfeature.DocumentService;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.List;

@CssImport("./styles/grid-styles.css")
@Route(value = "documents", layout = MainLayout.class)
public class DocumentListView extends VerticalLayout {

    private final DocumentService documentService;

    private final Grid<Document> grid = new Grid<>(Document.class);
    private final TextField searchField = new TextField("Поиск по названию");
    private final ComboBox<String> typeFilter = new ComboBox<>("Тип документа");

    public DocumentListView(@Autowired DocumentService documentService) {
        this.documentService = documentService;

        searchField.setPlaceholder("Введите часть названия...");
        searchField.setClearButtonVisible(true);
        searchField.setValueChangeMode(ValueChangeMode.LAZY);
        searchField.addValueChangeListener(e -> updateList());

        typeFilter.setItems("Все", "Приказ", "Распоряжение", "Служебная записка");
        typeFilter.setValue("Все");
        typeFilter.setClearButtonVisible(false);
        typeFilter.addValueChangeListener(e -> updateList());

        HorizontalLayout filters = new HorizontalLayout(searchField, typeFilter);
        filters.setAlignItems(FlexComponent.Alignment.END);

        configureGrid();

        add(filters, grid);

        updateList();
    }

    private void configureGrid() {
        grid.removeAllColumns();

        grid.addColumn(Document::getTitle)
                .setHeader("Название")
                .setSortable(true)
                .setKey("title");

        grid.addColumn(Document::getRegNumber)
                .setHeader("Регистрационный номер");

        grid.addColumn(Document::getRegDate)
                .setHeader("Дата регистрации")
                .setSortable(true)
                .setKey("regDate");

        grid.addColumn(Document::getType)
                .setHeader("Тип документа");

        grid.addColumn(Document::isUrgent)
                .setHeader("Срочный документ")
                .setKey("urgent");

        grid.addColumn(doc -> doc.getCounterparty() != null ? doc.getCounterparty().getName() : "")
                .setHeader("Контрагент")
                .setKey("counterparty");

        grid.setSizeFull();

        grid.sort(List.of(
                new GridSortOrder<>(grid.getColumnByKey("regDate"), SortDirection.DESCENDING)
        ));
    }

    private void updateList() {
        String searchTerm = searchField.getValue();
        String selectedType = typeFilter.getValue();
        grid.setItems(documentService.findDocuments(searchTerm, selectedType));
    }
}
