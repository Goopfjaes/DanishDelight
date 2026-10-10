package dk.danskdelight.registry;

import dk.danskdelight.DanskDelight;
import dk.danskdelight.item.MealItem;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.effect.MobEffect;
import net.minecraft.world.effect.MobEffectInstance;
import net.minecraft.world.food.FoodProperties;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.Items;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

public class ModItems {
    public static final DeferredRegister<Item> ITEMS =
            DeferredRegister.create(ForgeRegistries.ITEMS, DanskDelight.MOD_ID);

    // ---- Ingredienser (kan ikke spises - bruges i Farmer's Delight's Cooking Pot) ----

    /** Kulør: brændt sukker i en glasflaske. Giver flasken tilbage når den bruges. */
    public static final RegistryObject<Item> KULOR = ITEMS.register("kulor",
            () -> new Item(new Item.Properties().stacksTo(16).craftRemainder(Items.GLASS_BOTTLE)));

    /** Brun sovs i en skål. Giver skålen tilbage når den bruges. */
    public static final RegistryObject<Item> BRUN_SOVS = ITEMS.register("brun_sovs",
            () -> new Item(new Item.Properties().stacksTo(16).craftRemainder(Items.BOWL)));

    /** Bernaise i en skål. Giver skålen tilbage når den bruges. */
    public static final RegistryObject<Item> BERNAISE = ITEMS.register("bernaise",
            () -> new Item(new Item.Properties().stacksTo(16).craftRemainder(Items.BOWL)));

    // ---- Mad ----

    /** Flæskesteg med sprød svær. */
    public static final RegistryObject<Item> FLAESKESTEG = ITEMS.register("flaeskesteg",
            () -> new MealItem(new Item.Properties().stacksTo(16).food(
                    new FoodProperties.Builder()
                            .nutrition(8)
                            .saturationMod(0.8F)
                            .meat()
                            .build())));

    /** Flæskefråder: flæskesteg med brun sovs, kartofler og kål. */
    public static final RegistryObject<Item> FLAESKEFRADER = ITEMS.register("flaeskefrader",
            () -> new MealItem(new Item.Properties().stacksTo(16).food(
                    withComfort(new FoodProperties.Builder()
                            .nutrition(12)
                            .saturationMod(0.8F), 6000)
                            .build())));

    /** Kylling bernaise: kylling, ris og bernaise i en skål. */
    public static final RegistryObject<Item> KYLLING_BERNAISE = ITEMS.register("kylling_bernaise",
            () -> new MealItem(new Item.Properties().stacksTo(16).craftRemainder(Items.BOWL).food(
                    withComfort(new FoodProperties.Builder()
                            .nutrition(11)
                            .saturationMod(0.8F), 3600)
                            .build())));

    /**
     * Tilføjer Farmer's Delight's "Comfort"-effekt (farmersdelight:comfort) til maden.
     * Effekten slås op i registret, så modden ikke behøver at kende FD's klasser.
     */
    private static FoodProperties.Builder withComfort(FoodProperties.Builder builder, int ticks) {
        MobEffect comfort = ForgeRegistries.MOB_EFFECTS.getValue(
                new ResourceLocation("farmersdelight", "comfort"));
        if (comfort != null) {
            builder.effect(new MobEffectInstance(comfort, ticks, 0), 1.0F);
        }
        return builder;
    }
}
